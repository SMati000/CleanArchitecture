from dataclasses import dataclass

from useCases.AccessManager import AccessManagerI, SimpleAccessManager, sessionDTO
from useCases.SimpleMessageDTO import SessionMessageDTO

@dataclass()
class Mode:
    """
    Dataclass that stores in which mode the user wants to start (sign in/log in)

    Attributes
    ------------
    - signIn: bool
        If the user wants to sign in, this is true. If the user wants to log in, this is false.
    """
    signIn: bool

class AccessController:
    """
    Checks that username and password entered by the user respect the conventions and arrange the data 
    in an easy way for the use case to read

    Attributes
    ------------
    __session: sessionDTO
        contains the data that the use case needs in an easy to read way for it
    __a
        the use case instance

    Methods
    ---------
    access(mode):
        calls the corresponding function of the use case according to the mode
    """

    __session: sessionDTO
    __a: AccessManagerI

    def __init__(self, username: str, password: str):
        """
        Checks that username and password entered by the user respect the conventions and arrange the data 
        in an easy way for the use case to read

        Parameters
        -----------
        username: str
        password: str
        """
        if username.isalnum() and password.isalnum(): 
            self.__session = sessionDTO(username, password)
            self.__a = SimpleAccessManager(self.__session)
        else:
            pass # ERROR
        

    def access(self, mode: Mode):
        """
        Calls the corresponding function of the use case according to the mode

        Parameters
        -----------
        mode: Mode
        """
        if(mode.signIn):
            self.__a.signin()
        else:
            self.__a.login()

    def getMessage(self) -> SessionMessageDTO:
        return self.__a.getMessage()