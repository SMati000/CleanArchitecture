from infrastructure.DataAccessI import DataAccessI


class UsersDataAccess(DataAccessI):
    def get(self, pk: tuple) -> bool:
        if len(pk) != 2:
            pass # ERROR

        query = "select username, password from users where username like '%s' and password like '%s'" % (pk[0], pk[1])
        print(query)
        res = self.cur.execute(query)
        return len(res.fetchall()) == 1

    def save(self, values: tuple):
        if len(values) != 2:
            pass # ERROR
        
        query = "insert into users values('%s', '%s')" % (values[0], values[1])
        self.cur.execute(query)
        self.con.commit()

    def remove(self, username: str):
        query = "delete from users where username like '%s'" % username
        self.cur.execute(query)
        self.con.commit()
