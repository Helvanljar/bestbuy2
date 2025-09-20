import pytest
from products import Product


def test_create_normal_product():
    """Test that creating a normal product works."""
    p = Product("MacBook Air M2", price=1450, quantity=100)
    assert p.name == "MacBook Air M2"
    assert p.price == 1450
    assert p.quantity == 100
    assert p.is_active()


def test_create_product_invalid_name():
    """Test that creating a product with empty name raises ValueError."""
    with pytest.raises(ValueError):
        Product("", price=1450, quantity=100)


def test_create_product_invalid_price():
    """Test that creating a product with negative price raises ValueError."""
    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=-10, quantity=100)


def test_product_becomes_inactive_when_quantity_zero():
    """Test that when a product reaches 0 quantity, it becomes inactive."""
    p = Product("MacBook Air M2", price=1450, quantity=1)
    p.buy(1)  # reduce to 0
    assert p.get_quantity() == 0
    assert not p.is_active()


def test_product_purchase_modifies_quantity_and_returns_total_price():
    """Test that product purchase modifies quantity and returns correct total."""
    p = Product("Bose QuietComfort Earbuds", price=250, quantity=10)
    total_price = p.buy(2)
    assert total_price == 500
    assert p.get_quantity() == 8


def test_buying_more_than_available_raises_exception():
    """Test that buying a larger quantity than available raises ValueError."""
    p = Product("Google Pixel 7", price=500, quantity=5)
    with pytest.raises(ValueError):
        p.buy(10)
