# Notification API

This project is a FastAPI application that provides an API for sending email and SMS notifications to users based on a specified payload. The application verifies the cardId against the email in a MongoDB database and sends notifications accordingly.

## Project Structure

```
notification-api
├── app
│   ├── main.py          # Entry point of the application
│   ├── models.py        # Data models for MongoDB
│   ├── routes.py        # API endpoints
│   ├── schemas.py       # Pydantic schemas for request validation
│   └── utils.py         # Utility functions for sending notifications
├── requirements.txt      # Project dependencies
├── README.md             # Project documentation
└── .env                  # Environment variables
```

## Setup Instructions

1. **Clone the repository:**
   ```
   git clone <repository-url>
   cd notification-api
   ```

2. **Create a virtual environment:**
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install dependencies:**
   ```
   pip install -r requirements.txt
   ```

4. **Configure environment variables:**
   Create a `.env` file in the root directory and add your MongoDB connection string and API key:
   ```
   MONGODB_URI=<your_mongodb_uri>
   API_KEY=<your_api_key>
   ```

5. **Run the application:**
   ```
   uvicorn app.main:app --reload
   ```

## API Usage

### Endpoint

- **POST /notify**

### Request Payload

The request should be a JSON object with the following structure:

```json
{
  "cardId": 123,
  "email": "user@example.com",
  "phoneNumber": "1234567890",
  "emailInfo": {
    "subject": "Notification Subject",
    "body": "This is the body of the notification."
  }
}
```

### Response

The API will respond with a JSON object indicating the success or failure of the notification for each `cardId`.

### Example

```bash
curl -X POST "http://localhost:8000/notify" \
-H "Content-Type: application/json" \
-H "apikey: <your_api_key>" \
-d '{
  "cardId": 123,
  "email": "user@example.com",
  "phoneNumber": "1234567890",
  "emailInfo": {
    "subject": "Test Notification",
    "body": "This is a test."
  }
}'
```

## License

This project is licensed under the MIT License. See the LICENSE file for more details.