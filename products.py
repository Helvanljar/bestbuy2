class Product:
    """Represents a product in the store."""

    def __init__(self, name: str, price: float, quantity: int):
        if not name:
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Product price cannot be negative.")
        if quantity < 0:
            raise ValueError("Product quantity cannot be negative.")

        self._name = name
        self._price = price
        self._quantity = quantity
        self._active = True
        self.promotion = None  # Promotion instance or None

    # ========= Properties =========
    @property
    def name(self) -> str:
        return self._name

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value

    @property
    def quantity(self) -> int:
        return self._quantity

    @quantity.setter
    def quantity(self, value: int):
        if value < 0:
            raise ValueError("Quantity cannot be negative.")
        self._quantity = value
        if self._quantity == 0:
            self.deactivate()
        else:
            self.activate()

    @property
    def active(self) -> bool:
        return self._active

    # ========= Methods =========
    def activate(self):
        self._active = True

    def deactivate(self):
        self._active = False

    def set_promotion(self, promotion):
        self.promotion = promotion

    def get_promotion(self):
        return self.promotion

    def buy(self, quantity: int) -> float:
        if quantity <= 0:
            raise ValueError("Purchase quantity must be greater than zero.")
        if self._quantity < quantity:
            raise ValueError(
                f"Cannot buy {quantity} units. Only {self._quantity} available."
            )

        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self._price * quantity

        self.quantity = self._quantity - quantity
        return total_price

    # ========= Magic Methods =========
    def __str__(self) -> str:
        promo_text = f", Promotion: {self.promotion.name}" if self.promotion else ""
        return f"{self._name}, Price: ${self._price} Quantity:{self._quantity}{promo_text}"

    def __gt__(self, other) -> bool:
        if not isinstance(other, Product):
            return NotImplemented
        return self._price > other._price

    def __lt__(self, other) -> bool:
        if not isinstance(other, Product):
            return NotImplemented
        return self._price < other._price


# ==============================
# NonStockedProduct
# ==============================

class NonStockedProduct(Product):
    def __init__(self, name: str, price: float):
        super().__init__(name, price, quantity=0)

    @Product.quantity.setter
    def quantity(self, value: int):
        """Non-stocked products always stay at 0 quantity."""
        self._quantity = 0

    def buy(self, quantity: int) -> float:
        if quantity <= 0:
            raise ValueError("Purchase quantity must be greater than zero.")
        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        return self.price * quantity

    def __str__(self) -> str:
        promo_text = f", Promotion: {self.promotion.name}" if self.promotion else ""
        return f"{self.name}, Price: ${self.price} (Non-stocked){promo_text}"


# ==============================
# LimitedProduct
# ==============================

class LimitedProduct(Product):
    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        super().__init__(name, price, quantity)
        if maximum <= 0:
            raise ValueError("Maximum must be greater than zero.")
        self.maximum = maximum

    def buy(self, quantity: int) -> float:
        if quantity > self.maximum:
            raise ValueError(
                f"Cannot buy more than {self.maximum} units of {self.name} per order."
            )

        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = super().buy(quantity)

        self.quantity = self.quantity - quantity
        return total_price

    def __str__(self) -> str:
        promo_text = f", Promotion: {self.promotion.name}" if self.promotion else ""
        return (
            f"{self.name}, Price: ${self.price}, Quantity:{self.quantity}, "
            f"(Max {self.maximum} per order){promo_text}"
        )
