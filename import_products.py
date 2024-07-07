# Gürkan Bıyık 07.04.2024
# https://www.linkedin.com/in/grkanbyk/
# https://github.com/grknbyk

# import_products.py
import json
import mysql.connector
from mysql.connector import errorcode

# Database configuration
config = {
    'user': 'admin',
    'password': 'password',
    'host': 'localhost',
    'raise_on_warnings': True,
}

# Database connection
db = mysql.connector.connect(**config)

cursor = db.cursor()

try: # Create petlebi database
    cursor.execute("CREATE DATABASE petlebi")
except mysql.connector.Error as err:
    pass

# Use petlebi database
cursor.execute("USE petlebi")
        
# Read create petlebi table query
with open('petlebi_create.sql', 'r', encoding="utf-8") as f:
    create_query = f.read()

try: # Create petlebi table
    cursor.execute(create_query)
except mysql.connector.Error as err:
    pass

# Read insert petlebi table query
with open('petlebi_insert.sql', 'r', encoding="utf-8") as f:
    insert_query = f.read()

# Load JSON data
with open('petlebi_products.json', 'r', encoding="utf-8") as json_file:
    data = json.load(json_file)
    
# Insert data into petlebi table
for product in data:
    product["images"] = json.dumps(product["images"])
    cursor.execute(insert_query, product)

db.commit()
cursor.close()
db.close()

print("Products are loaded successfully.")