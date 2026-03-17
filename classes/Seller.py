"""
Seller module
Gives classes for manage the flow of the system
"""

from classes.services_manager import ServicesManager
from classes.service import Service

class Seller:
    """
    Manage the flow system to interact with the user.

    This class handles user interactions, directing requests
    through the appropriate workflow steps.
    """

    def __init__(self):
        """Initialize the Seller class.

        Arguments:
            services_sold (list): list of services in a sale.
            total (float): total amount of the sale.
            services_manager (ServicesManager): instance of ServicesManager class.
        """
        self.services_sold = []
        self.total_price = 0.0
        self.services_manager = ServicesManager()
    def show_services_offered(self):
        """
        Shows the services offered
        """
        for service in self.services_manager.services_offered:

            print(service.name)

    def system_loop (self):
        """
        Manage the System Loop
        """

        while True:

            self.show_services_offered()
            option = input("Seleccione el producto a vender")

            if option == "quit":
                break
