from pymongo import MongoClient
import pandas as pd

client = MongoClient("mongodb://localhost:27017/")
db = client["youtube_db"]
collection = db["comments"]

# Ambil data dari MongoDB
data = list(collection.find())
df = pd.DataFrame(data)

# Tampilkan beberapa komentar
print(df[['comment']].head())
