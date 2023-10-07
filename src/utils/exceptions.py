```python
class Error(Exception):
    """Base class for other exceptions"""
    pass

class OrderPlacementError(Error):
    """Raised when there is an issue with placing the order"""
    pass

class BudgetExceededError(Error):
    """Raised when the total cost of the order exceeds the user's budget limit"""
    pass

class DishUnavailableError(Error):
    """Raised when the preferred dish is not available"""
    pass

class APIError(Error):
    """Raised when there is an issue with the Gmail or Uber Eats API"""
    pass

class DeliveryUnavailableError(Error):
    """Raised when the user's location is not covered by Uber Eats delivery"""
    pass
```