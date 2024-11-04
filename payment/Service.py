from payment.gateways.payment_gateways import RazorPaymentGateway


class PaymentService:
    def __init__(self):
        self.payment_gateway = RazorPaymentGateway()

    def initiate_payment(self, order_id, amount):
        return self.payment_gateway.generate_payment_link(order_id, amount)