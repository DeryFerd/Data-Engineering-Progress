import os
from dotenv import load_dotenv
from pymongo import MongoClient
from fetch_comments import get_comments

load_dotenv()

# Connect to MongoDB local
client = MongoClient("mongodb://localhost:27017/")
db = client["youtube_db"]
collection = db["comments"]

# Scraping comments from Youtube video
video_id = "CRraHg4Ks_g"
comments = get_comments(video_id, max_results=500)

# Save comments to MongoDB
data_to_insert = [{"video_id": video_id, "comment": c} for c in comments]
if data_to_insert:
    collection.insert_many(data_to_insert)
    print(f"{len(data_to_insert)} comments sucessfully saved to MongoDB.")
else:
    print("No comments are saved.")
