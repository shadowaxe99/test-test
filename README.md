# UMI - Uber Meals Intelligence

UMI is an AI agent that automatically orders Uber Eats based on the meetings scheduled in a Gmail calendar. It's designed for professionals and any individuals with frequent meetings and a preference for automated food delivery.

## Features

1. **Integration with Gmail Calendar**: UMI reads the user's Gmail calendar and detects keywords like "lunch", "breakfast", "dinner", or any custom tags set by the user to identify meal-related meetings.

2. **Setup & Personalization**: Users set up a profile including dietary preferences, allergies, and favorite cuisines. They can specify a default delivery address or use the location of the meeting (if provided).

3. **Ordering Mechanism**: UMI integrates with Uber Eats API for menu fetching, order placement, and payment processing. For recurring meetings, it allows the option to set recurring orders or diversify based on user preferences.

4. **Notifications & Confirmations**: Before placing an order, UMI sends a confirmation prompt to the user via email or a preferred communication method. It notifies the user once the order has been placed and provides ETA.

5. **Budgeting**: Users can set a budget limit for each meal or meeting. UMI will aim to place orders within this limit, considering delivery fees and taxes.

6. **Fallbacks & Alternatives**: In case a preferred dish isn't available, UMI picks an alternative based on user preferences or past orders. It also provides the option to skip meals or opt for a different delivery service in case Uber Eats is unavailable.

7. **Security**: UMI implements OAuth 2.0 for secure integration with Gmail and Uber Eats. It does not store sensitive data like passwords or payment information.

8. **Feedback Mechanism**: After delivery, UMI asks the user for feedback to improve future orders. Users can rate the food and provide comments.

## Installation

Please refer to `setup.py` for installation instructions.

## Usage

Please refer to `src/main.py` for usage instructions.

## Testing

Test cases are provided in the `src/tests` directory.

## Contributing

Please read `CONTRIBUTING.md` for details on our code of conduct, and the process for submitting pull requests to us.

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.