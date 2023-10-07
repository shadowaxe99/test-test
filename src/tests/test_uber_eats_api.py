```python
import unittest
from unittest.mock import patch
from src.integration.uber_eats_api import fetch_menu, place_order

class TestUberEatsAPI(unittest.TestCase):

    @patch('src.integration.uber_eats_api.requests.get')
    def test_fetch_menu(self, mock_get):
        # Mocking the response from Uber Eats API
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {
            "menu": [
                {"dish": "Pizza", "price": 10},
                {"dish": "Burger", "price": 8}
            ]
        }

        response = fetch_menu("Italian")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()["menu"]), 2)

    @patch('src.integration.uber_eats_api.requests.post')
    def test_place_order(self, mock_post):
        # Mocking the response from Uber Eats API
        mock_post.return_value.status_code = 200
        mock_post.return_value.json.return_value = {
            "order_id": "12345",
            "status": "Placed",
            "eta": "30 minutes"
        }

        order = {
            "user_id": "user1",
            "dish": "Pizza",
            "quantity": 1,
            "address": "123 Street, City, Country"
        }

        response = place_order(order)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "Placed")

if __name__ == '__main__':
    unittest.main()
```