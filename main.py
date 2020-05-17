from frontend import TkinterFrontend
from postgres_backend import PostgresDataBase
# from sqlite_backend import Sqlite3Database not in use but could be injected


class BookStore():

    def __init__(self, frontend, backend):
        self.fe = frontend
        self.be = backend

    def start(self):
        self.fe.start()

system = BookStore(TkinterFrontend(PostgresDataBase()), PostgresDataBase())
system.start()