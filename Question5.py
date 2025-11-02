import sys

def add_item(cart):
    while True:
        name = input("Item name: ").strip()
        if name.isalpha():
            break
        else:
            print("Enter a valid name.")
    
    while True:
        price_input = input("Price: ").strip()
        if price_input.isnumeric():
            price = int(price_input)
            break
        else:
            print("Enter a valid numeric price.")
    
    while True:
        quantity_input = input("Quantity: ").strip()
        if quantity_input.isnumeric():
            quantity = int(quantity_input)
            break
        else:
            print("Enter a valid numeric quantity.")
    
    if name in cart:
        cart[name]["quantity"] += quantity
    else:
        cart[name] = {"price": price, "quantity": quantity}
    
    print("Item added!")

def remove_item(cart):
    while True:
        name = input("Item name: ").strip()
        if name.isalpha():
            break
        else:
            print("Enter a valid name.")
    
    if name in cart:
        del cart[name]
        print(f"{name} removed from cart")
    else:
        print("This item doesn't exist in the cart.")

def update_quantity(cart):
    while True:
        name = input("Item name: ").strip()
        if name.isalpha():
            break
        else:
            print("Enter a valid name.")
    
    while True:
        quantity_input = input("Quantity: ").strip()
        if quantity_input.isnumeric():
            quantity = int(quantity_input)
            break
        else:
            print("Enter a valid numeric quantity.")
    
    if name in cart:
        cart[name]["quantity"] = quantity
        print(f"{name} updated")
    else:
        print("This item doesn't exist in the cart.")

def view_cart(cart):
    print("Cart Summary")
    if not cart:
        print("Your cart is empty.")
        return
    
    total_cost = 0
    for item, info in cart.items():
        quantity = info["quantity"]
        price = info["price"]
        total = quantity * price
        total_cost += total
        print(f"{info["quantity"]}   |   {quantity}   |   {price}   |   {total}")
    
    print(f"Total Cart: {total_cost}")

def checkout(cart):
    if not cart:
        print("Add items to checkout")
        return
    
    cart.clear()
    print("Checkout done")

def main():
    print("Shopping Cart Menu:")
    print("Cart Summary:")
    print("1. Add item")
    print("2. Remove item")
    print("3. Update quantity")
    print("4. View cart")
    print("5. Checkout")
    print("6. Exit")
    
    cart = {}
    
    while True:
        choice = int(input("Choice: "))
        
        if choice == 1:
            add_item(cart)
        
        elif choice == 2:
            remove_item(cart)
            
        elif choice == 3:
            update_quantity(cart)
        
        elif choice == 4:
            view_cart(cart)
            
        elif choice == 5:
            checkout(cart)
        
        elif choice == 6:
            break

main()