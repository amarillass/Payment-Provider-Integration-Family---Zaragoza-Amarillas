class MercadoPagoAuthorizer:
    def authorize(self, amount: float) -> str:
        return f"mercado_pago:authorized:{amount:.2f}"
