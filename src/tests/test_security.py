```python
import unittest
from unittest.mock import patch
from src.security import OAuthHandler

class TestSecurity(unittest.TestCase):

    @patch('src.security.OAuthHandler')
    def test_oauth_gmail(self, MockOAuthHandler):
        # Mocking the OAuthHandler
        mock_oauth = MockOAuthHandler()
        mock_oauth.authenticate.return_value = True

        # Test data
        gmail_api_key = "test_gmail_api_key"

        # Call the method to test
        result = mock_oauth.authenticate(gmail_api_key)

        # Assert the result
        self.assertTrue(result)

    @patch('src.security.OAuthHandler')
    def test_oauth_uber_eats(self, MockOAuthHandler):
        # Mocking the OAuthHandler
        mock_oauth = MockOAuthHandler()
        mock_oauth.authenticate.return_value = True

        # Test data
        uber_eats_api_key = "test_uber_eats_api_key"

        # Call the method to test
        result = mock_oauth.authenticate(uber_eats_api_key)

        # Assert the result
        self.assertTrue(result)

    @patch('src.security.OAuthHandler')
    def test_oauth_failure(self, MockOAuthHandler):
        # Mocking the OAuthHandler
        mock_oauth = MockOAuthHandler()
        mock_oauth.authenticate.return_value = False

        # Test data
        invalid_api_key = "invalid_api_key"

        # Call the method to test
        result = mock_oauth.authenticate(invalid_api_key)

        # Assert the result
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()
```