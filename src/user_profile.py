```python
class UserProfile:
    def __init__(self, dietary_preferences, allergies, favorite_cuisines, delivery_address):
        self.dietary_preferences = dietary_preferences
        self.allergies = allergies
        self.favorite_cuisines = favorite_cuisines
        self.delivery_address = delivery_address

    def update_profile(self, dietary_preferences=None, allergies=None, favorite_cuisines=None, delivery_address=None):
        if dietary_preferences is not None:
            self.dietary_preferences = dietary_preferences
        if allergies is not None:
            self.allergies = allergies
        if favorite_cuisines is not None:
            self.favorite_cuisines = favorite_cuisines
        if delivery_address is not None:
            self.delivery_address = delivery_address

    def get_profile(self):
        return {
            "dietary_preferences": self.dietary_preferences,
            "allergies": self.allergies,
            "favorite_cuisines": self.favorite_cuisines,
            "delivery_address": self.delivery_address
        }
```