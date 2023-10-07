```python
from src.user_profile import user_profile
from src.utils.exceptions import BudgetExceededError

def calculate_budget(order):
    """
    Calculate the total cost of an order within the user's budget limit.
    """
    total_cost = order['price'] + order['delivery_fee'] + order['taxes']
    
    if total_cost > user_profile['budget_limit']:
        raise BudgetExceededError("The total cost of the order exceeds the budget limit.")
    
    return total_cost

def check_budget(order):
    """
    Check if the total cost of the order is within the user's budget limit.
    """
    try:
        total_cost = calculate_budget(order)
        return True
    except BudgetExceededError:
        return False
```