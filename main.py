from products import Product
from store import Store


def start(store: Store):
    """Run a robust CLI for the store with full input validation."""
    while True:
        print("\n===== Welcome to Best Buy =====")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            products_list = store.get_all_products()
            if not products_list:
                print("No active products available in the store.")
            else:
                print("\nProducts in store:")
                for idx, product in enumerate(products_list, start=1):
                    print(f"{idx}. {product.show()}")

        elif choice == "2":
            total_quantity = store.get_total_quantity()
            print(f"Total quantity of all products in store: {total_quantity}")

        elif choice == "3":
            products_list = store.get_all_products()
            if not products_list:
                print("No active products available to order.")
                continue

            print("\nAvailable products:")
            for idx, product in enumerate(products_list, start=1):
                print(
                    f"{idx}. {product.name} - Price: {product.price}, "
                    f"Quantity: {product.get_quantity()}"
                )

            shopping_list = []

            while True:
                prod_choice = input(
                    "Enter product number to buy (or 'done' to finish): "
                ).strip()

                if prod_choice.lower() == "done":
                    break

                try:
                    product_idx = int(prod_choice) - 1
                    if not (0 <= product_idx < len(products_list)):
                        print("Invalid product number. Try again.")
                        continue
                except ValueError:
                    print("Please enter a valid number.")
                    continue

                product = products_list[product_idx]

                qty_input = input(f"Enter quantity for {product.name}: ").strip()
                try:
                    quantity = int(qty_input)
                    if quantity <= 0:
                        print("Quantity must be greater than zero.")
                        continue
                    if quantity > product.get_quantity():
                        print(
                            f"Cannot add {quantity} x {product.name}. "
                            f"Only {product.get_quantity()} available."
                        )
                        continue
                except ValueError:
                    print("Please enter a valid integer quantity.")
                    continue

                shopping_list.append((product, quantity))
                print(f"Added {quantity} x {product.name} to your order.")

            if shopping_list:
                try:
                    total_price = store.order(shopping_list)
                    print(f"Order successful! Total cost: {total_price} dollars.")
                except ValueError as e:
                    print(f"Error processing order: {e}")
            else:
                print("No items in the order.")

        elif choice == "4":
            print("Thank you for visiting Best Buy! Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1-4.")


if __name__ == "__main__":
    # Setup initial stock of inventory
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]
    best_buy = Store(product_list)

    start(best_buy)
