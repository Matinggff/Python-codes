#restaurant
class Restaurant:
    def __init__(self, name):
        self.name = name
        self.menu = {}

    def add_dish(self, dish_name, price):
        self.menu[dish_name] = price

    def view_menu(self):
        print(f"Menu at {self.name}:")
        for dish, price in self.menu.items():
            print(f"{dish}: ${price:.2f}")

    def place_order(self, order):
        total_price = 0
        print(f"Order for {self.name}:")
        for item in order:
            if item in self.menu:
                print(f"{item}: ${self.menu[item]:.2f}")
                total_price += self.menu[item]
            else:
                print(f"{item} is not on the menu.")
        print(f"Total: ${total_price:.2f}")

if __name__ == "__main__":
    restaurant = Restaurant("My Restaurant")

    restaurant.add_dish("Burger", 10.99)
    restaurant.add_dish("Pizza", 12.99)
    restaurant.add_dish("Pasta", 8.99)

    while True:
        print("\nOptions:")
        print("1. View Menu")
        print("2. Place an Order")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            restaurant.view_menu()
        elif choice == "2":
            customer_order = input("Enter the items you want to order (comma-separated): ").split(",")
            restaurant.place_order(customer_order)
        elif choice == "3":
            print("Thank you for dining with us!")
            break
        else:
            print("Invalid choice. Please try again.")

