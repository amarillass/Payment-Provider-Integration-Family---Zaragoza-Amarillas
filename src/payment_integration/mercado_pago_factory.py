from typing import Any

from .mercado_pago_authorizer import MercadoPagoAuthorizer
from .mercado_pago_refund_processor import MercadoPagoRefundProcessor
from .mercado_pago_webhook_verifier import MercadoPagoWebhookVerifier
from .payment_provider_factory import PaymentProviderFactory


class MercadoPagoFactory(PaymentProviderFactory):
    def create_authorizer(self) -> Any:
        return MercadoPagoAuthorizer()

    def create_refund_processor(self) -> Any:
        return MercadoPagoRefundProcessor()

    def create_webhook_verifier(self) -> Any:
        return MercadoPagoWebhookVerifier()
