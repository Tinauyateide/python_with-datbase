# Importing my dependencies
import sqlite3
import csv

# creating my database
conn = sqlite3.connect("WAEC.db")

# creating my cursor
c = conn.cursor()

# creating my table format
table = """CREATE TABLE result (
                                    'student_name' TEXT,
                                    'english' INT,
                                    'mathematics' INT,
                                    'biology' INT,
                                    'economics' INT,
                                    'christian_religious_studies' INT,
                                    'government' INT,
                                    'history' INT,
                                    'literature' INT,
                                    'fine_arts' INT
                                )"""

# # create my actual table
c.execute(table)

# to open my csv file and read its contents using the csv module
with open('result.csv', "r") as u:
    reader = csv.reader(u)
    
    # to insert the values of my read file into my sqlite table
    c.executemany("""
            INSERT INTO result VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, reader)

print('Executed successfully!')

# to commit my table
conn.commit()

# to close my connection
conn.close()
