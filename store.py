from products import Product


class Store:
    def __init__(self, products: list[Product]):
        self.products = products

    def add_product(self, product: Product):
        self.products.append(product)

    def remove_product(self, product: Product):
        self.products.remove(product)

    def get_total_quantity(self) -> int:
        return sum(product.quantity for product in self.products if product.is_active())

    def get_all_products(self) -> list[Product]:
        return [product for product in self.products if product.is_active()]

    def order(self, shopping_list: list[tuple[Product, int]]) -> float:
        total_price = 0
        for product, quantity in shopping_list:
            if quantity <= 0:
                raise ValueError(
                    f"Quantity for {product.name} must be positive."
                )
            total_price += product.buy(quantity)
        return total_price

    # --- Magic methods ---
    def __contains__(self, product: Product) -> bool:
        return product in self.products

    def __add__(self, other: "Store") -> "Store":
        return Store(self.products + other.products)
