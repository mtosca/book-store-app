import sqlite3

def create_table():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()

    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)")

    conn.commit()
    conn.close()

def insert(item, qty, price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()

    cur.execute("INSERT INTO store VALUES (?, ?, ?)", (item, qty, price))

    conn.commit()
    conn.close()

def update(item, qty, price):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()

    cur.execute("UPDATE store SET quantity = ?, price = ? WHERE item = ?", (qty, price, item))

    conn.commit()
    conn.close()


def view():
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()

    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()

    conn.close()
    return rows

def delete(item):
    conn = sqlite3.connect("lite.db")
    cur = conn.cursor()

    cur.execute("DELETE FROM store WHERE item = ?", (item,))

    conn.commit()
    conn.close()


#insert('Coffee cup', 40, 4.99)
#insert('Wine glass', 40, 9.95)
#delete('Coffee cup')
#delete('Wine glass')
update('Coffee cup', 66, 4.99)
print(view())
