"""This module defins the SalesRecord class."""

from datetime import date, datetime
import os
import pandas as pd

from classes.service import Service
from classes.constants import COLUMNS


class SalesRecord:
    """
    It will be in charg of manage the excel files, how contain the sales record
    """

    def __init__(self):
        """Initialize the Interface class.

        Arguments:
            file_path (str): the path of the excel file where the sales are recorded.
        """

        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

        db_dir = os.path.join(base_dir, "DB")
        file_name = f"slaes_record_{date.today().strftime('%y-%m-%d')}.xlsx"

        self.file_path = os.path.join(db_dir, file_name)
        self.load_sales_record_file()

    def _create_sales_record_file(self) -> None:
        """Create the excel file"""

        df = pd.DataFrame(columns=COLUMNS)
        df.to_excel(self.file_path, index=False)

        print(f"Archivo creado en: {self.file_path}")

    def load_sales_record_file(self) -> None:
        """Loath the Excel file path"""
        if not os.path.exists(self.file_path):
            self._create_sales_record_file()

    def show_daily_sales(self) -> None:
        """Shows the daily sales in an excel file."""
        os.startfile(self.file_path)

    def register_sale(self, sold_services: list[Service]):
        """Adds the sales to the record"""
        for service in sold_services:
            sales_values = [
                date.today().strftime("%y-%m-%d"),
                datetime.now().strftime("%H:%M"),
                service.name,
                service.price,
            ]

            new_entry = dict(zip(COLUMNS, sales_values))

            df = pd.read_excel(self.file_path)
            df = pd.concat([df, pd.DataFrame([new_entry])], ignore_index=True)

            df.to_excel(self.file_path, index=False)

        print("Venta agregada")
