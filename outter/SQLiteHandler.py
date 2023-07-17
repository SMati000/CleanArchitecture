import sqlite3


class SQLiteHandler:
    def __init__(self):
        con = sqlite3.connect("database.db")
        cur = con.cursor()

        res = cur.execute("SELECT name FROM sqlite_master where name like 'users'")
        if len(res.fetchall()) == 0:
            cur.execute("CREATE TABLE users(username text primary key, password text)")
            print("Users table created successfully")

        con.close()