from entities import Cart, Card


class User:
    """
    Represents the user entity, for a shopping app.

    Attributes
    ------------
    __user: str
    __password: str
    __card: list
        the user's payment cards
    __cart: Cart
        the user's cart of products
    
    Methods
    ----------
    addCard(card):
        Adds the card to the __card list
    removeCard(card):
        Removes the card from the __card list
    """
    
    __user: str
    __password: str
    __card: list
    __cart: Cart

    def __init__(self, user: str, password: str):
        self.__user = user
        self.__password = password

    def addCard(self, card: Card):
        """
        Adds the card to the __card list

        Parameters
        ------------
        card: Card
            card to be added to the user
        """
        self.__card.append(card)


    def removeCard(self, card: Card):
        """
        Removes the card from the __card list

        Parameters
        ------------
        card: Card
            card to be removed from the user
        """
        self.__card.remove(card)


    def getCart(self) -> Cart:
        return self.__cart

    def getCard(self, number) -> Card:
        return self.__card[number] # !!!!!!!
