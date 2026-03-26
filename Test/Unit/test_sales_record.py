"""Test the sales record function"""

from datetime import date
import pytest
import pandas as pd
from classes.sales_record import  SalesRecord
from classes.service import Service

class TestSalesRecord ():
    """checks if the file its created"""
    def test_load_sales_record_file(self, tmp_path):
        """Test if exist a usable file"""
        sales_record = SalesRecord()

        sales_record.file_path = tmp_path / "Test_load_sales"

        sales_record.load_sales_record_file()

        assert sales_record.file_path.exists()

    def test_registrer_sale(self, tmp_path):
        """cheks if the input its registred in the file"""

        sales_record = SalesRecord()
        sales_record.file_path = tmp_path / "Test_load_sales"

        sales_record.load_sales_record_file()

        service = Service("Corte de cabello", 150)

        sales_record.register_sale([service])

        df = pd.read_excel(sales_record.file_path)

        assert len(df) == 1
        assert df.iloc[0]["Servicio"] == "Corte de cabello"
        assert df.iloc[0]["Precio"] == 150
        assert df.iloc[0]["Fecha"] == date.today().strftime("%y-%m-%d")
