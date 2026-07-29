from flask import Flask, render_template, request, jsonify
from rag_pipeline import get_answer, build_vector_store

app = Flask(__name__)
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    if not data or "question" not in data:
        return jsonify({"error": "No question provided"}), 400
    question = data.get("question", "").strip().lower()
    if not question:
        return jsonify({"error": "Empty question"}), 400
    try:
        result = get_answer(question)
        return jsonify({
            "answer": result["answer"],
            "sources": result.get("sources", [])
        })
    except Exception as e:
        print(f"❌ Error in /chat: {e}")
        return jsonify({"error": "Something went wrong"}), 500

@app.route("/rebuild", methods=["POST"])
def rebuild():
    try:
        build_vector_store()
        return jsonify({"message": " Vector store rebuilt successfully!"})
    except Exception as e:
        print(f" Error in /rebuild: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
