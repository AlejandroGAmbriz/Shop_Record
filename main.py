"""This is the main module of the application."""

from classes.SalesRecord import SalesRecord
from classes.Seller import Seller
from classes.Service import Service
from classes.ServicesManager import ServicesManager

services_manager = ServicesManager()

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
                input("Ingrese el nuevo nombre o precio del servicio: "),
            )

def main():
    """Main function to run the application."""

    print("Bienvenido a la app 'administrado de ventas'")
    while True:
        print("Estos son los servicios que ofrecemos: ")
        for service in services_manager.services_offered:
            print(service)
        choice = (
            input(
                "Elija el producto a vender o escriba (s)ettings para administrar los servicios ofrecidos: "
            )
            .strip()
            .lower()
        )
        if choice == "s":
            settings()
        is_continue = input("¿Desea continuar? (s/n): ").strip().lower()
        if is_continue == "n":
            break


if __name__ == "__main__":
    main()



