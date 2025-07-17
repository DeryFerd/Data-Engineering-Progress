import re
import pandas as pd
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
import contractions

# Load stopword and tokenizer
nltk.download('stopwords')
nltk.download('punkt')

# Indonesian Language
stop_words = set(stopwords.words('indonesian'))

def clean_text(text):
    text = contractions.fix(text)
    text = re.sub(r"http\S+|www\S+", '', text)
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    text = text.lower()
    tokens = text.split()
    filtered = [word for word in tokens if word not in stop_words]
    return ' '.join(filtered)


if __name__ == "__main__":
    # Create sample of comment
    sample = "he's crazy!"

    cleaned = clean_text(sample)
    print("Sebelum:", sample)
    print("Sesudah:", cleaned)
