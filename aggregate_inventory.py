# import sqlite3
import sqlite3

#check
print('sqlite imported successfully')

#create or connect to a database
conn = sqlite3.connect("Stationeries.db")

#check the connection to a database
print(":connection created successfully!") 

# create a cursor object
c = conn.cursor()

#check
print(f'cursor created successfully!')

# to get the amount spent on procurement of items
c.execute("""SELECT SUM(price*quantity) FROM INVENTORY;
""")
items = c.fetchall()
[res], = items
print(f'{res} is the total amount spent on procurement of the products')

# to querresy my table from inventory to give average quantity in stock
c.execute("""SELECT AVG(quantity) AS AVERAGE_QUANTITY
        FROM INVENTORY;
        """)

items = c.fetchall()
[res], = items
print(f'{res} is the average quantity of items in stock')

# query to print the least quantity in stock
c.execute("""SELECT product_name, quantity FROM INVENTORY 
        WHERE quantity = (SELECT MIN(quantity) FROM INVENTORY);""")

items = c.fetchall()
[product_name, quantity], = items
print(f'{product_name} has the least quantity with {quantity} packs of product in stock')

# query to print the most quantity in stock
c.execute("""SELECT product_name, quantity FROM INVENTORY 
        WHERE quantity = (SELECT MAX(quantity) FROM INVENTORY);""")

items = c.fetchall()
[product_name, quantity], = items
print(f'{product_name} has the highest quantity with {quantity} packs of product in stock')