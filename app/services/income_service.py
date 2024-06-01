from db.database import get_connection
from models.income import Income
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
