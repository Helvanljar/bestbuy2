from abc import ABC
from promotions import Promotion


class Product:
    def __init__(self, name: str, price: float, quantity: int):
        if not name:
            raise ValueError("Product name cannot be empty.")
        if price <= 0:
            raise ValueError("Price must be positive.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self._name = name
        self._price = price
        self._quantity = quantity
        self._active = True
        self._promotion: Promotion | None = None

    # --- Properties ---
    @property
    def name(self):
        return self._name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value: float):
        if value <= 0:
            raise ValueError("Price must be positive.")
        self._price = value

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value: int):
        if value < 0:
            raise ValueError("Quantity cannot be negative.")
        self._quantity = value
        if self._quantity == 0:
            self.deactivate()

    @property
    def promotion(self):
        return self._promotion

    def set_promotion(self, promotion: Promotion | None):
        self._promotion = promotion

    # --- Status ---
    def is_active(self) -> bool:
        return self._active

    def deactivate(self):
        self._active = False

    def activate(self):
        self._active = True

    # --- Operations ---
    def buy(self, quantity: int) -> float:
        if not self.is_active():
            raise ValueError(f"Product {self.name} is not active.")
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")
        if quantity > self._quantity:
            raise ValueError(f"Not enough {self.name} in stock.")

        # Apply promotion if available
        if self._promotion:
            total_price = self._promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * quantity

        self._quantity -= quantity
        if self._quantity == 0:
            self.deactivate()

        return total_price

    # --- Magic Methods ---
    def __str__(self):
        promo_text = f" Promotion: {self._promotion.name}" if self._promotion else ""
        return f"{self.name}, Price: ${self.price} Quantity:{self.quantity}{promo_text}"

    def __gt__(self, other):
        return self.price > other.price

    def __lt__(self, other):
        return self.price < other.price


class NonStockedProduct(Product):
    def __init__(self, name: str, price: float):
        super().__init__(name, price, 0)

    def buy(self, quantity: int) -> float:
        if not self.is_active():
            raise ValueError(f"Product {self.name} is not active.")
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")

        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        return self.price * quantity

    def __str__(self):
        promo_text = f" Promotion: {self.promotion.name}" if self.promotion else ""
        return f"{self.name}, Price: ${self.price} (Non-stocked){promo_text}"


class LimitedProduct(Product):
    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        super().__init__(name, price, quantity)
        self.maximum = maximum

    def buy(self, quantity: int) -> float:
        if quantity > self.maximum:
            raise ValueError(
                f"Cannot buy more than {self.maximum} of {self.name} in one order."
            )
        if quantity > self.quantity:
            raise ValueError(f"Not enough {self.name} in stock.")
        if quantity <= 0:
            raise ValueError("Quantity must be positive.")

        # Apply promotion if exists
        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * quantity

        self.quantity -= quantity
        return total_price

    def __str__(self):
        promo_text = f" Promotion: {self.promotion.name}" if self.promotion else ""
        return (
            f"{self.name}, Price: ${self.price} Quantity:{self.quantity} "
            f"(Max per order: {self.maximum}){promo_text}"
        )
