import mysql.connector
from mysql.connector import Error
from contextlib import contextmanager

@contextmanager
def get_conn():
    try:
        conn = mysql.connector.connect(
            host="db",      # Docker service
            user="appuser",
            password="apppassword",
            database="appdb"
        )
        yield conn
    except Error as e:
        print(f"DB Connection Error: {e}")
        yield None
    finally:
        if conn and conn.is_connected():
            conn.close()
