"""This module defins the ServicesManager class that inherits from Service."""

from classes.Service import Service


class ServicesManager():
    """This class is in charge of managing the services offered by the seller.
    
    Atributes:
        services_offered (list): list of services offered by the seller.
    
    Methods:
        add_service() -> None:
            Add a service to the services_offered list.
        remove_service(name_service: str) -> None:
            Remove a service from the services_offered list.
        mod_service(name_service: str, to_change: str) -> None:
            Modify a service from the services_offered list."""

    def __init__(self, services_offered: list[Service]):
        """Initialize the ServicesManager class.
        
        Arguments:
            services_offered (list): list of services offered by the seller.
        """
        self.services_offered = services_offered

    def add_service(self) -> None:
        """Add a service to the services_offered list.
        """
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
