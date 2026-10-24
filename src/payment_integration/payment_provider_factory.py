from abc import ABC, abstractmethod
from typing import Any


class PaymentProviderFactory(ABC):
    @abstractmethod
    def create_authorizer(self) -> Any:
        pass

    @abstractmethod
    def create_refund_processor(self) -> Any:
        pass

    @abstractmethod
    def create_webhook_verifier(self) -> Any:
        pass
