def generate_wordcloud(df, bank_name):
    text = ' '.join(df['cleaned_text'].dropna().astype(str))
    wordcloud = WordCloud(width=1000, height=600, background_color='white',
                          colormap='viridis', max_words=100, contour_width=3, contour_color='steelblue').generate(text)

    plt.figure(figsize=(12, 7))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title(f'{bank_name} - Word Cloud')
    plt.tight_layout()
    output_path = f'outputs/{bank_name}_wordcloud.png'
    plt.savefig(output_path, dpi=300)
    plt.close()
