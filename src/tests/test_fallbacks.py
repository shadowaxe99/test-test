```python
import unittest
from unittest.mock import patch
from src.fallbacks import pick_alternative

class TestFallbacks(unittest.TestCase):

    @patch('src.fallbacks.pick_alternative')
    def test_pick_alternative(self, mock_pick_alternative):
        # Mock user profile and unavailable dish
        user_profile = {
            'preferences': ['Italian', 'Mexican'],
            'allergies': ['Nuts'],
            'past_orders': ['Pizza', 'Tacos']
        }
        unavailable_dish = 'Pizza'

        # Call the function with the mock data
        result = pick_alternative(user_profile, unavailable_dish)

        # Assert that the function was called with the correct arguments
        mock_pick_alternative.assert_called_with(user_profile, unavailable_dish)

        # Assert that the function returned a dish that is not the unavailable dish
        self.assertNotEqual(result, unavailable_dish)

        # Assert that the function returned a dish that is in the user's past orders
        self.assertIn(result, user_profile['past_orders'])

if __name__ == '__main__':
    unittest.main()
```