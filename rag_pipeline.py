import os
os.environ["TRANSFORMERS_OFFLINE"] = "1"
os.environ["HF_DATASETS_OFFLINE"] = "1"

from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

load_dotenv()

VECTOR_STORE_PATH = "vector_store"
DATA_PATH = "data/college_faq.pdf"

# ── Embedding Model ─────────────────────────
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    model_kwargs={"local_files_only": True}
)

# ── Build Vector Store ──────────────────────
def build_vector_store():
    print("📄 Loading documents...")

    loader = PyPDFLoader(DATA_PATH)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(documents)
    print(f"✅ Created {len(chunks)} chunks")

    db = FAISS.from_documents(chunks, embeddings)
    db.save_local(VECTOR_STORE_PATH)

    print("💾 Vector store saved!")
    return db


# ── Load Vector Store ───────────────────────
def load_vector_store():
    if os.path.exists(VECTOR_STORE_PATH) and os.path.exists(os.path.join(VECTOR_STORE_PATH, "index.faiss")):
        print("📂 Loading existing vector store...")
        return FAISS.load_local(
            VECTOR_STORE_PATH,
            embeddings,
            allow_dangerous_deserialization=True
        )

    print("⚠️ No vector store found. Building new one...")
    return build_vector_store()


# ── LLM (Groq) ──────────────────────────────
llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.3
)

# ── Prompt (IMPROVED 🔥) ────────────────────
prompt = PromptTemplate.from_template("""
You are a helpful AI assistant for Annamacharya University (AITS Rajampet).

Answer the user's question using the context below.

RULES:
- Give clear, human-like answers
- Use simple language
- If exact answer is not found, give closest relevant info
- Do NOT say "I don't have information" unless totally unrelated

Context:
{context}

Question: {question}

Answer:
""")

# ── Format Docs ─────────────────────────────
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


# ── Build QA Chain ──────────────────────────
def get_qa_chain():
    db = load_vector_store()

    retriever = db.as_retriever(search_kwargs={"k": 6})

    chain = (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain


# ── Lazy Init ───────────────────────────────
_qa_chain = None


# ── Main Function ───────────────────────────
def get_answer(question: str) -> dict:
    global _qa_chain

    if _qa_chain is None:
        print("🔧 Initializing QA chain...")
        _qa_chain = get_qa_chain()
        print("✅ QA chain ready!")

    print(f"👉 Question: {question}")

    # 🔥 Basic fallback (fast response)
    if "annamacharya university" in question:
        return {
            "answer": "Annamacharya University is a private university located in Rajampet, Andhra Pradesh, offering courses in engineering, management, sciences, and more.",
            "sources": []
        }

    try:
        answer = _qa_chain.invoke(question)

        if not answer or len(answer.strip()) < 10:
            answer = "I’m not fully sure yet 🤔. You can ask about admissions, courses, fees, or campus facilities."

    except Exception as e:
        print(f"❌ LLM Error: {e}")
        answer = "Something went wrong while fetching the answer."

    print(f"🤖 Answer: {answer}")

    return {
        "answer": answer,
        "sources": []
    }