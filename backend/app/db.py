import os
import time
import mysql.connector
from mysql.connector import Error

DB_HOST = os.environ.get("DB_HOST", "db")
DB_USER = os.environ.get("DB_USER", "appuser")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "apppassword")
DB_NAME = os.environ.get("DB_NAME", "recipe_db")

conn = None

def init_db(retries=5, delay=5):
    """Initialize MySQL connection with retries."""
    global conn
    attempt = 0
    while attempt < retries:
        try:
            conn = mysql.connector.connect(
                host=DB_HOST,
                user=DB_USER,
                password=DB_PASSWORD,
                database=DB_NAME
            )
            if conn.is_connected():
                print("✅ Connected to MySQL")
                return conn
        except Error as e:
            print(f"❌ DB connection failed: {e}. Retrying in {delay}s...")
            attempt += 1
            time.sleep(delay)
    raise Exception("Unable to connect to MySQL after several retries")
