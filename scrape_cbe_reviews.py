from google_play_scraper import Sort, reviews
import csv
from datetime import datetime
import os

APP_ID = "com.combanketh.mobilebanking"
bank_name = "Commercial Bank of Ethiopia"

output_dir = "C:\\Users\\ayedr\\week-2\\data"
os.makedirs(output_dir, exist_ok=True)

timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
filename = os.path.join(output_dir, f"CBE_reviews_{timestamp}.csv")

results, _ = reviews(
    APP_ID,
    lang='en',
    country='et',
    sort=Sort.NEWEST,
    count=500,
    filter_score_with=None
)

with open(filename, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=['review_text', 'rating', 'date', 'bank_name', 'source'])
    writer.writeheader()
    for entry in results:
        writer.writerow({
            'review_text': entry['content'],
            'rating': entry['score'],
            'date': entry['at'].strftime('%Y-%m-%d'),
            'bank_name': bank_name,
            'source': 'Google Play'
        })

print(f"✅ Saved {len(results)} reviews to {filename}")
