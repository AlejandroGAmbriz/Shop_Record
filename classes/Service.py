"""
Service module
Gives classes for manage the Services Logic
"""


class Service:
    """
    This class represents a Service.
    The service must have name and price
    """

    def __init__(self, name: str, price: float):
        """Initialize the Service class.

        Arguments:
            name (str): the name of the service or product.
            price (float): the price of the service or product.
        """
        self.name = name
        self.price = price
