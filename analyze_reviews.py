import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
from load_enriched_data import load_reviews

# Load data
boa_df, cbe_df, dashen_df = load_reviews()

# === Sentiment distribution plot ===
def plot_sentiment_distribution(df, bank_name):
    plt.figure(figsize=(6, 4))
    sns.countplot(data=df, x='sentiment_label',hue='sentiment_label', palette='Set2', legend=False)
    plt.title(f"Sentiment Distribution - {bank_name}")
    plt.xlabel("Sentiment")
    plt.ylabel("Review Count")
    plt.tight_layout()
    plt.savefig(f"outputs/sentiment_distribution_{bank_name}.png")
    plt.close()

# === Word Cloud for frequent keywords ===
def generate_wordcloud(df, bank_name):
    text = ' '.join(df['cleaned_text'].dropna().astype(str))
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(f"Word Cloud - {bank_name}")
    plt.tight_layout()
    plt.savefig(f"outputs/wordcloud_{bank_name}.png")
    plt.close()

# Create output directory if needed
import os
os.makedirs("outputs", exist_ok=True)

# Generate plots for all banks
for df, name in zip([boa_df, cbe_df, dashen_df], ['BOA', 'CBE', 'Dashen']):
    plot_sentiment_distribution(df, name)
    generate_wordcloud(df, name)

print("✅ All plots saved in /outputs/")
