from payment_integration.adyen_factory import AdyenFactory
from payment_integration.checkout_service import CheckoutService
from payment_integration.mercado_pago_factory import MercadoPagoFactory
from payment_integration.stripe_factory import StripeFactory


def test_stripe_family_is_selected_together():
    checkout = CheckoutService(StripeFactory())

    assert checkout.authorize_payment(125.50) == "stripe:authorized:125.50"
    assert checkout.refund_payment(25.00) == "stripe:refunded:25.00"
    assert checkout.verify_webhook("stripe-valid") is True
    assert checkout.verify_webhook("adyen-valid") is False


def test_adyen_family_is_selected_together():
    checkout = CheckoutService(AdyenFactory())

    assert checkout.authorize_payment(125.50) == "adyen:authorized:125.50"
    assert checkout.refund_payment(25.00) == "adyen:refunded:25.00"
    assert checkout.verify_webhook("adyen-valid") is True
    assert checkout.verify_webhook("stripe-valid") is False


def test_mercado_pago_family_is_selected_together():
    checkout = CheckoutService(MercadoPagoFactory())

    assert checkout.authorize_payment(125.50) == "mercado_pago:authorized:125.50"
    assert checkout.refund_payment(25.00) == "mercado_pago:refunded:25.00"
    assert checkout.verify_webhook("mercado_pago-valid") is True
    assert checkout.verify_webhook("stripe-valid") is False
