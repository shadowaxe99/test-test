```python
import unittest
from src.budgeting import calculate_budget
from src.utils.exceptions import BudgetExceededError

class TestBudgeting(unittest.TestCase):

    def setUp(self):
        self.user_profile = {
            "budget_limit": 20.00,
            "preferred_cuisines": ["Italian", "Mexican"],
            "allergies": ["Nuts"],
            "favorite_dishes": ["Pizza", "Tacos"]
        }

    def test_calculate_budget_within_limit(self):
        order_cost = 15.00
        self.assertEqual(calculate_budget(self.user_profile, order_cost), True)

    def test_calculate_budget_exceeds_limit(self):
        order_cost = 25.00
        self.assertRaises(BudgetExceededError, calculate_budget, self.user_profile, order_cost)

if __name__ == '__main__':
    unittest.main()
```