import pandas as pd
from textblob import TextBlob

# Load data dari CSV
df = pd.read_csv("data/cleaned_comments.csv")

# Fungsi analisis sentimen
def get_sentiment(text):
    if not isinstance(text, str) or text.strip() == "":
        return "unknown"  # atau bisa return None juga
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.1:
        return "positive"
    elif polarity < -0.1:
        return "negative"
    else:
        return "neutral"


# Apply ke kolom komentar bersih
df["sentiment"] = df["cleaned_comment"].apply(get_sentiment)

# Tampilkan hasil
print(df[["cleaned_comment", "sentiment"]].head(10))

# Simpan hasil ke file baru
df.to_csv("data/comments_with_sentiment.csv", index=False, encoding="utf-8-sig")
