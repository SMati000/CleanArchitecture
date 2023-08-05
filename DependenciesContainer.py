from dependency_injector import containers, providers

from useCases.AccessManager import AccessManagerI, SimpleAccessManager, sessionDTO
# from infrastructure.AccessController import AccessController
from infrastructure.DataAccessI import DataAccessI
from outter.DataAccess import UsersDataAccess

import sqlite3

def provide_db() -> sqlite3.Connection:
    """
    creates and returns an instance of Connection sqlite3.
    Also, verifies that the database is correctly set up.

    Return
    ---------
    sqlite3.Connection
    """  
    con = sqlite3.connect("database.db")
    cur = con.cursor()

    res = cur.execute("SELECT name FROM sqlite_master where name like 'users'")
    if len(res.fetchall()) == 0:
        cur.execute("CREATE TABLE users(username text primary key, password text)")
        print("Users table created successfully")
    
    return con

class Container(containers.DeclarativeContainer):
    """
    Container of dependencies

    Attributes
    ------------------
    db:
        unique instance of SQLite Connection, for "database.db"
    dataAccess:
        instance of DataAccessI
    accessManager:
        instance of AccessManagerI
    accessManager_factory:
        specific instance of accessManager dependency according to container's config
    """

    config = providers.Configuration()

    db = providers.Singleton(provide_db)
    dataAccess = providers.AbstractFactory(DataAccessI)

    accessManager = providers.Dependency(instance_of = AccessManagerI)
    accessManager_factory = providers.Factory(
        accessManager,
        dbPersister = providers.Factory(UsersDataAccess)
    )