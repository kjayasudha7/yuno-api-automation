python
import os

BASE_URL = "https://api.y.uno/v1"

PUBLIC_API_KEY = os.getenv("PUBLIC_API_KEY")
PRIVATE_SECRET_KEY = os.getenv("PRIVATE_SECRET_KEY")
ACCOUNT_ID = os.getenv("ACCOUNT_ID")

if not all([PUBLIC_API_KEY, PRIVATE_SECRET_KEY, ACCOUNT_ID]):
    raise EnvironmentError("Missing required environment variables")
