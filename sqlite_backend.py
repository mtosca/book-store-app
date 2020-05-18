import sqlite3
from book import Book

class Sqlite3Database:

    def __init__(self, db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS book (id INTEGER PRIMARY KEY, title text, author text, year integer, isbn integer)")
        self.conn.commit()

    def insert(self, book):
        self.cur.execute("INSERT INTO book VALUES (NULL,?,?,?,?)", book.attr_touple())
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * FROM book")
        rows=self.cur.fetchall()
        return rows

    def search(self, book):
        self.cur.execute("SELECT * FROM book WHERE title=? OR author=? OR year=? OR isbn=?", book.attr_touple())
        rows=self.cur.fetchall()
        return rows

    def delete(self, book):
        self.cur.execute("DELETE FROM book WHERE id=?",(book.id,))
        self.conn.commit()

    def update(self, book):
        self.cur.execute("UPDATE book SET title=?, author=?, year=?, isbn=? WHERE id=?", book.attr_touple_with_id())
        self.conn.commit()
        
    def __del__(self):
        self.conn.close()