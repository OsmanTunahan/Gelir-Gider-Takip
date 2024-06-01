from mysql.connector import errorcode
from app.config import Config
import mysql.connector

def get_connection():
    try:
        conn = mysql.connector.connect(
            user=Config.DATABASE_USER, 
            password=Config.DATABASE_PASSWORD,
            host=Config.DATABASE_HOST,
            database=Config.DATABASE_NAME
        )
        return conn
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        return None