from typing import List
from products import Product


class Store:
    """Represents a store that holds products and allows purchasing."""

    def __init__(self, products: List[Product]):
        self.products = products

    def add_product(self, product: Product):
        self.products.append(product)

    def remove_product(self, product: Product):
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        return sum(p.quantity for p in self.products)

    def get_all_products(self) -> List[Product]:
        return [p for p in self.products if p.active]

    def order(self, shopping_list: List[tuple]) -> float:
        total = 0.0
        for product, quantity in shopping_list:
            if not product.active:
                raise ValueError(f"Product {product.name} is inactive.")
            total += product.buy(quantity)
        return total

    # ========= Magic Methods =========
    def __contains__(self, product: Product) -> bool:
        return product in self.products

    def __add__(self, other):
        if not isinstance(other, Store):
            return NotImplemented
        return Store(self.products + other.products)
