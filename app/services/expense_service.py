from db.database import get_connection
from app.models.expense import Expense

def add_expense(amount, date, description, company_id=None):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("INSERT INTO expenses (amount, date, description, company_id) VALUES (?, ?, ?, ?)", (amount, date, description, company_id))
        conn.commit()
        return cursor.lastrowid
    
def get_expense(id):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM expenses WHERE id = ?", (id,))
        row = cursor.fetchone()
        return Expense(row[0], row[1], row[2], row[3], row[4]) if row else None