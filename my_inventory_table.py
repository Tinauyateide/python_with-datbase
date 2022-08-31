# import sqlite3
import sqlite3

#check
print('sqlite imported successfully')

#create or connect to a database
conn = sqlite3.connect("Stationeries.db")

#check the connection to a database
print(":connection created successfully!") ; print(type(conn))

# create a cursor object
c = conn.cursor()

#check
print(f'cursor created successfully! \n{type(c)}')

#create a database table:
c.execute(
    """
    CREATE TABLE INVENTORY(
        id INT,
        product_name text,
        price INT,
        quantity INT
        )
        """
)
print('my products table has been created successfully')

# inputting data's to go into the stores database
my_store = [(1, "Notepads", 4000, 21),
            (2, "Envelops", 1000, 17),
            (3, "White Paper", 23000, 50),
            (4, "Markers", 2000, 50),
            (5, "Calculator", 1000, 24),
            (6, "Staples", 3500, 20),
            (7, "Pencils", 600, 40),
            (8, "Tissue Paper", 800, 30),
            (9, "Paper Basket", 1500, 60),
            (10, "Hard File", 1000, 26),
            (11, "Battery", 700, 28),
            (12, "Old School Bell", 8000, 10),
            (13, "Masking Tape", 1900, 15),
            (14, "Cleaning Solution", 2500, 17),
            (15, "Perforator", 4000, 12),
            ]

# inserting my items into table
c.executemany("INSERT INTO INVENTORY VALUES(?, ?, ?, ?)", my_store)

print('We have inserted', c.rowcount,' records to the table')

conn.commit()

c.execute("SELECT * FROM INVENTORY")

items = c.fetchall()

#format output to display in tabular form
print("id"+ "\t product_name"+ "\t\tprice" "\t\t quantity \n" f'{"." *70}')

# loop through my items
for item in items:
    id, product_name, price, quantity = item
    print(f"{id}\t{product_name:18}{price:10}{quantity:17}")

#to commit my table
conn.commit()

#to close my connection
conn.close()