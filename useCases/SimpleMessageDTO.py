from dataclasses import dataclass


@dataclass(frozen=True)
class SimpleMessageDTO():
    title: str
    message: str

    def __str__(self) -> str:
        self.title + "\n" + self.message

@dataclass(frozen=True)
class SessionMessageDTO(SimpleMessageDTO):
    user: str
    password: str

    def __str__(self) -> str:
        self.title + "\n" + self.message
