"""Test the calculator Function"""
import pytest
from classes.service import Service
from classes.calculator import Calculator

class TestCalculator():
    """Test the Calculator class functions""" 

    @pytest.fixture
    def sold_list(self):
        """Gives a list of sold services"""
        return [
            Service("Fade", 50),
            Service("Barba", 100)
        ]

    @pytest.fixture
    def calc(self, sold_list):
        """Instance of Calculator class"""
        calc = Calculator()

        calc.sold_services = sold_list
        return calc

    def test_add_service_sold(self, sold_list, calc):
        """Test the Calculator add service function"""
        calc.add_service_sold(Service("Mascarilla", 100))

        assert sold_list[2].name == "Mascarilla"
        assert sold_list[2].price == 100

    def test_remove_service_sold(self, sold_list, calc):
        """Test the Calculator remove service function"""
        calc.remove_service_sold(sold_list[1])

        assert len(sold_list) == 1
        assert sold_list[0].name == "Fade"

    def test_total_sum(self, calc):
        """Test the Calculator total sum service function"""
        assert calc.total_sum() == 150
