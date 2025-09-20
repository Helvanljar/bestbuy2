# BestBuy Store Project

## 📌 Overview
This project implements a simplified store system with **object-oriented programming (OOP)** concepts in Python.  
It includes product management, store operations, promotions, and a command-line interface (CLI).  
Bonus features like **magic methods** and **operator overloading** are also implemented.

---

## 🚀 Features

### Product System
- **Product**: Standard product with name, price, and quantity.
- **NonStockedProduct**: Digital/non-stocked products (e.g., software licenses).
- **LimitedProduct**: Products limited to a maximum purchase quantity.

### Store System
- Add/remove products.
- Order multiple products at once.
- Track total store quantity.
- List only **active products**.

### Promotions
- **PercentDiscount** → e.g., 30% off.
- **SecondHalfPrice** → Second item at half price.
- **ThirdOneFree** → Buy 2, get 1 free.
- Only one promotion can be applied per product.

### CLI (Command Line Interface)
User can:
1. List all products in store.
2. Show total amount in store.
3. Make an order (with validation).
4. Quit.

### Bonus Features (Magic Methods & Properties)
- `__str__`: Print product directly (`print(product)`).
- `>` `<`: Compare products by price.
- `in`: Check if a product exists in store.
- `+`: Combine two stores into a new store.
- Properties (`@property`) replace getters/setters with Pythonic syntax.

---

## 🛠️ Installation & Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/Helvanljar/bestbuy2.git
   cd bestbuy
   ```

2. Run the CLI:
   ```bash
   python main.py
   ```

3. Run tests:
   ```bash
   pytest -v
   ```

---

## ✅ Example Usage

```python
from products import Product, NonStockedProduct, LimitedProduct
from promotions import PercentDiscount, SecondHalfPrice, ThirdOneFree
from store import Store

# Setup initial stock
mac = Product("MacBook Air M2", price=1450, quantity=100)
bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
pixel = Product("Google Pixel 7", price=500, quantity=250)
windows = NonStockedProduct("Windows License", price=125)
shipping = LimitedProduct("Shipping", price=10, quantity=250, maximum=1)

# Store
best_buy = Store([mac, bose, pixel, windows, shipping])

# Promotions
second_half_price = SecondHalfPrice("Second Half price!")
third_one_free = ThirdOneFree("Third One Free!")
thirty_percent = PercentDiscount("30% off!", percent=30)

# Apply promotions
mac.set_promotion(second_half_price)
bose.set_promotion(third_one_free)
windows.set_promotion(thirty_percent)
```

---

## 🧪 Testing

Unit tests (`pytest`) cover:
- Product creation and invalid parameters.
- Stock depletion and activity status.
- Promotions logic.
- Store operations and orders.

Run tests:
```bash
pytest -v
```

---

## 👨‍💻 Author
Developed as part of the **BestBuy OOP Python project**.
