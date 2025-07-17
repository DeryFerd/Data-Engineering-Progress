from pymongo import MongoClient
import pandas as pd

client = MongoClient("mongodb://localhost:27017/")
db = client["youtube_db"]
collection = db["comments"]

# Load Data from MongoDB
data = list(collection.find())
df = pd.DataFrame(data)

# Show some comments
print(df[['comment']].head())
