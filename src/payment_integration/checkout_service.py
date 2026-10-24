from .payment_authorizer import PaymentAuthorizer
from .payment_provider_factory import PaymentProviderFactory
from .refund_processor import RefundProcessor
from .webhook_verifier import WebhookVerifier


class CheckoutService:
    def __init__(self, factory: PaymentProviderFactory):
        self.authorizer: PaymentAuthorizer = factory.create_authorizer()
        self.refunds: RefundProcessor = factory.create_refund_processor()
        self.webhooks: WebhookVerifier = factory.create_webhook_verifier()

    def authorize_payment(self, amount: float) -> str:
        return self.authorizer.authorize(amount)

    def refund_payment(self, amount: float) -> str:
        return self.refunds.refund(amount)

    def verify_webhook(self, signature: str) -> bool:
        return self.webhooks.verify(signature)