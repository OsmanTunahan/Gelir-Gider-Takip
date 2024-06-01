from db.database import get_connection
from app.models.company import Company

def add_company(name):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO companies (name) VALUES (?)", (name,))
        conn.commit()
        return cursor.lastrowid