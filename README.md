
# Online Store Inventory Management System

A command-line inventory management application built with Python and PostgreSQL. Users can view, add, update, and delete products, with inventory data stored in a PostgreSQL database.


## Demo

Want to see the application in action? [**Watch the project demonstration video (Demo.mov)**](Demo.mov).

The video demonstrates how to view products, add new products, update prices, and delete products using the command-line interface.


![Inventory Management Demo](demo.gif)

The demonstration shows the application running in the terminal.

## Features

- **View Products:** Retrieve and display all products stored in the database.
- **Add Products:** Insert new products with automatically generated product IDs.
- **Update Prices:** Modify the price of an existing product.
- **Delete Products:** Remove products from the database.
- **Persistent Storage:** Store inventory data in PostgreSQL.

## Technologies Used

- **Python:** Application logic and command-line interface.
- **PostgreSQL:** Relational database for storing product information.
- **Psycopg 3:** PostgreSQL database adapter for Python.
- **SQL:** Database creation, querying, insertion, updating, and deletion.

## Application Preview

```text
ONLINE STORE INVENTORY

1. View all products
2. Add a product
3. Update product price
4. Delete a product
5. Exit

Choose an option: 1

(1, 'Laptop', 850, 10)
(2, 'Mouse', 25, 50)
(3, 'Keyboard', 75, 20)
(4, 'Monitor', 200, 15)
```

## Database Structure

The application uses a PostgreSQL database named `online_store`, containing a `products` table.

| Column | Data Type | Description |
|--------|-----------|-------------|
| product_id | INTEGER | Automatically generated primary key |
| name | VARCHAR(100) | Product name |
| price | INTEGER | Product price |
| stock | INTEGER | Available inventory quantity |

## Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/jay-jain/online-store-sql.git
cd online-store-sql
```

### 2. Install Python Dependencies

Create and activate a Python virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the required library:

```bash
python -m pip install -r requirements.txt
```

### 3. Set Up PostgreSQL

Ensure PostgreSQL is installed and running.

Create the database:

```bash
psql -d postgres -f create_database.sql
```

Create the products table:

```bash
psql -d online_store -f create_tables.sql
```

The application assumes PostgreSQL is accessible through the local default connection settings.

### 4. Run the Application

```bash
python inventory.py
```

Follow the terminal menu to manage inventory.

## Project Structure

```text
online-store-sql/
├── inventory.py
├── create_database.sql
├── create_tables.sql
├── requirements.txt
├── .gitignore
├── README.md
└── demo.gif
```

## How It Works

The Python application connects to PostgreSQL using Psycopg.

When a user selects a menu option, Python executes the corresponding SQL command:

| Operation | SQL Command |
|-----------|-------------|
| View products | SELECT |
| Add product | INSERT |
| Update price | UPDATE |
| Delete product | DELETE |

PostgreSQL stores the product information, allowing changes to persist between application runs.

## Future Improvements

- Input validation and error handling
- Search products by name
- Improved terminal formatting
- Support for additional inventory attributes
