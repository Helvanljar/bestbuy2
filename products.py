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

    def show(self) -> str:
        """Return a string representation of the product."""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity: int) -> float:
        """
        Buy a given quantity of the product.
        Returns the total price of the purchase.
        Raises ValueError if quantity is invalid.
        """
        if quantity <= 0:
            raise ValueError("Purchase quantity must be greater than zero.")
        if quantity > self.quantity:
            raise ValueError(
                f"Cannot buy {quantity} units. Only {self.quantity} available."
            )

        total_price = self.price * quantity
        self.set_quantity(self.quantity - quantity)
        return total_price


# ==============================
# New product types
# ==============================

class NonStockedProduct(Product):
    """Represents a product with no stock tracking (e.g., software license)."""

    def __init__(self, name: str, price: float):
        # Always call base class with quantity=0
        super().__init__(name, price, quantity=0)

    def set_quantity(self, quantity: int):
        """Non-stocked products always have 0 quantity."""
        self.quantity = 0

    def buy(self, quantity: int) -> float:
        """Always allow purchase regardless of stock."""
        if quantity <= 0:
            raise ValueError("Purchase quantity must be greater than zero.")
        return self.price * quantity

    def show(self) -> str:
        """Return a string representation for non-stocked product."""
        return f"{self.name}, Price: {self.price}, (Non-stocked)"


class LimitedProduct(Product):
    """Represents a product that can only be purchased up to 'maximum' per order."""

    def __init__(self, name: str, price: float, quantity: int, maximum: int):
        super().__init__(name, price, quantity)
        if maximum <= 0:
            raise ValueError("Maximum must be greater than zero.")
        self.maximum = maximum

    def buy(self, quantity: int) -> float:
        """Allow buying only up to 'maximum' per order."""
        if quantity > self.maximum:
            raise ValueError(
                f"Cannot buy more than {self.maximum} units of {self.name} per order."
            )
        return super().buy(quantity)

    def show(self) -> str:
        """Return a string representation for limited product."""
        return (
            f"{self.name}, Price: {self.price}, Quantity: {self.quantity}, "
            f"(Max {self.maximum} per order)"
        )
