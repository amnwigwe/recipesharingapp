from .db import get_conn
import bcrypt

def create_user(username, email, password):
    pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute("INSERT INTO users (username, email, password_hash) VALUES (%s,%s,%s) RETURNING id, username, email",
                    (username, email, pw_hash))
        conn.commit()
        return cur.fetchone()

def get_user_by_email(email):
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute("SELECT * FROM users WHERE email=%s", (email,))
        return cur.fetchone()