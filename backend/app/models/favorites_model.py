from .db import get_conn

def add_favorite(user_id, recipe_id):
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute("INSERT INTO favorites (user_id, recipe_id) VALUES (%s,%s) ON CONFLICT DO NOTHING RETURNING *",
                    (user_id, recipe_id))
        conn.commit()
        return cur.fetchone()

def remove_favorite(user_id, recipe_id):
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute("DELETE FROM favorites WHERE user_id=%s AND recipe_id=%s RETURNING *", (user_id, recipe_id))
        conn.commit()
        return cur.fetchone()

def list_favorites(user_id):
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute("SELECT r.* FROM recipes r JOIN favorites f ON r.id=f.recipe_id WHERE f.user_id=%s", (user_id,))
        return cur.fetchall()