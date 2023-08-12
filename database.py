# database.py

import mysql.connector

from dotenv import dotenv_values

config = dotenv_values(".env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}

db_config = {
  'user': config.get("DATABASE_USER"),
  'password': config.get("DATABASE_PASS"),
  'host': config.get("DATABASE_HOST"),
  'database': config.get("DATABASE_SCHEMA"),
  'raise_on_warnings': bool(config.get("DEBUG"))
}

# Establish a database connection
def get_database_connection():
    try:
        connection = mysql.connector.connect(**db_config)
        return connection
    except mysql.connector.Error as e:
        print("Error while connecting to MySQL", e)
        return None

# SELECT function
def execute_select_query(query):
    connection = get_database_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            connection.close()
            return result
        except mysql.connector.Error as e:
            print("Error executing SELECT query:", e)
    return None

# INSERT function
def execute_insert_query(query, values):
    connection = get_database_connection()
    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute(query, values)
            connection.commit()
            cursor.close()
            connection.close()
            return True
        except mysql.connector.Error as e:
            print("Error executing INSERT query:", e)
    return False
