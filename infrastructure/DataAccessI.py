from sqlite3 import Connection, Cursor

from dependency_injector.wiring import inject, Provide

class DataAccessI:
    """
    Interface to manage tables from a database

    Methods
    --------
    exists(pk) -> bool:
        tries to get the row from a table, and returns true if it exists
    save(values):
        insert that row into a table in the database
    remove(pk):
        tries to remove, if it exists, from a table
    """
    
    con: Connection
    cur: Cursor

    @inject
    def __init__(self, db: Connection = Provide["db"]):
        self.con = db
        self.cur = self.con.cursor()

    def exists(self, pk: tuple) -> bool:
        """
        tries to get the row from a table, and returns true if it exists

        Parameters
        ------------
        pk: tuple
            primary key of the row to check

        return
        ---------
        exists: bool
            whether the row exists or not
        """
        pass

    def save(self, values: tuple):
        """
        insert that row into a table in the database

        Parameters
        ------------
        values: tuple
            row to insert into the table
        """
        pass

    def remove(self, pk: tuple):
        """
        tries to remove, if it exists, from a table

        Parameters
        ------------
        pk: tuple
            primary key of the row to remove from the table
        """
        pass