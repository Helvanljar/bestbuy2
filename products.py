class Product:
    """Represents a product in the store."""

    def __init__(self, name: str, price: float, quantity: int):
        if not name:
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Product price cannot be negative.")
        if quantity < 0:
            raise ValueError("Product quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True
        self.promotion = None  # Promotion instance or None

    def get_quantity(self) -> int:
        """Return the current quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity: int):
        """Update quantity and deactivate product if it reaches zero."""
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if self.quantity == 0:
            self.deactivate()
        else:
            self.activate()

    def is_active(self) -> bool:
        """Return True if the product is active, False otherwise."""
        return self.active

    def activate(self):
        """Activate the product."""
        self.active = True

    def deactivate(self):
        """Deactivate the product."""
        self.active = False

    def set_promotion(self, promotion):
        """Assign a promotion to this product."""
        self.promotion = promotion

    def get_promotion(self):
        """Return the current promotion."""
        return self.promotion

    def show(self) -> str:
        promo_text = f", Promotion: {self.promotion.name}" if self.promotion else ""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}{promo_text}"

    def buy(self, quantity: int) -> float:
        if quantity <= 0:
            raise ValueError("Purchase quantity must be greater than zero.")
        if quantity > self.quantity:
            raise ValueError(
                f"Cannot buy {quantity} units. Only {self.quantity} available."
            )

        if self.promotion:
            total_price = self.promotion.apply_promotion(self, quantity)
        else:
            total_price = self.price * quantity

        self.set_quantity(self.quantity - quantity)
        return total_price


# ==============================
# New product types
# ==============================

class NonStockedProduct(Product):
    """Represents a product with no stock tracking (e.g., software license)."""

    def __init__(self, name: str, price: float):
        super().__init__(name, price, quantity=0)

    def set_quantity(self, quantity: int):
        """Non-stocked products always have 0 quantity."""
        self.quantity = 0

    def buy(self, quantity: int) -> float:
        if quantity <= 0:
            raise ValueError("Purchase quantity must be greater than zero.")

        if self.promotion:
            return self.promotion.apply_promotion(self, quantity)
        return self.price * quantity

    def show(self) -> str:
        promo_text = f", Promotion: {self.promotion.name}" if self.promotion else ""
        return f"{self.name}, Price: {self.price}, (Non-stocked){promo_text}"


class LimitedProduct(Product):
    """Represents a product that can only be purchased up to 'maximum' per order."""

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

        self.set_quantity(self.quantity - quantity)
        return total_price

    def show(self) -> str:
        promo_text = f", Promotion: {self.promotion.name}" if self.promotion else ""
        return (
            f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, "
            f"(Max {self.maximum} per order){promo_text}"
        )
