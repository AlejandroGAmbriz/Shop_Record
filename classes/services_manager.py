"""
Service Manager Modul
Gves a class to manage the interactio of services with the sistem
"""

from classes.service import Service


class ServicesManager:
    """
    This class is in charge of managing the service's CRUD.
    
    """
    def __init__(self, _services_offered: list[Service] = None):
        """Initialize the ServicesManager class.

        Arguments:
            _services_offered (list): list of services offered by the seller.
        """
        if _services_offered is None:
            self._services_offered = []
        else:
            self._services_offered = _services_offered

    @property
    def services_offered(self) -> list[Service]:
        """Get the services_offered list."""
        return self._services_offered

    @services_offered.setter
    def services_offered(self, services_offered: list[Service]) -> None:
        """Set the services_offered list."""
        self._services_offered.extend(services_offered)

    def add_service(self) -> None:
        """Add a service to the services_offered list."""
        input_name = input("Agregue el nombre del servicio o producto: ")
        input_price = float(input("Agregue el precio del servicio o producto: "))

        service = Service(input_name, input_price)

        if service not in self.services_offered:
            self.services_offered.append(service)
        else:
            print("El servicio o producto ya existe")

    def remove_service(self, name_service: str) -> None:
        """Remove a service from the services_offered list."""
        for service in self.services_offered:
            if service.name == name_service:
                self.services_offered.remove(service)
                break
            else:
                print("El servicio o producto no existe")

    def mod_service(self, name_service: str, to_change: str) -> None:
        """Modify a service from the services_offered list.
        it could be the name or the price of the service."""
        if name_service not in self._services_offered:

            for service in self.services_offered:
                if service.name == name_service:
                    if to_change == "name":

                        new_name = input(
                            "Agregue el nuevo nombre del servicio o producto: "
                        )
                        service.name = new_name

                    elif to_change == "price":

                        new_price = float(
                            input("Agregue el nuevo precio del servicio o producto: ")
                        )
                        service.price = new_price

        else:
            print("El servicio o producto no existe")
