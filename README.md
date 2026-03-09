# Subscription-Based Content API

This is a backend API for a premium content platform built with Python, FastAPI, and PostgreSQL. It demonstrates basic access control based on user subscription status (Free vs. Premium), a simulated upgrade process, and activity logging.

## Prerequisites
- Python 3.8+
- PostgreSQL
- `pip` package manager

## Setup Instructions

1. **Install PostgreSQL** (if not already installed). Ensure it is running.
2. **Clone the repository / Navigate to the folder**:
   ```bash
   cd SUBAPI
   ```
3. **Install Dependencies**:
   ```bash
   pip install fastapi uvicorn sqlalchemy psycopg2-binary
   ```
4. **Configure the Database Structure**:
   - Create a PostgreSQL database named `subapi_db`. You can use your terminal or pgAdmin.
     *(Example command: `createdb -U postgres subapi_db`)*
   - In `database.py`, update the `DATABASE_URL` with your actual PostgreSQL username and password if it differs from the default.

5. **Run the Server**:
   ```bash
   uvicorn main:app --reload
   ```

## API Documentation
The best way to interact with the API is through FastAPI's automatic, interactive documentation. Once the server is running, simply open your browser and go to:
**[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)**

From there, you can expand any endpoint, click "Try it out", and execute requests directly from the UI.

## Example Requests (Using `curl`)

**1. Create a User (Defaults to Free)**
```bash
curl -X POST "http://127.0.0.1:8000/users/" \
     -H "Content-Type: application/json" \
     -d '{"username": "johndoe"}'
```

**2. Access Free Content**
```bash
curl "http://127.0.0.1:8000/content/free"
```

**3. Attempt to Access Premium Content (Will fail if Free)**
```bash
# Assuming the user created above has ID 1
curl "http://127.0.0.1:8000/content/premium?user_id=1"
```

**4. Upgrade User to Premium**
```bash
curl -X POST "http://127.0.0.1:8000/users/1/upgrade"
```

**5. Access Premium Content Successfully**
```bash
curl "http://127.0.0.1:8000/content/premium?user_id=1"
```


