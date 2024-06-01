from app.db.database import get_connection
from app.models.income import Income
import mysql.connector

def add_income(amount, date, description=None):
    conn = get_connection()
    if conn is None:
        return None

    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO income (amount, date, description) VALUES (%s, %s, %s)", (amount, date, description))
        conn.commit()
        return cursor.lastrowid
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()

def get_income(id):
    conn = get_connection()
    if conn is None:
        return None

    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM income WHERE id = %s", (id,))
        row = cursor.fetchone()
        return Income(row[0], row[1], row[2], row[3]) if row else None
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()

def get_all_income():
    conn = get_connection()
    if conn is None:
        return []

    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM income")
        rows = cursor.fetchall()
        return [Income(row[0], row[1], row[2], row[3]) for row in rows]
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
        conn.close()