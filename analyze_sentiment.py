import os
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer
from rake_nltk import Rake
from datetime import datetime

# Initialize analyzers
sia = SentimentIntensityAnalyzer()
rake = Rake()

# Path
input_dir = "data/processed"
output_dir = "data/enriched"
os.makedirs(output_dir, exist_ok=True)

# Loop over processed files
for file in os.listdir(input_dir):
    if file.endswith(".csv"):
        df = pd.read_csv(os.path.join(input_dir, file))
        
        # --- Sentiment Scoring ---
        df['sentiment_score'] = df['cleaned_text'].apply(lambda x: sia.polarity_scores(str(x))['compound'])
        df['sentiment_label'] = df['sentiment_score'].apply(lambda x: 'positive' if x > 0.05 else 'negative' if x < -0.05 else 'neutral')

        # --- Keyword Extraction ---
        def extract_keywords(text):
            rake.extract_keywords_from_text(str(text))
            return ', '.join(rake.get_ranked_phrases()[:5])  # Top 5 phrases

        df['keywords'] = df['cleaned_text'].apply(extract_keywords)

        # Save the enriched file
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        out_path = os.path.join(output_dir, f"enriched_{file.split('.')[0]}_{timestamp}.csv")
        df.to_csv(out_path, index=False)
        print(f"✅ Enriched and saved: {out_path}")
