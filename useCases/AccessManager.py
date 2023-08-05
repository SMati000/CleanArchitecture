from dataclasses import dataclass

from entities import User
from useCases.SimpleMessageDTO import SessionMessageDTO
from infrastructure.DataAccessI import DataAccessI

@dataclass(frozen=True)
class sessionDTO:
    """
    Contains the data of the session to be loaded. Ready to be read by the use case
    """
    user: str
    password: str

    def __init__(self, user: str, pswd: str):
        if user.isalnum() and pswd.isalnum():
            object.__setattr__(self, 'user', user)
            object.__setattr__(self, 'password', pswd)
        else:
            raise Exception("Username and password must be alphanumeric")


class AccessManagerI:
    """
    Interface of the access manager.

    Attributes
    -----------
    _dbPersister: DataAccessI
        instance of DataAccessI to have access to the database
    _message
        The message to be returned so that it can be passed on to the presenter and then showed to the user

    Methods
    --------
    signin():
        method that should save the session data to the database, and then sign in
    login():
        method that should check that the session is actually saved in the database and if so, log in
    """
    _dbPersister: DataAccessI
    _message: SessionMessageDTO

    def __init__(self, dbPersister: DataAccessI):
        """initializes the session instance to be loaded"""
        self._dbPersister = dbPersister

    def signin(self, session: sessionDTO):
        """should save the session data to the database, and then sign in"""
        pass

    def login(self, session: sessionDTO):
        """should check that the session is actually saved in the database and if so, log in"""
        pass

    def getMessage(self) -> SessionMessageDTO:
        """returns _message"""
        return self._message


class SimpleAccessManager(AccessManagerI):
    """Implements AccessManagerI"""

    # Override
    def signin(self, session: sessionDTO):
        self._dbPersister.save((session.user, session.password))
        self.__continue("Signed In", session)
        

    # Override
    def login(self, session: sessionDTO):
        if self._dbPersister.exists((session.user, )):
            self.__continue("Logged In", session)
        else:
            pass # ERROR
        
        
    def __continue(self, title: str, session: sessionDTO):
        # After database is checked, this method is internally called to generate the message
        self._message = SessionMessageDTO(title, "Warning! This is sensitive data!", 
                                    session.user, session.password)
        