```python
import datetime
import re

def extract_meal_keywords(event_description):
    """
    Extract meal keywords from event description.
    """
    meal_keywords = ["lunch", "breakfast", "dinner"]
    found_keywords = [word for word in meal_keywords if word in event_description.lower()]
    return found_keywords

def parse_gmail_event(event):
    """
    Parse Gmail event to extract necessary details.
    """
    event_details = {}
    event_details['start_time'] = datetime.datetime.fromisoformat(event['start']['dateTime'])
    event_details['end_time'] = datetime.datetime.fromisoformat(event['end']['dateTime'])
    event_details['description'] = event['description']
    event_details['location'] = event.get('location', '')
    event_details['meal_keywords'] = extract_meal_keywords(event_details['description'])
    return event_details

def calculate_total_cost(order_details, delivery_fee, tax_rate):
    """
    Calculate total cost of an order including delivery fee and tax.
    """
    total_cost = order_details['price'] + delivery_fee
    total_cost += total_cost * tax_rate
    return total_cost

def is_within_budget(total_cost, budget_limit):
    """
    Check if total cost is within budget limit.
    """
    return total_cost <= budget_limit

def extract_address_from_location(location):
    """
    Extract address from location string.
    """
    address = re.search(r'\d{1,4} .+, .+, .+ \d{5}', location)
    return address.group() if address else ''

def get_alternative_dish(preferred_dish, menu):
    """
    Get an alternative dish from the menu if the preferred dish is not available.
    """
    for dish in menu:
        if dish != preferred_dish and dish['type'] == preferred_dish['type']:
            return dish
    return None
```