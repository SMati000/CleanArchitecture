import unittest  
import os
import sqlite3

import sys
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from outter.SQLiteHandler import SQLiteHandler

from infrastructure.DataAccessI import DataAccessI
from outter.DataAccess import UsersDataAccess


class Tests(unittest.TestCase):  
    def test_db_existence(self):
        db = SQLiteHandler()
        self.assertTrue(os.path.isfile(os.path.relpath("./database.db")), "../database.db no existe")

        con = sqlite3.connect("database.db")
        cur = con.cursor()

        res = cur.execute("SELECT name FROM sqlite_master where name like 'users'")
        self.assertEqual(len(res.fetchall()), 1, "Tabla users no existe")

        con.close()

    def test_db_users(self):
        users: DataAccessI
        users = UsersDataAccess()

        tp = ("testU", "testP")
        users.save(tp)
        self.assertTrue(users.get(tp), "No se agrego, o no se lee correctamente el registro a la tabla users")
        users.remove(tp[0])
        self.assertFalse(users.get(tp), "No se elimino el registro de la tabla users")



if __name__ == '__main__':  
    unittest.main()