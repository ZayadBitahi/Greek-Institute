from menu_item import MenuItem
from menu_manager import MenuManager
import sys

def show_user_menu():
    while True:
        print("\n=== Menu Editor ===")
        print("[V] View an item")
        print("[A] Add an item")
        print("[D] Delete an item")
        print("[U] Update an item")
        print("[S] Show restaurant menu")
        print("[E] Exit")

        choice = input("Choose an option: ").strip().upper()

        if choice == "V":
            view_item()
        elif choice == "A":
            add_item_to_menu()
        elif choice == "D":
            remove_item_from_menu()
        elif choice == "U":
            update_item_from_menu()
        elif choice == "S":
            show_restaurant_menu()
        elif choice == "E":
            print("\nFinal restaurant menu:")
            show_restaurant_menu()
            sys.exit()
        else:
            print("Invalid option. Try again.")



def add_item_to_menu():
    name = input("Item name: ")
    try:
        price = float(input("Item price: "))
    except ValueError:
        print("Price must be a number.")
        return

    item = MenuItem(name, price)
    res, code = item.save()
    if code == 201:
        print("Item was added successfully.")
    else:
        print("Error adding item:", res.get("error", res.get("message")))

def remove_item_from_menu():
    name = input("Item name to delete: ")
    items = MenuManager.all_items()
    found = None
    for itm in items:
        if itm.item_name == name:
            found = itm
            break
    if not found:
        print("Item not found.")
        return

    res, code = found.delete()
    if code == 200:
        print("Item was deleted successfully.")
    else:
        print("Error deleting item:", res.get("error", res.get("message")))

def update_item_from_menu():
    old_name = input("Current item name: ")
    try:
        old_price = float(input("Current item price: "))
    except ValueError:
        print("Price must be a number.")
        return
    new_name = input("New item name: ")
    try:
        new_price = float(input("New item price: "))
    except ValueError:
        print("Price must be a number.")
        return

    item = MenuItem(old_name, old_price)
    res, code = item.update(new_name, new_price)
    if code == 200:
        print("Item updated successfully.")
    else:
        print("Error updating item:", res.get("error", res.get("message")))

def show_restaurant_menu():
    items = MenuManager.all_items()
    if not items:
        print("Menu is empty.")
        return
    print("\n--- Restaurant Menu ---")
    for item in items:
        print(f"- {item.item_name}: ${item.item_price}")

def view_item():
    name = input("Enter item name: ")
    item = MenuManager.get_by_name(name)
    if item:
        print(f"Found: {item.item_name} - ${item.item_price}")
    else:
        print("Item not found.")


if __name__ == "__main__":
    show_user_menu()
