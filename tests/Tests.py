import unittest  
import os

import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from outter.DataAccess import UsersDataAccess
from DependenciesContainer import Container, providers


class Tests(unittest.TestCase):  
    def test_db_existence(self):
        """
        Tests the existence of the database file and its tables.
        """
        self.assertTrue(os.path.isfile(os.path.relpath("./database.db")), "../database.db no existe")
        
        c = Container()

        con = c.db()
        self.assertTrue(con is c.db(), "singleton for db object is not working")

        cur = con.cursor()

        res = cur.execute("SELECT name FROM sqlite_master where name like 'users'")
        self.assertEqual(len(res.fetchall()), 1, "Tabla users no existe")

        con.close()

    def test_db_users(self):
        """
        Tests the well functioning of the methods of UsersDataAccess class
        """
        container = Container(dataAccess = providers.Factory(UsersDataAccess))
        users = container.dataAccess()
        
        tp = ("testU", "testP")
        users.save(tp)
        self.assertTrue(users.exists(tp), "No se agrego, o no se lee correctamente el registro a la tabla users")
        users.remove((tp[0],))
        self.assertFalse(users.exists(tp), "No se elimino el registro de la tabla users")



if __name__ == '__main__':  
    unittest.main()