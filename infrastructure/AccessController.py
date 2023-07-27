from dataclasses import dataclass

from useCases.AccessManager import AccessManagerI, sessionDTO
from useCases.SimpleMessageDTO import SessionMessageDTO

from dependency_injector.wiring import inject

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
    @staticmethod
    getSession(username, passoword) -> sessionDTO:
        checks the username and password are valid and returns a sessionDTO
    access(mode):
        calls the corresponding function of the use case according to the mode
    """

    __a: AccessManagerI

    @inject
    def __init__(self, a: AccessManagerI):
        """
        initializes the AccessManager

        Parameters
        -----------
        a: AccessManagerI
        """
        self.__a = a

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