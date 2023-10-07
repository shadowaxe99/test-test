```python
import unittest
from unittest.mock import patch
from src.notifications import send_confirmation, send_notification

class TestNotifications(unittest.TestCase):

    @patch('src.notifications.send_email')
    def test_send_confirmation(self, mock_send_email):
        # Arrange
        user_profile = {
            'email': 'test@example.com',
            'name': 'Test User'
        }
        order = {
            'restaurant': 'Test Restaurant',
            'dish': 'Test Dish',
            'price': 10.00
        }

        # Act
        send_confirmation(user_profile, order)

        # Assert
        mock_send_email.assert_called_once_with(
            to=user_profile['email'],
            subject=f'Confirmation: Your order from {order["restaurant"]}',
            body=f'Hi {user_profile["name"]},\n\nYour order for {order["dish"]} from {order["restaurant"]} has been placed. The total cost is ${order["price"]}. Please confirm this order.'
        )

    @patch('src.notifications.send_email')
    def test_send_notification(self, mock_send_email):
        # Arrange
        user_profile = {
            'email': 'test@example.com',
            'name': 'Test User'
        }
        order = {
            'restaurant': 'Test Restaurant',
            'dish': 'Test Dish',
            'price': 10.00,
            'eta': '30 minutes'
        }

        # Act
        send_notification(user_profile, order)

        # Assert
        mock_send_email.assert_called_once_with(
            to=user_profile['email'],
            subject=f'Notification: Your order from {order["restaurant"]}',
            body=f'Hi {user_profile["name"]},\n\nYour order for {order["dish"]} from {order["restaurant"]} has been placed and will arrive in approximately {order["eta"]}. The total cost is ${order["price"]}.'
        )

if __name__ == '__main__':
    unittest.main()
```