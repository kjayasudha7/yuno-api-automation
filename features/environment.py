python
from utils.headers import build_headers

def before_scenario(context, scenario):
    context.headers = build_headers()
    context.response = None
    context.customer_id = None
    context.payment_id = None
