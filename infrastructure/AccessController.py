from dataclasses import dataclass

from useCases.AccessManager import AccessManagerI, SimpleAccessManager, sessionDTO
from useCases.SimpleMessageDTO import SessionMessageDTO

@dataclass()
class Mode:
    signIn: bool

class AccessController:
    __session: sessionDTO
    __a: AccessManagerI

    def __init__(self, username: str, password: str):
        if username.isalnum() and password.isalnum(): 
            self.__session = sessionDTO(username, password)
            self.__a = SimpleAccessManager(self.__session)
        else:
            pass # ERROR
        

    def access(self, mode: Mode):
        if(mode.signIn):
            self.__a.signin()
        else:
            self.__a.login()

    def getMessage(self) -> SessionMessageDTO:
        return self.__a.getMessage()