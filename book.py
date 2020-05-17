
class Book:

    def __init__(self, id=None, title="", author="", year="", isbn=""):
        self.id = id
        self.title = title.title()
        self.author = author.title()
        self.year = int(year) if year != "" else 0
        self.isbn = isbn
    
    def from_touple(self, touple):
        self.id = touple[0]
        self.title = touple[1]
        self.author = touple[2]
        self.year = touple[3]
        self.isbn = touple[4]
        return self

    def attr_touple(self):
        return (self.title, self.author, self.year, self.isbn)

    def attr_touple_with_id(self):
        return (self.title, self.author, self.year, self.isbn, self.id)