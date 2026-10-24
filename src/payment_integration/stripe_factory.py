from typing import Any

from .payment_provider_factory import PaymentProviderFactory
from .stripe_authorizer import StripeAuthorizer
from .stripe_refund_processor import StripeRefundProcessor
from .stripe_webhook_verifier import StripeWebhookVerifier


class StripeFactory(PaymentProviderFactory):
    def create_authorizer(self) -> Any:
        return StripeAuthorizer()

    def create_refund_processor(self) -> Any:
        return StripeRefundProcessor()

    def create_webhook_verifier(self) -> Any:
        return StripeWebhookVerifier()
