# 🎓 AITS University RAG Chatbot

An AI-powered Retrieval-Augmented Generation (RAG) chatbot developed for **AITS (Annamacharya Institute of Technology and Sciences)** to provide accurate answers to student and university-related queries using institutional documents.

The chatbot retrieves relevant information from university PDFs and generates context-aware responses using Large Language Models (LLMs).

## 🚀 Project Overview

The AITS University RAG Chatbot is designed to answer questions related to:

* Admissions
* Courses and Departments
* Fee Structure
* Academic Calendar
* Examinations
* Placements
* Faculty Information
* Campus Facilities
* Student Services
* Frequently Asked Questions

The chatbot uses Retrieval-Augmented Generation (RAG), ensuring responses are grounded in university documents rather than relying solely on the language model's knowledge.

## ✨ Features

* 🔍 Semantic Search using Vector Embeddings
* 📄 PDF Knowledge Base Integration
* 🤖 AI-Powered Question Answering
* ⚡ Fast Document Retrieval using FAISS
* 💬 Interactive Web Interface
* 🎯 Context-Aware Responses
* 📚 University FAQ Support

## 🏗️ Project Architecture

User Query
    │
    ▼
Flask Web Application
    │
    ▼
Generate Embeddings
    │
    ▼
FAISS Vector Store
    │
Retrieve Relevant Chunks
    │
    ▼
Large Language Model
    │
Generate Response
    │
    ▼
Answer Displayed to User

## 📂 Project Structure

RAG-CHATBOT/
│
├── data/
│   └── college_faq.pdf
│
├── templates/
│   └── index.html
│
├── vector_store/
│   ├── index.faiss
│   └── index.pkl
│
├── app.py
├── rag_pipeline.py
├── requirements.txt
├── .env
├── .gitignore
│
└── README.md

### Folder Description

| Folder/File              | Description                                      |
| ------------------------ | ------------------------------------------------ |
| data/college_faq.pdf     | University FAQ document used as knowledge source |
| templates/index.html     | Frontend user interface                          |
| vector_store/index.faiss | FAISS vector database                            |
| vector_store/index.pkl   | Metadata for vector embeddings                   |
| app.py                   | Main Flask application                           |
| rag_pipeline.py          | RAG pipeline implementation                      |
| requirements.txt         | Project dependencies                             |
| .env                     | API keys and environment variables               |


## 🛠️ Technologies Used

### Frontend

* HTML5
* CSS3
* JavaScript

### Backend

* Python
* Flask

### AI & NLP

* LangChain
* Groq LLM(LLaMa 3)
* Sentence Transformers

### Vector Database

* FAISS

### Document Processing

* PyPDF2
* PDF Loader

## ⚙️ Installation

### 1. Clone Repository

git clone https://github.com/yourusername/AITS-RAG-Chatbot.git

cd AITS-RAG-Chatbot

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate Environment:

Windows

```bash
venv\Scripts\activate
```

Linux/Mac

```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory.

Example:
```env
GOOGLE_API_KEY=your_gemini_api_key
# OR
OPENAI_API_KEY=your_openai_api_key

## ▶️ Run the Application

Start Flask Server:

```bash
python app.py
```

Open Browser:

```text
http://127.0.0.1:5000
```

---

## 🔄 How the RAG Pipeline Works

### Step 1: Load PDF

The chatbot loads university information from:

```text
data/college_faq.pdf
```

### Step 2: Text Chunking

The PDF content is divided into smaller chunks for efficient retrieval.

### Step 3: Generate Embeddings

Each chunk is converted into vector embeddings.

### Step 4: Store in FAISS

Embeddings are stored in:

```text
vector_store/index.faiss
vector_store/index.pkl
```

### Step 5: Retrieve Relevant Information

When a user asks a question, the chatbot finds the most relevant chunks from the vector database.

### Step 6: Generate Response

The retrieved context is passed to the LLM, which generates an accurate answer.

## 💬 Example Questions

```text
What courses are available at AITS?

How can I apply for admission?

What is the fee structure?

What are the placement opportunities?

When are the semester examinations conducted?

What facilities are available on campus?

Who can I contact for admissions?
```

## 📸 User Interface

The chatbot provides a simple and responsive web interface where users can:

* Ask questions naturally
* Receive instant responses
* Interact with university information in real time

## 📈 Future Enhancements

* Voice Assistant Support
* Multi-Language Support
* Student Login Integration
* WhatsApp Chatbot Integration
* Real-Time Notifications
* University ERP Integration
* Mobile Application

## 🧪 Testing

Run the application locally and test using various university-related queries.

Example:

```text
Q: What courses are offered?

A: AITS offers undergraduate and postgraduate programs including...
```


### Built with ❤️ using Flask, LangChain, FAISS, and Generative AI.
