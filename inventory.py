import psycopg

# Establishes a connection to the PostgreSQL database named online_store and returns a Connection object.
conn = psycopg.connect("dbname=online_store")

# Repeats the menu until the user chooses to exit.
while True:

    # Menu
    print("\nONLINE STORE INVENTORY\n")
    print("1. View all products")
    print("2. Add a product")
    print("3. Update product price")
    print("4. Delete a product")
    print("5. Exit\n")

    choice = input("Choose an option: ")

    # Branching from menu options:
    if choice == "1":
        cur = conn.cursor()  # Creates a cursor to execute SQL commands.
        cur.execute("SELECT * FROM products;")  # Retrieves all products from PostgreSQL.
        rows = cur.fetchall()  # Stores the returned rows in a Python list of tuples.

        print("\nPRODUCTS:\n")

        for row in rows:
            print(row)  # Prints each product on a separate line.

    elif choice == "2":
        print()
        name = input("Enter product name: ")
        price = int(input("Enter product price: "))
        stock = int(input("Enter product stock: "))
        cur = conn.cursor()  # Creates a cursor to execute SQL commands.

        # Sends the product information to PostgreSQL.
        cur.execute(
            "INSERT INTO products (name, price, stock) VALUES (%s, %s, %s);",
            (name, price, stock)
        )

        conn.commit()  # Permanently saves the INSERT operation to the PostgreSQL database.
        print("\nProduct added successfully!")

    elif choice == "3":
        print()
        product_id = int(input("Enter product ID to update: "))
        new_price = int(input("Enter new price: "))
        cur = conn.cursor()  # Creates a cursor to execute SQL commands.

        cur.execute(
            "UPDATE products SET price = %s WHERE product_id = %s;",
            (new_price, product_id)
        )

        conn.commit()  # Permanently saves the updated price to PostgreSQL.
        print("\nProduct price updated successfully!")

    elif choice == "4":
        print()
        product_id = int(input("Enter product ID to delete: "))
        cur = conn.cursor()  # Creates a cursor to execute SQL commands.

        cur.execute(
            "DELETE FROM products WHERE product_id = %s;",
            (product_id,)
        )

        conn.commit()  # Permanently saves the deletion to PostgreSQL.
        print("\nProduct deleted successfully!")

    elif choice == "5":
        print("\nGoodbye!\n")
        break  # Exits the while loop, ending the program.

    else:
        print("\nInvalid option. Please choose 1 through 5.")

conn.close()  # Closes the PostgreSQL database connection.