from dataclasses import dataclass


@dataclass(frozen=True)
class SimpleMessageDTO():
    """
    Contains a generic message to show to the user. This is made for the presenter to read it easily.
    """

    title: str
    message: str

    def __str__(self) -> str:
        self.title + "\n" + self.message

@dataclass(frozen=True)
class SessionMessageDTO(SimpleMessageDTO):
    """
    Contains all the data of the session that will be shown to the user. This is made for the presenter to read it easily.
    """

    user: str
    password: str

    def __str__(self) -> str:
        self.title + "\n" + self.message
