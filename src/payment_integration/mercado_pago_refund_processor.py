class MercadoPagoRefundProcessor:
    def refund(self, amount: float) -> str:
        return f"mercado_pago:refunded:{amount:.2f}"
