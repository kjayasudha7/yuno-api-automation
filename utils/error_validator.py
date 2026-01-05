python
from constants.error_codes import ErrorCodes

def validate_error_response(response, expected_status, expected_code):
    assert response.status_code == expected_status

    body = response.json()
    assert "code" in body
    assert "messages" in body
    assert body["code"] == expected_code
    assert isinstance(body["messages"], list)
