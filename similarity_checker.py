import openai
import numpy as np

openai.api_key = 'your-openai-api-key'

def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (np.linalg.norm(vec1) * np.linalg.norm(vec2))

def calculate_similarity(resume_text, jd_text):
    # Generate embeddings
    resume_embedding = openai.Embedding.create(input=resume_text, model="text-embedding-ada-002")['data'][0]['embedding']
    jd_embedding = openai.Embedding.create(input=jd_text, model="text-embedding-ada-002")['data'][0]['embedding']

    # Calculate similarity
    similarity_score = cosine_similarity(resume_embedding, jd_embedding)
    match_score = round(similarity_score * 100, 2)

    # Labeling
    if match_score >= 80:
        label = 'Great Fit'
    elif match_score >= 50:
        label = 'Needs Improvement'
    else:
        label = 'Not Aligned'

    return match_score, label
