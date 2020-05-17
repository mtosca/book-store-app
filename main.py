from frontend import TkinterFrontend
from backend import PostgresDataBase


class BookStore():

    def __init__(self, frontend, backend):
        self.fe = frontend
        self.be = backend

    def start(self):
        self.fe.start()

system = BookStore(TkinterFrontend(PostgresDataBase()), PostgresDataBase())
system.start()