import pytest
from products import Product, NonStockedProduct, LimitedProduct


def test_create_normal_product():
    """Test that creating a normal product works."""
    p = Product("MacBook Air M2", price=1450, quantity=100)
    assert p.name == "MacBook Air M2"
    assert p.price == 1450
    assert p.quantity == 100
    assert p.active


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
    p.buy(1)
    assert p.quantity == 0
    assert not p.active


def test_product_purchase_modifies_quantity_and_returns_total_price():
    """Test that product purchase modifies quantity and returns correct total."""
    p = Product("Bose QuietComfort Earbuds", price=250, quantity=10)
    total_price = p.buy(2)
    assert total_price == 500
    assert p.quantity == 8


def test_buying_more_than_available_raises_exception():
    """Test that buying a larger quantity than available raises ValueError."""
    p = Product("Google Pixel 7", price=500, quantity=5)
    with pytest.raises(ValueError):
        p.buy(10)


def test_non_stocked_product_always_quantity_zero():
    """Test that NonStockedProduct always has quantity 0."""
    nsp = NonStockedProduct("Windows License", price=125)
    assert nsp.quantity == 0
    nsp.quantity = 10
    assert nsp.quantity == 0


def test_limited_product_restricts_maximum():
    """Test that LimitedProduct enforces maximum per order."""
    lp = LimitedProduct("Shipping", price=10, quantity=5, maximum=1)
    with pytest.raises(ValueError):
        lp.buy(2)


def test_str_magic_method():
    """Test that __str__ returns the correct string."""
    p = Product("MacBook Air M2", price=1450, quantity=100)
    expected = "MacBook Air M2, Price: $1450 Quantity:100"
    assert str(p) == expected


def test_comparison_magic_methods():
    """Test product price comparison operators."""
    p1 = Product("MacBook Air M2", price=1450, quantity=100)
    p2 = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    assert p1 > p2
    assert p2 < p1
