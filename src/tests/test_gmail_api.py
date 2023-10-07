```python
import unittest
from unittest.mock import patch
from src.integration.gmail_api import read_gmail_calendar

class TestGmailAPI(unittest.TestCase):

    @patch('src.integration.gmail_api.gmail_api_key')
    def test_read_gmail_calendar(self, mock_gmail_api_key):
        # Mocking the gmail api key
        mock_gmail_api_key.return_value = 'test_key'

        # Test data
        test_data = [
            {
                'summary': 'Lunch meeting with John',
                'start': {'dateTime': '2022-05-01T12:00:00'},
                'end': {'dateTime': '2022-05-01T13:00:00'}
            },
            {
                'summary': 'Dinner with family',
                'start': {'dateTime': '2022-05-01T19:00:00'},
                'end': {'dateTime': '2022-05-01T21:00:00'}
            }
        ]

        # Expected result
        expected_result = [
            {
                'meal': 'lunch',
                'start': '2022-05-01T12:00:00',
                'end': '2022-05-01T13:00:00'
            },
            {
                'meal': 'dinner',
                'start': '2022-05-01T19:00:00',
                'end': '2022-05-01T21:00:00'
            }
        ]

        # Mocking the read_gmail_calendar function
        with patch('src.integration.gmail_api.read_gmail_calendar') as mock_read_gmail_calendar:
            mock_read_gmail_calendar.return_value = test_data

            # Calling the function with the test data
            result = read_gmail_calendar()

            # Asserting that the function returns the expected result
            self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
```