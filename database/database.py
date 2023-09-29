import sqlite3

try:
    conn = sqlite3.connect('database.db')

    cursor = conn.cursor()

    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY, 
            username TEXT NOT NULL,
            phone INTEGER NOT NULL,
            address STRING NOT NULL,
            name STRING NOT NULL
        ) 
    """)

    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY, 
            name TEXT NOT NULL
        ) 
    """)

    cursor.execute(""" 
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY, 
            name TEXT NOT NULL, 
            price INTEGER NOT NULL, 
            src TEXT NOT NULL, 
            description TEXT NOT NULL, 
            category_id INTEGER NOT NULL,
            FOREIGN KEY (category_id) REFERENCES categories(id) 
        ) 
    """)

    cursor.execute(""" INSERT INTO categories (name) VALUES('Овощи') """)
    cursor.execute(""" INSERT INTO categories (name) VALUES('Фрукты') """)
    cursor.execute(""" INSERT INTO categories (name) VALUES('Ягоды') """)

    # Овощи

    cursor.execute("""
        INSERT INTO products (
            name, price, src, description, category_id) 
                VALUES('Огурцы', 300, 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/TEIDE.JPG/1280px-TEIDE.JPG', 'Чудное описание этого товара', 1) 
    """)
    cursor.execute("""
        INSERT INTO products (
            name, price, src, description, category_id) 
                VALUES('Морковь', 200, 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/TEIDE.JPG/1280px-TEIDE.JPG', 'Чудное описание этого товара', 1) 
    """)
    cursor.execute("""
        INSERT INTO products (
            name, price, src, description, category_id) 
                VALUES('Картофель', 100, 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/TEIDE.JPG/1280px-TEIDE.JPG', 'Чудное описание этого товара', 1) 
    """)

    # Фрукты

    cursor.execute("""
        INSERT INTO products (
            name, price, src, description, category_id) 
                VALUES('Яблоки', 300, 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/TEIDE.JPG/1280px-TEIDE.JPG', 'Чудное описание этого товара', 2) 
    """)
    cursor.execute("""
        INSERT INTO products (
            name, price, src, description, category_id) 
                VALUES('Бананы', 200, 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/TEIDE.JPG/1280px-TEIDE.JPG', 'Чудное описание этого товара', 2) 
    """)
    cursor.execute("""
        INSERT INTO products (
            name, price, src, description, category_id) 
                VALUES('Персики', 100, 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/TEIDE.JPG/1280px-TEIDE.JPG', 'Чудное описание этого товара', 2) 
    """)

    # Ягоды

    cursor.execute("""
        INSERT INTO products (
            name, price, src, description, category_id) 
                VALUES('Клубника', 300, 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/TEIDE.JPG/1280px-TEIDE.JPG', 'Чудное описание этого товара', 3) 
    """)
    cursor.execute("""
        INSERT INTO products (
            name, price, src, description, category_id) 
                VALUES('Земляника', 200, 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/TEIDE.JPG/1280px-TEIDE.JPG', 'Чудное описание этого товара', 3) 
    """)
    cursor.execute("""
        INSERT INTO products (
            name, price, src, description, category_id) 
                VALUES('Вишня', 100, 'https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/TEIDE.JPG/1280px-TEIDE.JPG', 'Чудное описание этого товара', 3) 
    """)

    conn.commit()
except sqlite3.Error as e:
    print('SQLite error:', e)
finally:
    conn.close()
