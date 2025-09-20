from products import Product, NonStockedProduct, LimitedProduct
from store import Store


def start(store: Store):
    """Start the CLI interface for the store."""
    while True:
        print("\n===== Best Buy Menu =====")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            products = store.get_all_products()
            print("\nAvailable products:")
            for idx, product in enumerate(products, 1):
                print(f"{idx}. {product.show()}")

        elif choice == "2":
            print(f"Total quantity in store: {store.get_total_quantity()}")

        elif choice == "3":
            products = store.get_all_products()
            order_list = []
            print("\nEnter products you want to buy (type 'done' to finish):")

            for idx, product in enumerate(products, 1):
                print(f"{idx}. {product.show()}")

            while True:
                selection = input("Enter product number (or 'done'): ").strip()
                if selection.lower() == "done":
                    break

                try:
                    index = int(selection) - 1
                    if index < 0 or index >= len(products):
                        print("Invalid selection.")
                        continue

                    product = products[index]
                    quantity = int(
                        input(f"Enter quantity for {product.name}: ").strip()
                    )

                    order_list.append((product, quantity))
                except ValueError:
                    print("Invalid input. Try again.")

            try:
                total_price = store.order(order_list)
                print(f"\nOrder successful! Total price: {total_price} dollars.")
            except Exception as e:
                print(f"Order failed: {e}")

        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    # setup initial stock of inventory
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
        NonStockedProduct("Windows License", price=125),
        LimitedProduct("Shipping", price=10, quantity=250, maximum=1),
    ]

    best_buy = Store(product_list)
    start(best_buy)
