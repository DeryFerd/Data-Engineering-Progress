import sqlite3
import requests
import time
import os
import pandas as pd
import streamlit as st
import plotly.express as px
from dotenv import load_dotenv
import finnhub
from datetime import datetime

# --- Konfigurasi Baru untuk Crypto ---
load_dotenv()
API_KEY = os.getenv('FINNHUB_API_KEY')
# Format Simbol Crypto Finnhub: EXCHANGE:PAIR
SYMBOL = 'BINANCE:BTCUSDT' 
DB_NAME = 'crypto_data_lite.db' # Ganti nama DB untuk data baru

# Cek jika API Key ada
if not API_KEY:
    st.error("API Key Finnhub tidak ditemukan. Mohon set 'Secrets' di pengaturan Streamlit.")
    st.stop() 

# Setup client Finnhub
finnhub_client = finnhub.Client(api_key=API_KEY)

def setup_database():
    """Membuat database dan tabel SQLite jika belum ada."""
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    # Ganti nama tabel menjadi lebih sesuai
    cur.execute("""
        CREATE TABLE IF NOT EXISTS crypto_ticks (
            timestamp TEXT PRIMARY KEY,
            symbol TEXT NOT NULL,
            open REAL,
            high REAL,
            low REAL,
            close REAL,
            volume REAL 
        );
    """)
    conn.commit()
    conn.close()
    print(f"Database '{DB_NAME}' siap digunakan.")

def fetch_crypto_data():
    """Mengambil data harga crypto terakhir dari Finnhub."""
    try:
        # Finnhub menggunakan endpoint 'quote' untuk data real-time crypto juga
        quote = finnhub_client.quote(SYMBOL)
        if quote['c'] == 0: return None
        return {
            'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'symbol': SYMBOL,
            'open': quote['o'],
            'high': quote['h'],
            'low': quote['l'],
            'close': quote['c'],
            'volume': quote.get('d', 0) # Volume untuk crypto bisa jadi 0 atau tidak ada
        }
    except Exception as e:
        print(f"Error fetching data: {e}")
        return None

def insert_data(payload):
    """Menyisipkan data ke dalam tabel SQLite."""
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    try:
        # Sesuaikan dengan nama tabel baru
        cur.execute("""
            INSERT INTO crypto_ticks (timestamp, symbol, open, high, low, close, volume)
            VALUES (:timestamp, :symbol, :open, :high, :low, :close, :volume)
        """, payload)
        conn.commit()
    except sqlite3.IntegrityError:
        pass # Abaikan jika data duplikat
    finally:
        conn.close()

# --- Fungsi Utama Aplikasi Streamlit ---
def run_app():
    st.set_page_config(page_title="Real-Time Crypto Dashboard", layout="wide")
    st.title(f"Harga Kripto Real-Time: {SYMBOL}")

    # Buat placeholder di luar loop
    chart_placeholder = st.empty()
    data_placeholder = st.empty()
    last_update_placeholder = st.empty()

    # Loop utama aplikasi
    while True:
        # 1. Ambil data baru dan simpan
        payload = fetch_crypto_data()
        if payload:
            insert_data(payload)
            print(f"Data baru diambil dan disimpan: {payload['timestamp']}")

        # 2. Baca semua data dari database untuk ditampilkan
        try:
            conn = sqlite3.connect(DB_NAME)
            # Baca dari tabel crypto_ticks
            df = pd.read_sql_query("SELECT * FROM crypto_ticks ORDER BY timestamp DESC LIMIT 100", conn)
            conn.close()

            if not df.empty:
                df_display = df.sort_values(by="timestamp")
                # Update judul grafik
                fig = px.line(df_display, x="timestamp", y="close", title=f'Harga Penutupan {SYMBOL}')
                
                chart_placeholder.plotly_chart(fig, use_container_width=True)
                data_placeholder.dataframe(df, use_container_width=True)
                last_update_placeholder.write(f"Update Terakhir: {pd.to_datetime(df_display['timestamp'].max())}")
            else:
                chart_placeholder.write("Menunggu data pertama masuk...")

        except Exception as e:
            st.error(f"Terjadi error saat menampilkan data: {e}")

        # 3. Tunggu sebelum siklus berikutnya
        time.sleep(60)

if __name__ == "__main__":
    setup_database()
    run_app()
