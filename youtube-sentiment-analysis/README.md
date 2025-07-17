# 🎯 YouTube Sentiment Analysis (Data Engineering Project)

This project is a simple data engineering pipeline to perform sentiment analysis on YouTube comments. Comments are fetched via the YouTube API, stored in MongoDB, cleaned, and analyzed using Python.

---

## 🗂️ Folder Structure
```
youtube-sentiment-analysis/
├── data/
│ ├── cleaned_comments.csv # Cleaned comment data
│ └── comments_with_sentiment.csv # Comments with sentiment label
├── src/
│ ├── fetch_comments.py # Fetch YouTube comments via API
│ ├── load_from_mongo.py # Load data from MongoDB
│ ├── preprocess.py # Clean comment texts
│ └── analysis.py # Run sentiment analysis
├── .env # YouTube API key (excluded from Git)
├── .gitignore
└── requirements.txt
```

---

## 🚀 Getting Started

### 1. Clone the Repository
```
git clone https://github.com/DeryFerd/Data-Engineering-Progress.git
cd Data-Engineering-Progress/youtube-sentiment-analysis
```

### 2. Install Dependencies
Make sure you have Python installed. Then run:
```
pip install -r requirements.txt
```

### 3. Add .env File
Create a ```.env``` file in the project root and add your YouTube API key:
```
YOUTUBE_API_KEY=your_api_key_here
```

## ⚙️ Pipeline Flow
```fetch_comments.py```

→ Fetches comments from a YouTube video and stores them in MongoDB.

```load_from_mongo.py```

→ Loads the saved comments into a Pandas DataFrame.

```preprocess.py```

→ Cleans the text: lowercasing, removing URLs, punctuation, stopwords, etc.

```analysis.py```

→ Uses TextBlob to classify the sentiment (positive, neutral, negative) and saves the results to CSV.

## 📊 Output
```cleaned_comments.csv```

→ Cleaned version of the YouTube comments.

```comments_with_sentiment.csv```

→ Final dataset with sentiment labels.

## 🧠 Notes
- This is a basic version — can be extended using advanced NLP models (e.g., BERT, SVM, LSTM).

- Make sure MongoDB is running locally before executing the scripts.

## 🤖 Built by
Dery Oktoriansah — A data enthusiast exploring the Data Engineering path.
