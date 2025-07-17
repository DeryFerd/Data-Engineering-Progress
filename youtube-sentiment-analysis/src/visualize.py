import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("data/comments_with_sentiment.csv")

# Calculate frequecy for each sentiment
sentiment_counts = df["sentiment"].value_counts()

# Pie chart
plt.figure(figsize=(6, 6))
plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', colors=["green", "red", "gray", "orange"])
plt.title("Distribusi Sentimen Komentar")
plt.tight_layout()
plt.show()

from wordcloud import WordCloud

# Merge all comments in one string
all_text = " ".join(df["cleaned_comment"].dropna())

# Create WordCloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_text)

# Visualize WordCloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("WordCloud dari Semua Komentar")
plt.tight_layout()
plt.show()

from collections import Counter

# Count word frequency
words = all_text.split()
word_counts = Counter(words)
common_words = word_counts.most_common(10)

# Bar chart
words, counts = zip(*common_words)
plt.figure(figsize=(8, 4))
plt.bar(words, counts, color='skyblue')
plt.title("10 Kata Terbanyak")
plt.ylabel("Frekuensi")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
