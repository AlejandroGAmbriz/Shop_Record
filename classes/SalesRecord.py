"""This module defins the SalesRecord class."""

from datetime import date
import os
import pandas as pd


class SalesRecord:
    """A class representing an SalesRecord
    It will be in charg of manage the excel files
    
    Atributes:
        file_path (str): the path of the excel file where the sales are recorded.
    
    Methods:
        load_sale(totlal: float, services_sold: list, services_offered: list) -> None:
            load the sales in an excel file.
        box_cut(services_offered: list) -> None:
            creat a new excel file and save the new excel path.
        show_daily_sales() -> None:
            Shows the daily sales in an excel file.
        """
    def __init__(self, file_path: str = None):
        """Initialize the Interface class.
        
        Arguments:
            file_path (str): the path of the excel file where the sales are recorded.
        """
        self.file_path = file_path

    def load_sale(self, totlal: float, services_sold: list, services_offered: list) -> None:
        """Load the sales in an excel file.
            load a new row in the excel file with the date and time,
            the services sold and the total amount of the sale.
            
        Arguments:
            total (float): the total amount of the sale.
            services_sold (list): list of services sold in the sale.
            services_offered (list): list of services offered by the seller.
        
        Exceptions:
            FileNotFoundError: if the excel file does not exist.
        """
        try:
            df = pd.read_excel(self.file_path)
            new_row = {col: None for col in df.columns}
            new_row["Feche y Hora"] = pd.Timestamp.now().strftime("%Y-%m-%d %H:%M:%S")
            for service in services_offered:
                if service in services_sold:
                    new_row[service] = service.price
                else:
                    new_row[service] = 0.0
            new_row["Total"] = totlal
            df = df.append(new_row, ignore_index=True)
            df.to_excel(self.file_path, index=False)
        except FileNotFoundError:
            print("No se ha encontrado el archivo:", self.file_path)

    def box_cut(self, services_offered: list) -> None:
        """Create a new excel file with the columns:
            Date and Time, services offered and Total.
            Save the new excel path in the file_path attribute.
        
        Arguments:
            services_offered (list): list of services offered by the seller.
        """
        columns = ["Feche y Hora"] + services_offered + ["Total"]
        df = pd.DataFrame(columns=columns)
        self.file_path = f"Ventas del día{date.today().strftime('%Y-%m-%d')}.xlsx"
        df.to_excel(self.file_path, index=False)

    def show_daily_sales(self) -> None:
        """Shows the daily sales in an excel file.
        """
        if os.path.exists(self.file_path):
            os.startfile(self.file_path)
        else:
            print("No existe el archivo:", self.file_path)
