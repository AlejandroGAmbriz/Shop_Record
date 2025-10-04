"""This module defins the Service class."""


class Service:
    """A class representing a service."""

    def __init__(self, name: str, price: float):
        """Initialize the Service class."""
        self.name = name
        self.price = price

    @property
    def name(self) -> str:
        """The name of the service or product."""
        return self.name

    @name.setter
    def name(self, name: str) -> None:
        self.name = name

    @property
    def price(self) -> float:
        """The price of the service or product."""
        return self.price

    @price.setter
    def price(self, price: float) -> None:
        self.price = price
