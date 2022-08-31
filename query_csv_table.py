# importing my dependencies
import sqlite3

# create my connection to my database
conn = sqlite3.connect("WAEC.db")

#create my cursor
c = conn.cursor()

# query my database
c.execute("""SELECT * FROM result""")

items = c.fetchall()
# print(items)


# to query my table  print the highest score in maths
def math():
    query = """SELECT student_name, mathematics FROM result 
            WHERE mathematics = (SELECT MAX(mathematics) FROM result)"""

    c.execute(query)

    print(c.fetchall())

math()

# to query my table print the lowest score in english
def english():
    query = """SELECT student_name, english FROM result 
            WHERE english = (SELECT MIN(english) FROM result)"""

    c.execute(query)

    print(c.fetchall())

english()

# to query my table print the average score in maths
def average_math():
    query = """SELECT AVG(mathematics) FROM result"""

    c.execute(query)

    print(c.fetchall())

average_math()

# to query my table print the average score in english
def average_english():
    query = """SELECT AVG(english) FROM result"""

    c.execute(query)

    print(c.fetchall())

average_english()

# query my table to print the best performing student across all nine subjects 
def best_performing():
    query = """SELECT student_name, (english+mathematics+biology+economics+christian_religious_studies+government+history+literature+fine_arts) AS total FROM result
ORDER BY total DESC
LIMIT 1"""
    c.execute(query)

    print(c.fetchall())

best_performing()

# query my table to print the best performing student across all subjects 
def avg_best_performing():
    query = """SELECT student_name, AVG(english+mathematics+biology+economics+christian_religious_studies+government+history+literature+fine_arts) AS total FROM result
ORDER BY total DESC
LIMIT 1"""
    c.execute(query)

    print(c.fetchall())

avg_best_performing()