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
items = c.execute("""SELECT id, product_name, price, CASE 
                                    WHEN quantity < 18 THEN 'restock' 
                                    ELSE 'sufficient'
                                END as status, quantity
                                FROM INVENTORY
""")
#to format my output
print("\nPlease restock these items""\nid"+"\tproduct_name"+"\t\tprice"+"\t\tstatus" "\t\tquantity\n" f'{"." *90}')

# loop through my items
for item in items:
    id, product_name, price, status, quantity = item
    print(f"{id}\t{product_name:17}{price:10}\t\t{status:9}{quantity:10}")

# to query my table to print product which is sufficient from the highest to lowest cost price
items = c.execute("""SELECT id, product_name, price, CASE 
                                    WHEN quantity > 18 THEN 'sufficient' 
                                    ELSE 'restock'
                                END as status, quantity
                                FROM INVENTORY
                                ORDER BY quantity Desc;
""")
#to format my output
print("\nPlease check again in 1week to restock items" "\nid"+"\tproduct_name"+"\t\tprice"+"\t\tstatus" "\t\tquantity\n" f'{"." *90}')

# loop through my items
for item in items:
    id, product_name, price, status, quantity = item
    print(f"{id}\t{product_name:17}{price:10}\t\t{status:9}{quantity:10}")

# to commit my query
conn.commit()

 #to close my connection 
conn.close()