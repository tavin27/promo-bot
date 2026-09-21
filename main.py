from decimal import Decimal

from src.models.promotion import Promotion

promotion = Promotion(
    title="Teclado Mecânico",
    price=Decimal("199.90"),
    original_price=Decimal("249.90"),
    url="https://example.com/teclado",
    store="Loja de exemplo",
)

print(f"Produto: {promotion.title}")
print(f"Preço atual: R$ {promotion.price}")
print(f"Preço original: R$ {promotion.original_price}")
print(f"Loja: {promotion.store}")
print(f"Link: {promotion.url}")
print(f"Desconto: {promotion.discount_percentage}%")