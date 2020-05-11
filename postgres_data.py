import psycopg2 as psy

def create_table(conn):
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")
    conn.commit()

def insert(conn, item, qty, price):
    cur = conn.cursor()
    cur.execute("INSERT INTO store VALUES (%s, %s, %s)", (item, qty, price))
    conn.commit()

def update(conn, item, qty, price):
    cur = conn.cursor()
    cur.execute("UPDATE store SET quantity = %s, price = %s WHERE item = %s", (qty, price, item))
    conn.commit()

def view(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM store")
    return cur.fetchall()

def delete(conn, item):
    cur = conn.cursor()
    cur.execute("DELETE FROM store WHERE item = %s", (item,))
    conn.commit()

try:
    conn = psy.connect("dbname='book_shop' user='postgres' password='postgres' host='localhost' port='5432'")
    create_table(conn)
    delete(conn, 'Coffee cup')
    delete(conn, 'Wine glass')
    insert(conn, 'Coffee cup', 40, 4.99)
    insert(conn, 'Wine glass', 40, 9.95)
    update(conn, 'Coffee cup', 66, 4.99)
    print(view(conn))

except Exception as error:
    print(error)
finally:
    conn.close()
