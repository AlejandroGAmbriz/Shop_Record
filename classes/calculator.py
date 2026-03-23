"""Module fot the managment of the calculator
"""
from classes.service import Service

class Calculator:
    """Manage the logic to make operations with the sold service list
    """

    def __init__(self):
        """
        Initialize the Calculator class.
    
        Arguments:
            sold_services (List[Service]): List of the services sold.
        """
        self.sold_services = []

    def add_service_sold(self, service:Service) ->None:
        """Add a service to the sold services lits"""
        self.sold_services.append(service)

    def remove_service_sold(self, service: Service) ->None:
        """Remove a service to the sold services list"""
        self.sold_services.remove(service)

    def total_sum(self) -> int:
        """Gives the total amount of the"service list"""
        total_amount = 0

        for service in self.sold_services:
            total_amount += service.price

        return total_amount
