# Best Buy Store Project

## Overview
This project simulates a small retail store system using Python.
It includes a product management system, a store inventory, and a command-line user interface (CLI) for interacting with the store.

It demonstrates **object-oriented programming**, including **classes, composition, and exception handling**, as well as **PEP 8 clean coding practices**.

---

## Features

### Product Class (`products.py`)
- Represents a single product in the store.
- Tracks:
  - Name
  - Price
  - Quantity
  - Active status
- Methods:
  - `buy(quantity)`: Buy a specific quantity and update stock.
  - `show()`: Print product info.
  - `set_quantity(quantity)`: Update quantity and deactivate if 0.
  - `activate()` / `deactivate()`: Toggle product status.
  - Input validation with exceptions.

### Store Class (`store.py`)
- Represents the store containing multiple products.
- Supports:
  - Adding/removing products
  - Getting total quantity of all products
  - Retrieving active products
  - Ordering multiple products at once with total cost calculation
- Uses **composition**: Store “has” Products.

### User Interface (`main.py`)
- Command-line interface (CLI) for interacting with the store.
- Menu options:
  1. List all active products
  2. Show total quantity in store
  3. Make an order
  4. Quit
- Robust input handling to prevent user errors.
- Updates product quantities and active status after purchases.

---

## Installation

1. Clone the repository (HTTPS):

```bash
git clone <your-repo-url>
cd bestbuy
```

2. Make sure you have Python 3 installed.

3. Run the application:

```bash
python3 main.py
```

---

## Usage

1. **List products** – Shows all active products with their price, quantity, and status.
2. **Show total quantity** – Displays the total number of items in the store.
3. **Make an order** – Choose one or more products, specify quantities, and see the total cost.
4. **Quit** – Exit the program safely.

The program ensures:
- Users cannot buy more than available stock.
- Invalid inputs are handled gracefully.
- Products deactivate automatically if stock reaches zero.

---

## Example

```
===== Welcome to Best Buy =====
1. List all products in store
2. Show total amount in store
3. Make an order
4. Quit
Enter your choice (1-4): 1

Products in store:
MacBook Air M2, Price: 1450, Quantity: 100, Status: Active
Bose QuietComfort Earbuds, Price: 250, Quantity: 500, Status: Active
Google Pixel 7, Price: 500, Quantity: 250, Status: Active
```

---

## Contributing
Feel free to fork this project, improve the UI, add persistence to a database or file, or extend product features.
Please submit pull requests with clear descriptions of your changes.

---

## License
This project is provided for educational purposes. No specific license is applied.

