import psycopg2 as psy

class PostgresDataBase:

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

    def insert(self, book):
        self.cur.execute("INSERT INTO book (title, author, year, isbn) VALUES (%s, %s, %s, %s)", book.attr_touple())
        self.conn.commit()

    def search(self, book):
        self.cur.execute("SELECT * FROM book WHERE title = %s OR author = %s OR year = %s OR isbn = %s", book.attr_touple())
        return self.cur.fetchall()

    def view(self):
        self.cur.execute("SELECT * FROM book")
        return self.cur.fetchall()

    def delete(self, book):
        self.cur.execute("DELETE FROM book WHERE id = %s", (book.id,))
        self.conn.commit()

    def update(self, book):
        print(book.attr_touple_with_id())
        self.cur.execute("UPDATE book SET title = %s, author = %s, year = %s, isbn = %s WHERE id = %s", book.attr_touple_with_id())
        self.conn.commit()