import psycopg2 as psy

conn_string = "dbname='book_shop' user='postgres' password='postgres' host='localhost' port='5432'"

def connect():
    conn = psy.connect(conn_string)
    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS book (
        id serial primary key,
        title varchar(128) not null,
        author varchar(128) not null,
        year int not null,
        isbn varchar(64) not null)"""
    )
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn = psy.connect(conn_string)
    cur = conn.cursor()

    cur.execute("INSERT INTO book (title, author, year, isbn) VALUES (%s, %s, %s, %s)", (title, author, year, isbn))

    conn.commit()
    conn.close()

def search(title="", author="", year=0, isbn=""):
    conn = psy.connect(conn_string)
    cur = conn.cursor()

    cur.execute("SELECT * FROM book WHERE title = %s OR author = %s OR year = %s OR isbn = %s", (title, author, year, isbn))

    rows = cur.fetchall()
    conn.close()
    return rows

def view():
    conn = psy.connect(conn_string)
    cur = conn.cursor()

    cur.execute("SELECT * FROM book")

    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = psy.connect(conn_string)
    cur = conn.cursor()

    cur.execute("DELETE FROM book WHERE id = %s", (id,))

    conn.commit()
    conn.close()

def update(id, title, author, year, isbn):
    conn = psy.connect(conn_string)
    cur = conn.cursor()

    cur.execute("UPDATE book SET title = %s, author = %s, year = %s, isbn = %s WHERE id = %s", (title, author, year, isbn, id))

    conn.commit()
    conn.close()

connect()