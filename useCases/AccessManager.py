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


class AccessManagerI:
    """
    Interface of the access manager.

    Attributes
    -----------
    _dbPersister: DataAccessI
        instance of DataAccessI to have access to the database
    _session: sessionDTO
        Data of the session to be loaded
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
    _session: sessionDTO
    _message: SessionMessageDTO

    def __init__(self, dbPersister: DataAccessI, session: sessionDTO):
        """initializes the session instance to be loaded"""
        self._dbPersister = dbPersister
        self._session = session

    def signin(self):
        """should save the session data to the database, and then sign in"""
        pass

    def login(self):
        """should check that the session is actually saved in the database and if so, log in"""
        pass

    def getMessage(self) -> SessionMessageDTO:
        """returns _message"""
        return self._message


class SimpleAccessManager(AccessManagerI):
    """Implements AccessManagerI"""

    # Override
    def signin(self):
        self._dbPersister.save((self._session.user, self._session.password))
        self.__continue("Signed In")
        

    # Override
    def login(self):
        if self._dbPersister.exists((self._session.user, )):
            self.__continue("Logged In")
        else:
            pass # ERROR
        
        
    def __continue(self, title: str):
        # After database is checked, this method is internally called to generate the message
        self._message = SessionMessageDTO(title, "Warning! This is sensitive data!", 
                                    self._session.user, self._session.password)
        