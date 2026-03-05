"""This module defins the Seller class."""

from classes.ServicesManager import ServicesManager

service_manager = ServicesManager()


class Seller:
    """This class is responsible for managing the information of a sale,
    such as the list of services sold and the total.

    Attributes:
        services_sold (list): list of services in a sale.
        total (float): total amount of the sale.
        services_offered (ServicesManager): instance of ServicesManager class.

    Methods:
        add_service: Adds a service to the services_sold list.
        remove_service: Removes a service from the services_sold list.
        calculate_total: Calculates the total amount of the sale.
    """

    def __init__(
        self, services_offered: list, services_sold: list, total_price: float = 0.0
    ):
        """Initialize the Seller class.

        Arguments:
            services_sold (list): list of services in a sale.
            total (float): total amount of the sale.
            services_offered (ServicesManager): instance of ServicesManager class.
        """
        self.services_sold = services_sold
        self.total_price = total_price
        self.services_offered = services_offered

    def add_service(self, service_added: str) -> None:
        """Adds a service to the services_sold list

        Arguments:
            service_added (str): name of the service to be added.

        Exeptions:
            ValueError: If the service is not found in the services_sold list.
        """

        for service in service_manager.services_offered:
            if service.name.strip().lower() == service_added:
                self.services_sold.append(service)
                break
        else:
            raise ValueError("El servicio o producto no existe")

    def remove_service(self, service_removed: str) -> None:
        """Removes a service from the services_sold list.

        Arguments:
            service_removed (str): name of the service to be removed.

        Exeptions:
            ValueError: If the service is not found in the services_sold list."""
        for service in self.services_sold:
            if service.name == service_removed:
                self.services_sold.remove(service)
                break
            else:
                raise ValueError(
                    "El servicio o producto no se encuentra en la lista de venta"
                )

    def calculate_total(self) -> float:
        """Calculates the toatl amoun of the sale.

        returns:
            float: total amount of the sale.
        """
        for service in self.services_sold:
            self.total_price += service.price
        return self.total_price
