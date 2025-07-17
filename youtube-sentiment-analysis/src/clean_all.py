from pymongo import MongoClient
import pandas as pd
from preprocess import clean_text

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["youtube_db"]
collection = db["comments"]

# Load data from MongoDB
data = list(collection.find())
df = pd.DataFrame(data)

# Clean all comments
df["cleaned_comment"] = df["comment"].apply(clean_text)

# Show top 10 comments
print(df[["comment", "cleaned_comment"]].head(10))

# Save to CSV
df.to_csv("data/cleaned_comments.csv", index=False, encoding='utf-8-sig')
