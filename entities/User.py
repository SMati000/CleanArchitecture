from entities import Cart, Card


class User:
    __user: str
    __password: str
    __card: list
    __cart: Cart

    def __init__(self, user: str, password: str):
        self.__user = user
        self.__password = password

    def addCard(self, card: Card):
        self.__card.append(card)
        # guardar en la db

    def removeCard(self, card: Card):
        self.__card.remove(card)
        # eliminar de la db

    def getCart(self):
        self.__cart

    def getCard(self, number):
        self.__card[number] # !!!!!!!
