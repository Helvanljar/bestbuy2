from abc import ABC, abstractmethod
from products import Product


class Promotion(ABC):
    """Abstract base class for promotions."""

    def __init__(self, name: str):
        self.name = name

    @abstractmethod
    def apply_promotion(self, product: Product, quantity: int) -> float:
        """Apply promotion logic and return discounted price."""
        pass


class PercentDiscount(Promotion):
    """Promotion: percentage discount on all items."""

    def __init__(self, name: str, percent: float):
        super().__init__(name)
        if percent <= 0 or percent >= 100:
            raise ValueError("Percent must be between 0 and 100.")
        self.percent = percent

    def apply_promotion(self, product: Product, quantity: int) -> float:
        discounted_price = product.price * (1 - self.percent / 100)
        return discounted_price * quantity


class SecondHalfPrice(Promotion):
    """Promotion: every second item at half price."""

    def apply_promotion(self, product: Product, quantity: int) -> float:
        pairs = quantity // 2
        remainder = quantity % 2
        return (pairs * (product.price + product.price * 0.5)) + (remainder * product.price)


class ThirdOneFree(Promotion):
    """Promotion: buy 2, get 1 free."""

    def apply_promotion(self, product: Product, quantity: int) -> float:
        groups_of_three = quantity // 3
        remainder = quantity % 3
        payable_quantity = (groups_of_three * 2) + remainder
        return payable_quantity * product.price

