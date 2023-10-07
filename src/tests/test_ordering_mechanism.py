```python
import unittest
from unittest.mock import patch
from src.ordering_mechanism import fetch_menu, place_order

class TestOrderingMechanism(unittest.TestCase):

    @patch('src.ordering_mechanism.uber_eats_api_key')
    def test_fetch_menu(self, mock_api_key):
        mock_api_key.return_value = 'test_key'
        result = fetch_menu('test_restaurant_id')
        self.assertIsInstance(result, dict)
        self.assertIn('menu', result)

    @patch('src.ordering_mechanism.uber_eats_api_key')
    def test_place_order(self, mock_api_key):
        mock_api_key.return_value = 'test_key'
        test_order = {
            'restaurant_id': 'test_restaurant_id',
            'menu_item_id': 'test_menu_item_id',
            'quantity': 1
        }
        result = place_order(test_order)
        self.assertIsInstance(result, dict)
        self.assertIn('order_id', result)
        self.assertIn('eta', result)

if __name__ == '__main__':
    unittest.main()
```