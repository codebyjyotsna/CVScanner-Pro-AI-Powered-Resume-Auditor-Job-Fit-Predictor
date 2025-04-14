# CVScanner Pro – AI-Powered Resume Auditor & Job Fit Predictor
CVScanner Pro is an AI tool that helps job seekers optimize resumes for specific job descriptions (JDs) by analyzing content alignment, skill match, and predicting hiring potential.

## Features
1. **Resume & JD Analyzer**: Compares keywords, roles, and skills.
2. **Job Fit Score**: Predicts match score using OpenAI embeddings.
3. **Resume Suggestions**: Provides actionable improvements.
4. **Real-Time Editing**: Inline suggestions and PDF export.

## Tech Stack
- **Frontend**: React.js, Tailwind CSS (hosted on Vercel)
- **Backend**: Flask, OpenAI API, pdfminer, docx2txt (hosted on Render/Railway)
- **NLP**: OpenAI Embeddings, spaCy, NLTK

## Deployment
1. **Frontend**: `Vercel`
2. **Backend**: `Render` or `Railway`
3. Store sensitive keys (e.g., OpenAI API) in environment variables.

## Getting Started
### Prerequisites
- Node.js, Python 3.8+, OpenAI API key.

### Steps
1. Clone the repo:  
   ```bash
   git clone https://github.com/codebyjyotsna/CVScanner-Pro.git
   ```
2. Install and run backend:
   ```bash
   cd backend
   pip install -r requirements.txt
   python app.py
   ```
3. Install and run frontend:
   ```bash
   cd ../frontend
   npm install
   npm start
   ```
4. Access the app at `http://localhost:3000`.

## Future Enhancements
- Multi-JD Matching
- Career Switcher Mode
- LinkedIn Integration
