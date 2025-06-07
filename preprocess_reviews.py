import os
import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Download necessary resources
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')

# Paths
RAW_DIR = "data"
PROCESSED_DIR = os.path.join("data", "processed")
os.makedirs(PROCESSED_DIR, exist_ok=True)

# Text cleaning function
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)  # remove punctuation
    text = re.sub(r'\d+', '', text)      # remove digits
    tokens = nltk.word_tokenize(text)
    tokens = [t for t in tokens if t not in stopwords.words('english')]
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(t) for t in tokens]
    return ' '.join(tokens)

# Process all CSV files in /data
for filename in os.listdir(RAW_DIR):
    if filename.endswith(".csv") and "reviews" in filename.lower():
        raw_path = os.path.join(RAW_DIR, filename)
        df = pd.read_csv(raw_path)

        if 'review_text' in df.columns:
            df['cleaned_text'] = df['review_text'].astype(str).apply(clean_text)
            processed_path = os.path.join(PROCESSED_DIR, f"processed_{filename}")
            df.to_csv(processed_path, index=False)
            print(f"✅ Processed and saved: {processed_path}")
        else:
            print(f"⚠️ Skipped {filename}: no 'review_text' column")
