"""
Service Manager Modul
Gves a class to manage the interactio of system with the DB services
"""
import os
import sqlite3
from classes.service import Service

class ServicesManager:
    """
    This class is in charge of managing the db service's CRUD.
    
    """
    def __init__(self):
        """
        Initialize the ServicesManager class.
        
        This constructor establishes a connection to the SQLite database
        located in the DB folder
        
        Arguments:
            _services_offered (list): list of services offered by the seller.
        """

        db_path = os.path.join(".", "DB", "services.db")
        self.conn_db_services  =  sqlite3.connect(db_path)
        self.cursor_db_services  = self.conn_db_services .cursor()

        self._create_services_db()

        self._services_offered = self.load_services()

    def _create_services_db(self) -> None:
        """Create the service DB if it not exist"""

        self.cursor_db_services.execute("""
            CREATE TABLE IF NOT EXISTS services(
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL
                )
                                    """)
        self.conn_db_services.commit()

    def load_services(self) -> list[Service]:
        """
        Load the DB service to retun a list of Service instance
        """
        self.cursor_db_services.execute("SELECT name, price FROM  services")
        rows = self.cursor_db_services.fetchall()

        return [Service(name, price) for name, price in rows]

    @property
    def services_offered(self) -> list[Service]:
        """Get the services_offered list."""
        return self._services_offered

    def add_service(self, new_servicie_name: str, new_service_price: int) -> None:
        """Add a service to the services_offered list."""
        self.conn_db_services.execute("INSERT INTO services (name, price) VALUES (?,?)",
                                      (new_servicie_name, new_service_price))
        self.conn_db_services.commit()

        self._services_offered = self.load_services()

    def remove_service(self, service: Service) -> None:
        """Remove a service from the services_offered list."""
        self.cursor_db_services.execute("DELETE FROM services WHERE name = ?",
                                        (service.name,))
        self.conn_db_services.commit()

        self._services_offered = self.load_services()


    def mod_service(self, service: Service, to_change: str) -> None:
        """Modify a service from the services_offered list.
        it could be the name or the price of the service."""
        if to_change == "name":
            new_name = input("Agregue el nuevo nombre del servicio o producto: ")

            self.cursor_db_services.execute("UPDATE services SET name =? WHERE name = ?",
                                            (new_name, service.name))
            self.conn_db_services.commit()

        elif to_change == "price":
            new_price = float(input("Agregue el nuevo precio del servicio o producto: "))

            self.cursor_db_services.execute("UPDATE services SET price= ? WHERE name = ?",
                                            (new_price, service.name))
            self.conn_db_services.commit()

        self._services_offered = self.load_services()
