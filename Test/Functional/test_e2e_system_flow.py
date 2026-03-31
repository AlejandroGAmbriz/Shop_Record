"""Tests e2e for the system flow"""

from datetime import date
import pytest
import pandas as pd
from openpyxl import Workbook
from classes.seller import Seller


@pytest.fixture
def seller_mock(tmp_path, fixture_service_manager):
    """Config a mock seller for the Test"""
    seller = Seller()

    seller.services_manager = fixture_service_manager

    seller.services_manager.add_service("Corte de cabello", 100)
    seller.services_manager.add_service("Manicure", 50)

    mock_file_path = tmp_path / "Test_load_sales.xlsx"
    wb = Workbook()
    wb.save(mock_file_path)

    seller.sales_record.file_path = mock_file_path

    return seller


class TestE2ESystemFlow:
    """Test e2e for the system flow"""

    def test_e2e_sale_flow(self, fake_input, capsys, seller_mock):
        """Test the flow of the system to record a sell"""
        user_inputs = ["Corte de cabello", "Sales report", "add sell", "quit", "quit"]

        fake_input(user_inputs)
        seller_mock.system_loop()

        df = pd.read_excel(seller_mock.sales_record.file_path, engine="openpyxl")

        captured = capsys.readouterr()
        output = captured.out

        assert "Corte de cabello" in output
        assert "Total: $100.0" in output
        assert len(df) == 1
        assert df.iloc[0]["Servicio"] == "Corte de cabello"
        assert df.iloc[0]["Precio"] == 100
        assert df.iloc[0]["Fecha"] == date.today().strftime("%y-%m-%d")

    def test_e2e_remove_sale_flow(self, fake_input, seller_mock):
        """Test the flow of the system to remove a service from the sold list"""
        user_inputs = [
            "Corte de cabello",
            "Manicure",
            "remove",
            "Manicure",
            "Sales report",
            "add sell",
            "quit",
            "quit",
        ]

        fake_input(user_inputs)
        seller_mock.system_loop()

        df = pd.read_excel(seller_mock.sales_record.file_path, engine="openpyxl")

        assert len(df) == 1
        assert df.iloc[0]["Servicio"] == "Corte de cabello"
        assert df.iloc[0]["Precio"] == 100
        assert df.iloc[0]["Fecha"] == date.today().strftime("%y-%m-%d")

    def test_e2e_add_service(self, fake_input, seller_mock, capsys):
        """Test for the system loop to add a service"""
        user_inputs = ["settings", "Add", "Perfilado", 50, "quit", "quit"]
        name_service_list = []

        fake_input(user_inputs)

        seller_mock.system_loop()

        services_list = seller_mock.services_manager.services_offered
        for service in services_list:
            name_service_list.append(service.name)

        captured = capsys.readouterr()
        ouutput = captured.out

        assert "Perfilado" in ouutput
        assert len(services_list) == 3
        assert services_list[2].name == "Perfilado"
        assert services_list[2].price == 50

    def test_e2e_remove_service(self, fake_input, seller_mock):
        """Test for the system loop to remove a service"""
        user_inputs = ["settings", "Remove", "Manicure", "quit", "quit"]
        name_service_list = []

        fake_input(user_inputs)

        seller_mock.system_loop()

        services_list = seller_mock.services_manager.services_offered
        for service in services_list:
            name_service_list.append(service.name)

        assert len(services_list) == 1
        assert "Manicure" not in name_service_list

    def test_e2e_mod_service_name(self, fake_input, capsys, seller_mock):
        """Test for the system loop to modify the name of a service"""
        user_inputs = [
            "settings",
            "Mod",
            "Manicure",
            "name",
            "Pedicure",
            "quit",
            "quit",
        ]
        name_sercvie_list = []

        fake_input(user_inputs)

        seller_mock.system_loop()

        service_list = seller_mock.services_manager.services_offered
        for service in service_list:
            name_sercvie_list.append(service.name)

        captured = capsys.readouterr()
        output = captured.out

        assert "Pedicure" in output
        assert "Pedicure" in name_sercvie_list
        assert "Manicure" not in name_sercvie_list

    def test_e2e_mod_service_price(self, fake_input, seller_mock):
        """Test for the system loop to modify the price of a service"""
        user_inputs = ["settings", "Mod", "Manicure", "price", 100, "quit", "quit"]
        new_service_price = 0

        fake_input(user_inputs)

        seller_mock.system_loop()

        service_list = seller_mock.services_manager.services_offered
        for service in service_list:
            if service.name == "Manicure":
                new_service_price = service.price

        assert new_service_price == 100
