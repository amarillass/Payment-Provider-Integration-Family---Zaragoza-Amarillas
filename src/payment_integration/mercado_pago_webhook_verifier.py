class MercadoPagoWebhookVerifier:
    def verify(self, signature: str) -> bool:
        return signature == "mercado_pago-valid"
