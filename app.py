from flask import Flask, request, jsonify, send_from_directory
import trafilatura
from transformers import pipeline

app = Flask(__name__)

# Global variable to store ingested content
content = []

# Initialize the question-answering pipeline
qa_pipeline = pipeline("question-answering")

@app.route('/')
def index():
    """Serve the frontend HTML page."""
    return send_from_directory('.', 'index.html')

@app.route('/ingest', methods=['POST'])
def ingest():
    """Ingest content from provided URLs."""
    global content
    content = []  # Clear previous content
    urls = request.json['urls']
    for url in urls:
        text = extract_text(url.strip())
        if text:
            content.append(text)
    return jsonify({"status": "Content ingested successfully"})

def extract_text(url):
    """Extract main text content from a URL."""
    try:
        downloaded = trafilatura.fetch_url(url)
        if downloaded:
            result = trafilatura.extract(downloaded)
            return result
    except Exception:
        return ""
    return ""

@app.route('/ask', methods=['POST'])
def ask():
    """Answer a question based on ingested content."""
    question = request.json['question']
    context = "\n\n".join(content)  # Combine content with separators
    if not context:
        return jsonify({"error": "No content ingested"})
    answer = qa_pipeline(question=question, context=context)
    return jsonify({"answer": answer['answer']})

if __name__ == '__main__':
    app.run(debug=True)
