python
def minimal_customer_payload():
    return {
        "account_id": "to_complete",
        "first_name": "Jaya",
        "last_name": "Sudha",
        "email": "jaya.sudha@yuno.test"
    }

def minimal_purchase_payload(card):
    return {
        "account_id": "to_complete",
        "amount": 1000,
        "currency": "USD",
        "workflow": "DIRECT",
        "payment_method": {
            "type": "CARD",
            "card": card
        }
    }
