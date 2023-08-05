from dataclasses import dataclass

from useCases.AccessManager import AccessManagerI, sessionDTO
from useCases.SimpleMessageDTO import SessionMessageDTO

from dependency_injector.wiring import inject, Provide

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
    __a
        the use case instance

    Methods
    ---------
    access(mode):
        calls the corresponding function of the use case according to the mode
    """

    __a: AccessManagerI

    @inject
    def __init__(self, a: AccessManagerI = Provide["accessManager_factory"]):
        """
        initializes the AccessManager

        Parameters
        -----------
        a: AccessManagerI
        """
        self.__a = a

    def access(self, mode: Mode, user: str, password: str):
        """
        Calls the corresponding function of the use case according to the mode

        Parameters
        -----------
        mode: Mode
        user: str
        password: str
        """
        session = sessionDTO(user, password)

        if(mode.signIn):
            self.__a.signin(session)
        else:
            self.__a.login(session)

    def getMessage(self) -> SessionMessageDTO:
        return self.__a.getMessage()