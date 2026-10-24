from typing import Any

from .adyen_authorizer import AdyenAuthorizer
from .adyen_refund_processor import AdyenRefundProcessor
from .adyen_webhook_verifier import AdyenWebhookVerifier
from .payment_provider_factory import PaymentProviderFactory


class AdyenFactory(PaymentProviderFactory):
    def create_authorizer(self) -> Any:
        return AdyenAuthorizer()

    def create_refund_processor(self) -> Any:
        return AdyenRefundProcessor()

    def create_webhook_verifier(self) -> Any:
        return AdyenWebhookVerifier()
