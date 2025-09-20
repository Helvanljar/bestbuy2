from typing import List
from products import Product


class Store:
    """Represents a store that holds products and allows purchasing."""

    def __init__(self, products: List[Product]):
        self.products = products

    def add_product(self, product: Product):
        """Add a product to the store."""
        self.products.append(product)

    def remove_product(self, product: Product):
        """Remove a product from the store."""
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        """Return total quantity of all products in the store."""
        return sum(p.get_quantity() for p in self.products)

    def get_all_products(self) -> List[Product]:
        """Return all active products."""
        return [p for p in self.products if p.is_active()]

    def order(self, shopping_list: List[tuple]) -> float:
        """
        Process an order of (Product, quantity) tuples.
        Returns total price of the order.
        """
        total = 0.0
        for product, quantity in shopping_list:
            if not product.is_active():
                raise ValueError(f"Product {product.name} is inactive.")
            total += product.buy(quantity)
        return total
