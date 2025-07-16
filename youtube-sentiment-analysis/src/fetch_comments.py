import os
import googleapiclient.discovery
from dotenv import load_dotenv

# Load API Key dari .env
load_dotenv()
api_key = os.getenv("YOUTUBE_API_KEY")

# Inisialisasi client YouTube
youtube = googleapiclient.discovery.build("youtube", "v3", developerKey=api_key)

def get_comments(video_id, max_results=500):
    comments = []
    next_page_token = None

    while len(comments) < max_results:
        request = youtube.commentThreads().list(
            part="snippet",
            videoId=video_id,
            maxResults=min(100, max_results - len(comments)),  # 100 max per call
            textFormat="plainText",
            pageToken=next_page_token
        )
        response = request.execute()

        for item in response.get("items", []):
            top_comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            comments.append(top_comment)

        # Cek apakah ada halaman selanjutnya
        next_page_token = response.get("nextPageToken")
        if not next_page_token:
            break

    return comments

