from infrastructure.DataAccessI import DataAccessI


class UsersDataAccess(DataAccessI):
    """
    manage the users table from the database

    Methods
    --------
    exists(pk) -> bool:
        tries to get the row from the users table, and returns true if it exists
    save(values):
        insert that row into the users table in the database
    remove(pk):
        tries to remove, if it exists, from the users table
    """

    def exists(self, pk: tuple) -> bool:
        if len(pk) != 1:
            pass # ERROR

        query = "select username from users where username like '%s'" % pk[0]
        res = self.cur.execute(query)
        return len(res.fetchall()) == 1

    def save(self, values: tuple):
        if len(values) != 2:
            pass # ERROR
        
        query = "insert into users values('%s', '%s')" % (values[0], values[1])
        self.cur.execute(query)
        self.con.commit()

    def remove(self, pk: tuple):
        if len(pk) != 1:
            pass # ERROR

        query = "delete from users where username like '%s'" % pk[0]
        self.cur.execute(query)
        self.con.commit()
