import paypalrestsdk
from django.conf import settings


class PayPalAPIProxy:
    def __init__(self):
        self.client_id = settings.PAYPAL_CLIENT_ID
        self.client_secret = settings.PAYPAL_CLIENT_SECRET
        self.mode = settings.PAYPAL_MODE
        paypalrestsdk.configure({
            'mode': self.mode,  # sandbox or live
            'client_id': self.client_id,
            'client_secret': self.client_secret
        })

    def create_payment(self, payment_data):
        """Create a payment using PayPal API."""
        payment = paypalrestsdk.Payment(payment_data)
        if payment.create():
            return payment
        else:
            return None

    def get_payment(self, payment_id):
        """Retrieve details of a payment."""
        try:
            payment = paypalrestsdk.Payment.find(payment_id)
            return payment
        except paypalrestsdk.ResourceNotFound:
            return None
