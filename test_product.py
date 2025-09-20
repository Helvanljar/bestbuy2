import pytest
from products import Product, NonStockedProduct, LimitedProduct
import promotions


def test_create_normal_product():
    p = Product("MacBook Air M2", price=1450, quantity=100)
    assert p.name == "MacBook Air M2"
    assert p.price == 1450
    assert p.quantity == 100
    assert p.is_active() is True


def test_create_invalid_product():
    with pytest.raises(ValueError):
        Product("", price=1450, quantity=100)
    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=-10, quantity=100)
    with pytest.raises(ValueError):
        Product("MacBook Air M2", price=1450, quantity=-5)


def test_product_becomes_inactive_when_quantity_zero():
    p = Product("MacBook Air M2", price=1450, quantity=1)
    p.buy(1)
    assert p.is_active() is False


def test_product_purchase_reduces_quantity_and_returns_total():
    p = Product("Bose QuietComfort Earbuds", price=250, quantity=10)
    total = p.buy(2)
    assert total == 500
    assert p.quantity == 8


def test_buying_more_than_available_raises_exception():
    p = Product("Google Pixel 7", price=500, quantity=5)
    with pytest.raises(ValueError):
        p.buy(10)


# ===== Tests for NonStockedProduct =====

def test_nonstocked_product_has_zero_quantity():
    nsp = NonStockedProduct("Windows License", price=125)
    assert nsp.get_quantity() == 0
    assert "Non-stocked" in nsp.show()


def test_nonstocked_product_allows_unlimited_purchase():
    nsp = NonStockedProduct("Windows License", price=125)
    total = nsp.buy(1000)
    assert total == 125 * 1000


# ===== Tests for LimitedProduct =====

def test_limited_product_respects_maximum():
    lp = LimitedProduct("Shipping", price=10, quantity=50, maximum=1)
    with pytest.raises(ValueError):
        lp.buy(2)


def test_limited_product_allows_purchase_up_to_maximum():
    lp = LimitedProduct("Shipping", price=10, quantity=50, maximum=1)
    total = lp.buy(1)
    assert total == 10
    assert lp.quantity == 49


# ===== Tests for Promotions =====

def test_percent_discount_promotion():
    p = Product("MacBook Air M2", price=100, quantity=10)
    promo = promotions.PercentDiscount("10% off", percent=10)
    p.set_promotion(promo)
    total = p.buy(2)
    assert total == 180  # 2 * 90


def test_second_half_price_promotion():
    p = Product("Bose", price=100, quantity=10)
    promo = promotions.SecondHalfPrice("Second Half Price")
    p.set_promotion(promo)
    total = p.buy(2)
    assert total == 150  # 1*100 + 1*50


def test_third_one_free_promotion():
    p = Product("Pixel", price=100, quantity=10)
    promo = promotions.ThirdOneFree("Third One Free")
    p.set_promotion(promo)
    total = p.buy(3)
    assert total == 200  # 3 for the price of 2
