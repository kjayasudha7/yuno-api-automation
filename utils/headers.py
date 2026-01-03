python
import uuid

def build_headers():
    return {
        "Content-Type": "application/json",
        "public-api-key": "to_complete",
        "private-secret-key": "to_complete",
        "x-idempotency-key": str(uuid.uuid4())
    }
