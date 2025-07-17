import pandas as pd
from textblob import TextBlob

# Load data from CSV
df = pd.read_csv("data/cleaned_comments.csv")

# Analysis sentiment function
def get_sentiment(text):
    if not isinstance(text, str) or text.strip() == "":
        return "unknown"  
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.1:
        return "positive"
    elif polarity < -0.1:
        return "negative"
    else:
        return "neutral"


# Apply to cleaned columns
df["sentiment"] = df["cleaned_comment"].apply(get_sentiment)

# print the output
print(df[["cleaned_comment", "sentiment"]].head(10))

# Save to new file
df.to_csv("data/comments_with_sentiment.csv", index=False, encoding="utf-8-sig")
