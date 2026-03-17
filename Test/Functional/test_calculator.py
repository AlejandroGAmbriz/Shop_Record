"""_summary_
"""
import unittest.mock
from unittest.mock import Mock

class TestCalculator(unittest.TestCase):
    """
    Test the Calculator functionality of sum an item list
    """
    def setUp(self):
        """
        Sets a list of items with his value and name
        """
        self.MAX_ITEMS = 3
        self.calculator = Mock()
        self.sell_item_list = []

        index = 1
        for index in range(self.MAX_ITEMS):

            item = Mock()
            item.value = index
            item.name = f"item {index}"

            self.sell_item_list.append(item)

    def test_sum(self):
        result =self.calculator.sum(self.sell_item_list)

        self.assertEqual (result, self.MAX_ITEMS)
