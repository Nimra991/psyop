import psycopg2
import os
import sys
if len(sys.argv) > 1:
    a = 1
else:
    print("Missing required argument (query)")
    sys.exit()

query = sys.argv[1]

DB = os.getenv('DATABASE')
PASS = os.getenv('DBPASS')
# Define the connection parameters
db_params = {
    'host': 'localhost',
    'database': 'postgres',
    'user': 'postgres',
    'password': 'alpha123',
}

try:
    # Establish a connection to the PostgreSQL database
    connection = psycopg2.connect(**db_params)

    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # You can now execute SQL queries using the cursor
    cursor.execute(query)

    rows = cursor.fetchall()
 
    # Do something with the data
    for row in rows:
        print(row)

    # Close the cursor and the connection
    cursor.close()
    connection.close()

except psycopg2.Error as e:
    print("Error: Unable to connect to the database")
    print(e)