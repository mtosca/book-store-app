
class Book:

    def __init__(self, id=None, title="", author="", year=0, isbn=""):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.isbn = isbn

    def attr_touple(self):
        return (self.title, self.author, self.year, self.isbn)

    def attr_touple_with_id(self):
        return (self.title, self.author, self.year, self.isbn, self.id)