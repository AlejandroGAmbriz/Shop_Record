"""Test for the ServiceManager class"""

import sqlite3
import pytest
from classes.services_manager import ServicesManager
from classes.service import Service

class TestServiceManager:
    """Test the ServiceManager's fucntions"""

    @pytest.fixture
    def fixture_service_manager(self):
        """Mock the DB services with a non persisten DB"""
        service_manager = ServicesManager()
        service_manager.conn_db_services = sqlite3.connect(":memory:")
        service_manager.cursor_db_services = service_manager.conn_db_services.cursor()
        service_manager._create_services_db()

        return service_manager


    def test_add_service(self, fixture_service_manager):
        """Test the add service function for the DB"""

        fixture_service_manager.add_service("Corte de cabello", 100)
        service_list = fixture_service_manager.services_offered

        assert len(service_list) == 1
        assert service_list[0].name == "Corte de cabello"
        assert service_list[0].price == 100


    def test_remove_service(self, fixture_service_manager):
        """Test the remove service function for the DB"""

        fixture_service_manager.add_service("Corte de cabello", 100)
        service = fixture_service_manager.services_offered[0]

        fixture_service_manager.remove_service(service)

        assert len(fixture_service_manager.services_offered) == 0


    def test_mod_service_name(self, fixture_service_manager, fake_input):
        """Test the mod of the service name for the DB"""

        fixture_service_manager.add_service("Corte de cabello", 100)
        service = fixture_service_manager.services_offered[0]

        fake_input("Corte basico")
        fixture_service_manager.mod_service(service, "name")
        service = fixture_service_manager.services_offered[0]

        assert service.name == "Corte basico"


    def test_mod_service_price(self, fixture_service_manager, fake_input):
        """Test the mod of the service price for the DB"""

        fixture_service_manager.add_service("Corte de cabello", 100)
        service = fixture_service_manager.services_offered[0]

        fake_input(50)
        fixture_service_manager.mod_service(service, "price")
        service = fixture_service_manager.services_offered[0]

        assert service.price == 50
