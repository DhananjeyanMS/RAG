from flask import Flask, request, render_template, jsonify
from text_processing import process_text  # Ensure these are imported correctly
from file_reading import read_files

app = Flask(__name__)

# Load and process documents at startup
file_paths = ["D:/Text vectorization/document2.pdf", "D:/Text vectorization/document2.pdf", "D:/Text vectorization/document2.pdf", "D:/Text vectorization/document1.docx","D:/Text vectorization/greetings.docx"]
combined_text = read_files(file_paths)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        question = request.form.get('question')
        if question:
            response = process_text(combined_text, question)
            return jsonify({'response': response})
        return jsonify({'response': 'No question provided'}), 400
    return render_template('index.html')

    

if __name__ == '__main__':
    app.run(debug=True)
