import openai

openai.api_key = 'your-openai-api-key'

def generate_suggestions(resume_text, jd_text):
    prompt = f"""
    Based on the following job description (JD):
    {jd_text}

    Analyze the following resume:
    {resume_text}

    Provide actionable suggestions for improving the resume, focusing on alignment with the JD, missing keywords, and formatting tips.
    """

    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=500
    )

    return response['choices'][0]['text'].strip()
