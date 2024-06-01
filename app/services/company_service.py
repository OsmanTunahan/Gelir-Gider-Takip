from app.db.database import get_connection
from app.models.company import Company

def add_company(name):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO companies (name) VALUES (?)", (name,))
        conn.commit()
        return cursor.lastrowid

def get_company(id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM companies WHERE id = ?", (id,))
        row = cursor.fetchone()
        return Company(row[0], row[1]) if row else None
    
def get_all_companies():
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM companies")
        rows = cursor.fetchall()
        return [Company(row[0], row[1]) for row in rows]