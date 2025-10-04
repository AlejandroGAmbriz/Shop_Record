"""This module defins the Settings class how inheritance from Interface class."""
from classes.Service import Service
from classes.Interface import Interface



class Settings(Interface):
    """A class representing the settings of the application."""

    def __init__(self):
        """Initialize the Settings class."""
        super().__init__(services_offered=[], services_sold=[])
        super().total_price(total=0)

    def add_service(self) -> None:
        """Add a service to the intreface."""
        input_name = input("Agregue el nombre del servicio o producto: ")
        input_price = float(input("Agregue el precio del servicio o producto: "))
        service = Service(input_name, input_price)
        if service not in self.services_offered:
            self.services_offered.append(service)
        else:
            print("El servicio o producto ya existe")

    def remove_service(self, name_service: str) -> None:
        """Remove a service from the interface."""
        for service in self.services_offered:
            if service.name == name_service:
                self.services_offered.remove(service)
                break
            else:
                print("El servicio o producto no existe")

    def mod_service(self, name_service: str, to_change:str) -> None:
        """Modify a service from the interface."""
        for service in self.services_offered:
            if service.name == name_service:
                if to_change == "name":
                    new_name = input("Agregue el nuevo nombre del servicio o producto: ")
                    service.name = new_name
                elif to_change == "price":
                    new_price = float(input("Agregue el nuevo precio del servicio o producto: "))
                    service.price = new_price
