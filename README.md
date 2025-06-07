# Week 2 - Fintech Review Analysis

This repository contains work for the 10Academy Week 2 challenge, focused on analyzing user reviews of Ethiopian fintech mobile apps.

---

## Objective

Analyze customer experience from Google Play Store reviews for Dashen Bank, CBE, and BOA apps, and generate data-driven recommendations for fintech service improvement.

---

##  Project Structure

`play_store_scraper.py`: Collects app reviews using `google-play-scraper`.
`connect_to_OracleDB.py`: Connects and inserts cleaned data into Oracle DB.
`sentiment_analysis.py`: Classifies reviews into positive/negative/neutral.
`theme_analysis.py`: Extracts and clusters keywords into themes.
`data/`: Contains raw and cleaned datasets.
`notebooks/`: Exploratory and visualization notebooks.
`README.md`, `.gitignore`, `requirements.txt`

---

##  Task Breakdown

### Task 1: Data Collection & Preprocessing
- Scrape 400+ reviews each from Dashen Bank, CBE, and BOA (Google Play).
- Clean dataset: remove duplicates, normalize dates (YYYY-MM-DD), and store in CSV.
- Output CSV columns: `review_text`, `rating`, `date`, `bank_name`, `source`.

### Task 2: Sentiment & Thematic Analysis
- Classify sentiments using `distilbert-base-uncased-finetuned-sst-2-english`.
- Extract keywords (TF-IDF/spaCy) and group into themes.
- Output: CSV with `review_id`, `review_text`, `sentiment_label`, `theme`.

### Task 3: Oracle Database Storage
- Create `bank_reviews` Oracle DB.
- Define tables: `banks`, `reviews`.
- Insert cleaned reviews using SQLAlchemy or cx_Oracle.

### Task 4: Insights & Recommendations
- Visualize sentiment trends and themes.
- Compare user feedback across banks.
- Generate actionable recommendations for each app.

---

##  Deliverables

- ✅ Clean CSVs with >1200 reviews.
- ✅ Sentiment labels and themes.
- ✅ Populated Oracle database.
- ✅ Insight report (Jupyter/Markdown/PDF).
- ✅ Well-structured GitHub repo with meaningful commits.

---

##  Requirements

See `requirements.txt` for all dependencies.

---

##  Author

Ahmed Muhammed Edris  
10Academy - AI Mastery Program, Week 2  
