from .db import get_conn

def create_recipe(title, ingredients, instructions, image_url, tags, user_id):
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute(
            "INSERT INTO recipes (title, ingredients, instructions, image_url, tags, created_by) VALUES (%s,%s,%s,%s,%s,%s) RETURNING *",
            (title, ingredients, instructions, image_url, tags, user_id)
        )
        conn.commit()
        return cur.fetchone()

def get_all_recipes(search=None, tag=None):
    with get_conn() as conn, conn.cursor() as cur:
        query = "SELECT * FROM recipes"
        params = []
        if search or tag:
            query += " WHERE"
            conditions = []
            if search:
                conditions.append(" title ILIKE %s OR ingredients ILIKE %s ")
                params.extend([f"%{search}%", f"%{search}%"])
            if tag:
                conditions.append(" %s = ANY(tags) ")
                params.append(tag)
            query += " AND ".join(conditions)
        cur.execute(query, tuple(params))
        return cur.fetchall()