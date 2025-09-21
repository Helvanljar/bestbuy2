import pytest
from products import Product, NonStockedProduct, LimitedProduct
from promotions import PercentDiscount, SecondHalfPrice, ThirdOneFree


def test_create_normal_product():
    p = Product("MacBook Air M2", price=1450, quantity=100)
    assert p.name == "MacBook Air M2"
    assert p.price == 1450
    assert p.quantity == 100
    assert p.is_active()


def test_create_product_invalid_name():
    with pytest.raises(ValueError):
        Product("", price=1450, quantity=100)


def test_create_product_invalid_price():
    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=-10, quantity=100)


def test_product_becomes_inactive_when_quantity_zero():
    p = Product("MacBook Air M2", price=1450, quantity=1)
    p.buy(1)
    assert p.quantity == 0
    assert not p.is_active()


def test_product_purchase_modifies_quantity_and_returns_total_price():
    p = Product("Bose QuietComfort Earbuds", price=250, quantity=10)
    total_price = p.buy(2)
    assert total_price == 500
    assert p.quantity == 8


def test_buying_more_than_available_raises_exception():
    p = Product("Google Pixel 7", price=500, quantity=5)
    with pytest.raises(ValueError):
        p.buy(10)


def test_limited_product_maximum():
    lp = LimitedProduct("Shipping", price=10, quantity=5, maximum=1)
    with pytest.raises(ValueError):
        lp.buy(2)


def test_non_stocked_product_buy():
    np = NonStockedProduct("Windows License", price=125)
    total = np.buy(3)
    assert total == 375


# --- Promotion tests ---
def test_percent_discount_promotion():
    p = Product("Test Product", price=100, quantity=10)
    promo = PercentDiscount("50% off", percent=50)
    p.set_promotion(promo)
    total = p.buy(2)
    assert total == 100  # 200 → 50% off = 100


def test_second_half_price_promotion():
    p = Product("Test Product", price=100, quantity=10)
    promo = SecondHalfPrice("Second half price")
    p.set_promotion(promo)
    total = p.buy(2)
    assert total == 150  # 100 + 50


def test_third_one_free_promotion():
    p = Product("Test Product", price=100, quantity=10)
    promo = ThirdOneFree("Third one free")
    p.set_promotion(promo)
    total = p.buy(3)
    assert total == 200  # pay for 2, get 1 free
