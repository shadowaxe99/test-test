```python
import os
from oauthlib.oauth2 import BackendApplicationClient
from requests_oauthlib import OAuth2Session

class OAuthHandler:
    def __init__(self, service_name):
        self.service_name = service_name
        self.client_id = os.getenv(f'{service_name.upper()}_CLIENT_ID')
        self.client_secret = os.getenv(f'{service_name.upper()}_CLIENT_SECRET')

    def get_oauth_session(self):
        client = BackendApplicationClient(client_id=self.client_id)
        oauth = OAuth2Session(client=client)
        token = oauth.fetch_token(token_url=f'https://oauth2.{self.service_name}.com/token',
                                  client_id=self.client_id,
                                  client_secret=self.client_secret)
        return oauth

def get_gmail_oauth_session():
    gmail_oauth_handler = OAuthHandler('gmail')
    return gmail_oauth_handler.get_oauth_session()

def get_ubereats_oauth_session():
    ubereats_oauth_handler = OAuthHandler('ubereats')
    return ubereats_oauth_handler.get_oauth_session()
```