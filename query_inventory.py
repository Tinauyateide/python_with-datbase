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
# to query my table to check which items need to be restocked 
items = c.execute("""SELECT * FROM INVENTORY WHERE quantity < 18
        ORDER BY quantity ASC;
""")
#to format my output
print("product_name"+"\t\t\t quantity \n" f'{"." *70}')

# loop through my items
for item in items:
    id, product_name, price, quantity = item
    print(f"{product_name:20}{quantity:19}")

# to query my table to print product which is sufficient from the highest to lowest cost price
items = c.execute("""SELECT * FROM INVENTORY WHERE quantity > 18
            ORDER BY price DESC;
""")
#to format my output
print("product_name"+"\t\tprice"+"\t\t\t quantity \n" f'{"." *70}')

# loop through my items
for item in items:
    id, product_name, price, quantity = item
    print(f"{product_name:20}{price:10}{quantity:19}")

# to commit my query
conn.commit()

 #to close my connection 
conn.close()