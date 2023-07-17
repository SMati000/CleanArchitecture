from dataclasses import dataclass

from entities import User
from infrastructure.DataAccessI import DataAccessI
from outter.DataAccess import UsersDataAccess
from useCases.SimpleMessageDTO import SessionMessageDTO

@dataclass(frozen=True)
class sessionDTO:
    user: str
    password: str


class AccessManagerI:
    _session: sessionDTO
    _message: SessionMessageDTO

    def __init__(self, session: sessionDTO):
        self._session = session

    def signin(self):
        pass

    def login(self):
        pass

    def getMessage(self) -> SessionMessageDTO:
        return self._message


"""Implements AccessManagerI"""
class SimpleAccessManager(AccessManagerI):
    __db: DataAccessI

    def __init__(self, session: sessionDTO):
        self._session = session
        self.__db = UsersDataAccess()

    """Override"""
    def signin(self):
        self.__db.save((self._session.user, self._session.password))
        self.__continue("Signed In")
        

    """Override"""
    def login(self):
        if self.__db.get((self._session.user, self._session.password)):
            self.__continue("Logged In")
        else:
            pass # ERROR
        
        
    def __continue(self, title: str):
        self._message = SessionMessageDTO(title, "Warning! This is sensitive data!", 
                                    self._session.user, self._session.password)
        