```python
import unittest
from src.user_profile import UserProfile

class TestUserProfile(unittest.TestCase):

    def setUp(self):
        self.user_profile = UserProfile()

    def test_set_preferences(self):
        self.user_profile.set_preferences('vegan')
        self.assertEqual(self.user_profile.preferences, 'vegan')

    def test_set_allergies(self):
        self.user_profile.set_allergies('peanuts')
        self.assertEqual(self.user_profile.allergies, 'peanuts')

    def test_set_favorite_cuisines(self):
        self.user_profile.set_favorite_cuisines('Italian')
        self.assertEqual(self.user_profile.favorite_cuisines, 'Italian')

    def test_set_delivery_address(self):
        self.user_profile.set_delivery_address('123 Main St')
        self.assertEqual(self.user_profile.delivery_address, '123 Main St')

    def test_set_budget_limit(self):
        self.user_profile.set_budget_limit(20)
        self.assertEqual(self.user_profile.budget_limit, 20)

if __name__ == '__main__':
    unittest.main()
```