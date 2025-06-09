import oracledb
import pandas as pd
import os
from datetime import datetime

# --- Oracle DB connection info ---
username = "System"
password = "Omebank66127"  
dsn = "127.0.0.1:1521/freepdb1"

# --- Enriched data folder ---
data_folder = r"C:\Users\ayedr\week-2\data\enriched"

# --- Connect to Oracle database ---
connection = oracledb.connect(user=username, password=password, dsn=dsn)
cursor = connection.cursor()
print("✅ Connected to Oracle Database.")

# --- Mapping of banks and their corresponding file patterns ---
bank_files = {
    "Bank of Abyssinia": ["enriched_processed_BOA_reviews_20250607_144730_20250607_164611"],
    "CBE": ["enriched_processed_CBE_reviews_20250607_143845_20250607_164611",
            "enriched_processed_CBE_reviews_20250607_144621_20250607_164611"],
    "Dashen Bank": ["enriched_processed_Dashen_reviews_20250607_145221_20250607_164611"]
}

# --- Function to insert bank if not present ---
def get_or_create_bank_id(bank_name):
    cursor.execute("SELECT bank_id FROM SYSTEM.banks WHERE name = :name", {'name': bank_name})
    row = cursor.fetchone()
    if row:
        return row[0]
    else:
        bank_id_var = cursor.var(oracledb.NUMBER)
        cursor.execute(
            "INSERT INTO SYSTEM.banks (name) VALUES (:name) RETURNING bank_id INTO :bank_id",
            {'name': bank_name, 'bank_id': bank_id_var}
        )
        return bank_id_var.getvalue()

# --- Process each bank ---
for bank_name, file_keywords in bank_files.items():
    print(f"\n📌 Processing bank: {bank_name}")
    
    # Load and concatenate files
    dfs = []
    for keyword in file_keywords:
        matching_files = [f for f in os.listdir(data_folder) if keyword in f]
        for fname in matching_files:
            fpath = os.path.join(data_folder, fname)
            print(f"   🔹 Loading file: {fpath}")
            df = pd.read_csv(fpath, sep="\t" if fpath.endswith(".tsv") else ",")
            dfs.append(df)
    
    if not dfs:
        print(f"⚠️ No files found for {bank_name}. Skipping...")
        continue
    
    df = pd.concat(dfs, ignore_index=True)
    df = df.dropna(subset=['review_text', 'rating', 'sentiment_label', 'date'])

    # Get bank_id
    bank_id = get_or_create_bank_id(bank_name)
    print(f"   🆔 Bank ID: {bank_id}")

    # Insert reviews
    inserted = 0
    for _, row in df.iterrows():
        try:
            review_text = str(row['review_text'])[:4000]
            rating = int(row['rating'])
            sentiment = str(row['sentiment_label'])
            review_date = pd.to_datetime(row['date'], errors='coerce')
            if pd.isnull(review_date):
                continue

            cursor.execute("""
                INSERT INTO reviews (bank_id, review_text, rating, sentiment, review_date)
                VALUES (:bank_id, :review_text, :rating, :sentiment, :review_date)
            """, {
                'bank_id': bank_id,
                'review_text': review_text,
                'rating': rating,
                'sentiment': sentiment,
                'review_date': review_date
            })
            inserted += 1
        except Exception as e:
            print(f"   ❌ Skipped a row due to error: {e}")

    connection.commit()
    print(f"✅ Inserted {inserted} reviews for {bank_name}.")

# --- Close DB ---
cursor.close()
connection.close()
print("\n🎉 Done! All reviews loaded by bank.")
