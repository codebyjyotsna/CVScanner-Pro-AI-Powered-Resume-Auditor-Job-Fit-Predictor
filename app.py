from flask import Flask, request, jsonify
from resume_parser import parse_resume
from similarity_checker import calculate_similarity
from suggestion_engine import generate_suggestions

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_files():
    if 'resume' not in request.files or 'jd' not in request.files:
        return jsonify({'error': 'Both resume and job description must be uploaded'}), 400

    resume_file = request.files['resume']
    jd_file = request.files['jd']

    # Parse text from files
    resume_text = parse_resume(resume_file)
    jd_text = jd_file.read().decode('utf-8')

    # Calculate similarity
    match_score, labels = calculate_similarity(resume_text, jd_text)

    # Generate suggestions
    suggestions = generate_suggestions(resume_text, jd_text)

    return jsonify({
        'match_score': match_score,
        'labels': labels,
        'suggestions': suggestions
    })

if __name__ == '__main__':
    app.run(debug=True)
