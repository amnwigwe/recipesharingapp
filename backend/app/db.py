import os
import psycopg
from psycopg.rows import dict_row

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://appuser:apppassword@localhost:5432/appdb")

def get_conn():
    return psycopg.connect(DATABASE_URL, row_factory=dict_row)

def init_db():
    with get_conn() as conn, conn.cursor() as cur:
        # Users table
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                id SERIAL PRIMARY KEY,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL
            );
            """
        )
        # Recipes table
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS recipes (
                id SERIAL PRIMARY KEY,
                title TEXT NOT NULL,
                ingredients TEXT NOT NULL,
                instructions TEXT NOT NULL,
                image_url TEXT,
                tags TEXT[],
                created_by INTEGER REFERENCES users(id) ON DELETE CASCADE
            );
            """
        )
        # Favorites table
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS favorites (
                id SERIAL PRIMARY KEY,
                user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
                recipe_id INTEGER REFERENCES recipes(id) ON DELETE CASCADE,
                UNIQUE(user_id, recipe_id)
            );
            """
        )
        conn.commit()