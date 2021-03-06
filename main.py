from frontend import TkinterFrontend
from postgres_backend import PostgresDataBase
# from sqlite_backend import Sqlite3Database not in use but could be injected


class BookStore():

    def __init__(self, frontend, backend):
        self.fe = frontend
        self.be = backend

    def start(self):
        self.fe.set_db(self.be)
        self.fe.start()

# window handler and database are "injectable", there is also a sqlite3 connector available
system = BookStore(TkinterFrontend(), PostgresDataBase())
system.start()