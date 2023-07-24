from dependency_injector import containers, providers

import sqlite3

from infrastructure.AccessController import AccessController

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

def provide_access_controller(username: str, password: str) -> AccessController:
    """
    Creates an AccessController instance. This is used from the container of dependencies with a callable provider

    Parameters
    -----------
    username: str
    password: str

    Return
    ---------
    instance: AccessController
    """
    from useCases.AccessManager import SimpleAccessManager
    from outter.DataAccess import UsersDataAccess
    
    ses = AccessController.getSession(username, password)

    container = Container(
        dataAccess = providers.Factory(UsersDataAccess),
        accessManager = providers.Factory(SimpleAccessManager)
    )

    c = AccessController(
        a = container.accessManager(container.dataAccess(), session=ses)
    )

    return c

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
    sAccessController:
        instance of an AccessController configured with a SimpleAccessManager
    """
    from useCases.AccessManager import AccessManagerI
    from infrastructure.DataAccessI import DataAccessI

    config = providers.Configuration()

    db = providers.Singleton(providers.Callable(provide_db))

    dataAccess = providers.Dependency(instance_of = DataAccessI)

    accessManager = providers.Dependency(instance_of = AccessManagerI)

    sAccessController = providers.Callable(provide_access_controller)

