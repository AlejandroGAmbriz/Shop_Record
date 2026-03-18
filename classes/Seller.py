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
    through the workflow steps.
    """

    def __init__(self):
        """Initialize the Seller class.

        Arguments:
            services_sold (list): list of services in a sale.
            total (float): total amount of the sale.
            services_manager (ServicesManager): instance of ServicesManager class.
        """
        #TODO: services_sold y total_price cuold be part of the calculator, chek it.
        self.services_sold = []
        self.total_price = 0.0
        self.services_manager = ServicesManager()

    def show_services_offered(self) -> None:
        """
        Shows the services offered
        """
        for service in self.services_manager.services_offered:

            print(service.name)

    def settings_loop(self) -> None:
        """
        Manage the settings loop for change on the offered services list
        """
        settings_option =""
        while settings_option != "quit":

            settings_option = input("Escriba la funcion que desee realizar: ")

            if settings_option == "Add":

                new_service_name = input("Agregue el nombre del servicio o producto: ")
                new_service_price = float(input("Agregue el precio del servicio o producto: "))

                if new_service_name not in self.services_manager.services_offered:
                    self.services_manager.add_service(new_service_name, new_service_price)
                else:
                    print("El servicio o producto ya existe")

            elif settings_option == "Remove":

                service_name = input("Escriba el servicio a remover: ")

                for service in self.services_manager.services_offered:
                    if service_name == service.name:
                        self.services_manager.remove_service(service)
                        break
                else:
                    print("El servicio no se encuentra en la lista.")

            elif settings_option == "Mod":

                service_name = input("Escriba el servicio a remover: ")
                to_change = input("Escriba la caracteristica a cambiar: ")

                for service in self.services_manager.services_offered:
                    if service_name == service.name:
                        self.services_manager.mod_service(service, to_change)
                        break

                else:
                    print("El servicio no se encuentra en la lista.")

    def system_loop (self) -> None:
        """
        Manage the System Loop
        """

        while True:

            self.show_services_offered()
            option = input("Seleccione el producto a vender: ")

            if option == "quit":
                break

            elif option == "settings":

                self.settings_loop()
