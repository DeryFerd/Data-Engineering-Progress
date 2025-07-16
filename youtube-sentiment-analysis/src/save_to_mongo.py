import os
from dotenv import load_dotenv
from pymongo import MongoClient
from fetch_comments import get_comments

# Load .env untuk YOUTUBE_API_KEY (walau gak dipakai langsung, biar konsisten)
load_dotenv()

# Koneksi ke MongoDB lokal
client = MongoClient("mongodb://localhost:27017/")
db = client["youtube_db"]
collection = db["comments"]

# Ambil komentar dari video
video_id = "CRraHg4Ks_g"
comments = get_comments(video_id, max_results=500)

# Format dan simpan ke MongoDB
data_to_insert = [{"video_id": video_id, "comment": c} for c in comments]
if data_to_insert:
    collection.insert_many(data_to_insert)
    print(f"{len(data_to_insert)} komentar berhasil disimpan ke MongoDB.")
else:
    print("Tidak ada komentar yang disimpan.")
