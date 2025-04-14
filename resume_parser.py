import pdfminer.high_level as pdfminer
import docx2txt

def parse_resume(file):
    if file.filename.endswith('.pdf'):
        return pdfminer.extract_text(file)
    elif file.filename.endswith('.docx'):
        return docx2txt.process(file)
    else:
        raise ValueError('Unsupported file format')
