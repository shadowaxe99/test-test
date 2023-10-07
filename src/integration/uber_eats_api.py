```python
import requests
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

from src.utils.constants import UBER_EATS_API_LIMIT
from src.utils.exceptions import DishUnavailableError

class UberEatsAPI:
    def __init__(self, client_id, client_secret):
        self.client_id = client_id
        self.client_secret = client_secret
        self.base_url = "https://api.ubereats.com"
        self.session = self._create_oauth_session()

    def _create_oauth_session(self):
        client = BackendApplicationClient(client_id=self.client_id)
        oauth = OAuth2Session(client=client)
        token = oauth.fetch_token(token_url='https://api.ubereats.com/token', client_id=self.client_id, client_secret=self.client_secret)
        return oauth

    def fetch_menu(self, restaurant_id):
        url = f"{self.base_url}/v1/restaurants/{restaurant_id}/menu"
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()

    def place_order(self, order):
        url = f"{self.base_url}/v1/orders"
        response = self.session.post(url, json=order)
        if response.status_code == 429:
            raise Exception("API limit reached: " + UBER_EATS_API_LIMIT)
        response.raise_for_status()
        return response.json()

    def get_dish(self, restaurant_id, dish_name):
        menu = self.fetch_menu(restaurant_id)
        for category in menu['categories']:
            for dish in category['dishes']:
                if dish['name'].lower() == dish_name.lower():
                    return dish
        raise DishUnavailableError(f"Dish {dish_name} not found in restaurant {restaurant_id}")

    def get_alternative_dish(self, restaurant_id, dish_name, user_profile):
        menu = self.fetch_menu(restaurant_id)
        for category in menu['categories']:
            for dish in category['dishes']:
                if dish['name'].lower() != dish_name.lower() and dish['cuisine'].lower() in user_profile['favorite_cuisines']:
                    return dish
        raise DishUnavailableError(f"No alternative dish found in restaurant {restaurant_id}")
```