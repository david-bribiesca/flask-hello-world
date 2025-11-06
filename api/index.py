from flask import Flask
import psycopg2
from dotenv import load_dotenv
import os

app = Flask(_name_)

def get_connection():
    load_dotenv()
    CONNECTION_STRING = os.getenv("CONN_STRING")
    return psycopg2.connect(CONNECTION_STRING)

@app.route('/')
def home():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About'

@app.route('/sensor')
def sensor():
    try:
        connection = get_connection()
        print("Connection successful!")
        
        # Create a cursor to execute SQL queries
        cursor = connection.cursor()
        
        # Example query
        cursor.execute("SELECT NOW();")
        result = cursor.fetchone()
        print("Current Time:", result)
    
        # Close the cursor and connection
        cursor.close()
        connection.close()
        print("Connection closed.")
        return f"Current Time: {result}"
    
    except Exception as e:
        return f"Failed to connect: {e}"
