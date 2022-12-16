import sqlite3

query = """
CREATE TABLE IF NOT EXISTS supplier(
id INTEGER PRIMARY KEY, 
number INTEGER UNIQUE,
adress VARCHAR(50)
company_name VARCHAR(50) NOT NULL);

CREATE TABLE IF NOT EXISTS client(
id INTEGER PRIMARY KEY, 
name VARCHAR(50) NOT NULL,
number INTEGER UNIQUE);

CREATE TABLE IF NOT EXISTS pharmacy(
id INTEGER PRIMARY KEY,
adress VARCHAR(50),
number INTEGER UNIQUE);

CREATE TABLE IF NOT EXISTS categories(
id INTEGER PRIMARY KEY,
name VARCHAR(100));

CREATE TABLE IF NOT EXISTS medicines(
id INTEGER PRIMARY KEY,
category_id INTEGER NOT NULL,
name VARCHAR(50) NOT NULL,
price INTEGER NOT NULL,
FOREIGN KEY (category_id) REFERENCES category(id));

CREATE TABLE IF NOT EXISTS list(
id INTEGER PRIMARY KEY, 
pharmacy_id INTEGER NOT NULL,
medicines_id INTEGER NOT NULL,
FOREIGN KEY (pharmacy_id) REFERENCES pharmacy(id),
FOREIGN KEY (medicines_id) REFERENCES medicines(id))
"""

try:
    connection = sqlite3.connect("Pharmacy")
    cursor = connection.cursor()
    cursor.executescript(query)
    connection.commit()
except:
    pass

