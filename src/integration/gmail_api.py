```python
import os
import datetime
from google.oauth2 import service_account
from googleapiclient.discovery import build

class GmailAPI:
    def __init__(self):
        self.gmail_api_key = os.getenv('GMAIL_API_KEY')
        self.credentials = service_account.Credentials.from_service_account_info(
            self.gmail_api_key, scopes=['https://www.googleapis.com/auth/calendar.readonly'])
        self.service = build('calendar', 'v3', credentials=self.credentials)

    def read_gmail_calendar(self, user_id='primary'):
        now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
        events_result = self.service.events().list(calendarId=user_id, timeMin=now,
                                                   maxResults=10, singleEvents=True,
                                                   orderBy='startTime').execute()
        events = events_result.get('items', [])

        meal_related_events = []
        meal_keywords = ['lunch', 'breakfast', 'dinner']

        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            summary = event['summary'].lower()

            if any(keyword in summary for keyword in meal_keywords):
                meal_related_events.append({
                    'start_time': start,
                    'summary': summary,
                    'location': event.get('location', '')
                })

        return meal_related_events
```