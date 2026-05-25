import re
import nltk
import pdfplumber

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# download nltk resources
nltk.download('punkt_tab')
nltk.download('stopwords')



def extract_text_from_pdf(pdf_path):

    text = ""

    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:

            extracted = page.extract_text()

            if extracted:
                text += extracted

    return text



def clean_text(text):

  
    text = text.lower()

   
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)

    return text


def remove_stopwords(text):

    stop_words = set(stopwords.words('english'))

    
    words = word_tokenize(text)

    filtered_words = [
        word for word in words
        if word not in stop_words
    ]

    return " ".join(filtered_words)