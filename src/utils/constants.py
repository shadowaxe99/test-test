```python
# src/utils/constants.py

# API keys
GMAIL_API_KEY = "YOUR_GMAIL_API_KEY"
UBER_EATS_API_KEY = "YOUR_UBER_EATS_API_KEY"

# API limits
GMAIL_API_LIMIT = 5000  # Adjust based on actual limit
UBER_EATS_API_LIMIT = 1000  # Adjust based on actual limit

# Meal-related keywords
MEAL_KEYWORDS = ["lunch", "breakfast", "dinner"]

# Message names
CONFIRMATION_PROMPT = "ConfirmationPrompt"
ORDER_NOTIFICATION = "OrderNotification"

# DOM Element IDs
USER_PROFILE_FORM = "userProfileForm"
ORDER_FORM = "orderForm"
CONFIRMATION_PROMPT_ID = "confirmationPrompt"
NOTIFICATION_ID = "notification"

# OAuth 2.0 details
OAUTH_CLIENT_ID = "YOUR_OAUTH_CLIENT_ID"
OAUTH_CLIENT_SECRET = "YOUR_OAUTH_CLIENT_SECRET"

# Exception messages
ORDER_PLACEMENT_ERROR = "Error while placing order."
BUDGET_EXCEEDED_ERROR = "Budget limit exceeded."
DISH_UNAVAILABLE_ERROR = "Preferred dish is unavailable."
```