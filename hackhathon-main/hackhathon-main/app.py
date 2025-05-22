from flask import Flask, request, jsonify, render_template
from analyzer import analyze_resume
import os

app = Flask(__name__)

# Folder to store uploaded resumes
UPLOAD_FOLDER = 'resumes'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'resume' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['resume']

    # Check if filename is empty
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Check if file is a PDF
    if not file.filename.lower().endswith('.pdf'):
        return jsonify({"error": "Only PDF files are supported"}), 400

    # Save the uploaded file
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    try:
        # Analyze the resume
        result = analyze_resume(filepath)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
