import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="financial_inventory_management"
)

if connection.is_connected():
    print("Successfully connected to the database.")

connection.close()
