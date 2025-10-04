"""This module defins the Interface class."""

from datetime import date
import pandas as pd


class Interface:
    """A class representing an interface."""

    def __init__(self, services_offered: list, services_sold: list, total: float = 0):
        """Initialize the Interface class."""
        self.services_offered = services_offered
        self.total = total
        self.services_sold = services_sold
    
    @property
    def services_offered(self) -> list:
        """The services offered by the interface."""
        return [service.name for service in self.services_offered]

    def load_sale(self, file_path: str, totlal: float) -> None:
        """Load the sales in an excel file."""
        

    def box_cut(self) -> None:
        """creat a new excel file."""
        columns = {
            ["Feche y Hora"] +
            self.services_offered +
            ["Total"]
        }
        df = pd.DataFrame(columns = columns)
        df.to_excel(f"Ventas del día{date.today().strftime('%Y-%m-%d')}.xlsx")

    def get_daily_sales(self) -> None:
        """Shows the daily sales in an excel file."""

    def total_price(self, total: float) -> float:
        """Calculate the total price of the salses."""
        for service in self.services_sold:
            total += service.price
        return total
