from flask import Flask, request, jsonify
from summarizer import summarizer_text

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Text Summarizer API! Use /summarize to summarize text."

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    text = data.get("text", "")
    summary = summarizer_text(text)
    return jsonify({"summary": summary})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

