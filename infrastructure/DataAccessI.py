import sqlite3


class DataAccessI:
    con = sqlite3.connect("database.db")
    cur = con.cursor()

    def get(self, pk: tuple) -> bool:
        pass

    def save(self, values: tuple):
        pass

    def remove(self, username: str):
        pass