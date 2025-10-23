"""This is the main module of the application."""

from classes.SalesRecord import SalesRecord
from classes.Seller import Seller
from classes.ServicesManager import ServicesManager

services_manager = ServicesManager()
sales_record = SalesRecord()


def settings():
    """Function to manage the services offered by the seller."""

    action = (
        input("¿Qué desea hacer? (a)gregar, (r)emover, (m)odificar: ").strip().lower()
    )
    match action:
        case "a":
            services_manager.add_service()
        case "r":
            services_manager.remove_service(
                input("Ingrese el nombre del servicio a remover: ")
            )
        case "m":
            services_manager.mod_service(
                input("Ingrese el nombre del servicio a modificar: "),
                input("Ingrese que caracteristica desea cambiar 'name' o 'price': "),
            )


def main():
    """Main function to run the application."""
    seller = Seller(
        total_price=0.0, services_offered=services_manager, services_sold=[]
    )

    print("Bienvenido a la app 'administrado de ventas'")
    while True:
        print("[(s) para configurar servicios]         [(q) para salir]")
        print("Estos son los servicios que ofrecemos: ")
        for service in services_manager.services_offered:
            print(f"[{service.name}] - ${service.price}")
        print(
            f"List de venta: {', ' .join(service.name for service in seller.services_sold)},"
        )
        for service in seller.services_sold:
            seller.total_price += service.price
        print(f"Total a pagar: [${seller.total_price}]")
        choice = (
            input(
                """
                [Escriba el producto a vender]:    
                """
            )
            .strip()
            .lower()
        )
        if choice == "s":
            settings()
        elif choice in [service.name for service in services_manager.services_offered]:
            seller.add_service(choice)
        # Loop control
        if choice == "q":
            break


if __name__ == "__main__":
    main()
