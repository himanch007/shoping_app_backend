# Shopping App Backend

## Project Setup

### 1. Clone the Repository
```bash
git clone https://github.com/himanch007/shoping_app_backend.git
cd shopping_app_backend

# Using virtualenv
python -m venv venv

# Activate the virtual environment
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# .env
MONGO_HOST=127.0.0.1
MONGO_PORT=27017
SECRET_KEY=super-secret-key
DOCS_URL=/docs

# Install MongoDB

# Run the application in local machine
uvicorn app:app --reload

# Run the application in production
uvicorn main:app --host 0.0.0.0 --port 8000
