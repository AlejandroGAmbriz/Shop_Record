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

    @property
    def name(self) -> str:
        """The name of the service or product.
        
        Arguments:
            name (str): the name of the service or product.
            
        Returns:
            str: the name of the service or product.
        """
        return self.name

    @name.setter
    def name(self, name: str) -> None:
        self.name = name

    @property
    def price(self) -> float:
        """The price of the service or product.
        
        Arguments:
            price (float): the price of the service or product.
            
        Returns:
            float: the price of the service or product."""
        return self.price

    @price.setter
    def price(self, price: float) -> None:
        self.price = price
