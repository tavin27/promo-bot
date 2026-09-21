from dataclasses import dataclass
from decimal import Decimal

@dataclass
class Promotion:
    title: str
    price: Decimal
    original_price: Decimal
    url: str
    store: str

    @property
    def discount_percentage(self) -> Decimal:
        if self.original_price <= 0:
            return Decimal("0")

        discount = (
            (self.original_price - self.price) / self.original_price * 100
        )

        return discount.quantize(Decimal("0.01"))