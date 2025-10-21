"""This module defins the Service class."""


class Service:
    """This class represents a Service.

    Atributes:
        name (str): the name of the service or product.
        price (float): the price of the service or product.

    Methods:
        name() -> str:
            The name of the service or product.
        price() -> float:
            The price of the service or product.
    """

    def __init__(self, name: str, price: float):
        """Initialize the Service class.

        Arguments:
            name (str): the name of the service or product.
            price (float): the price of the service or product.
        """
        self.name = name
        self.price = price
