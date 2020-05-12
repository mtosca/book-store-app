import psycopg2 as psy

class DataBase:

    def __init__(self):
        self.conn_string = "dbname='book_shop' user='postgres' password='postgres' host='localhost' port='5432'"
        self.conn = psy.connect(self.conn_string)
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS book (
            id serial primary key,
            title varchar(128) not null,
            author varchar(128) not null,
            year int not null,
            isbn varchar(64) not null)"""
        )
        self.conn.commit()

    def __del__(self):
        self.conn.close()

    def insert(self, title, author, year, isbn):
        self.cur.execute("INSERT INTO book (title, author, year, isbn) VALUES (%s, %s, %s, %s)", (title, author, year, isbn))
        self.conn.commit()

    def search(self, title="", author="", year="", isbn=""):
        year = int(year) if year != "" else 0 
        self.cur.execute("SELECT * FROM book WHERE title = %s OR author = %s OR year = %s OR isbn = %s", (title, author, year, isbn))
        return self.cur.fetchall()

    def view(self):
        self.cur.execute("SELECT * FROM book")
        return self.cur.fetchall()

    def delete(self, id):
        self.cur.execute("DELETE FROM book WHERE id = %s", (id,))
        self.conn.commit()

    def update(self, id, title, author, year, isbn):
        self.cur.execute("UPDATE book SET title = %s, author = %s, year = %s, isbn = %s WHERE id = %s", (title, author, year, isbn, id))
        self.conn.commit()