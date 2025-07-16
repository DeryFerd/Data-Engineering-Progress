from pymongo import MongoClient
import pandas as pd
from preprocess import clean_text

# Koneksi ke MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["youtube_db"]
collection = db["comments"]

# Ambil data dari MongoDB
data = list(collection.find())
df = pd.DataFrame(data)

# Bersihkan semua komentar
df["cleaned_comment"] = df["comment"].apply(clean_text)

# Tampilkan 10 komentar pertama
print(df[["comment", "cleaned_comment"]].head(10))

# Simpan hasil ke CSV (opsional)
df.to_csv("data/cleaned_comments.csv", index=False, encoding='utf-8-sig')
