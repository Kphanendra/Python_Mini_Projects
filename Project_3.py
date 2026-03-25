# Mini Project 3: Shopping Cart System

# Initialize the cart
cart = []

def add_to_cart(product_name, price, quantity):
    # Check if item already exists to update quantity instead of duplicating
    for item in cart:
        if item['name'].lower() == product_name.lower():
            item['quantity'] += quantity
            print(f" Updated {product_name} quantity.")
            return
            
    # If new item, create dictionary and add to list
    product = {
        "name": product_name,
        "price": price,
        "quantity": quantity
    }
    cart.append(product)
    print(f" Added {product_name} to cart.")

def remove_from_cart(product_name):
    global cart
    cart = [item for item in cart if item['name'].lower() != product_name.lower()]
    print(f" Removed {product_name} from cart.")

def display_cart():
    if not cart:
        print("\n Your cart is empty!")
        return

    print("\n---------  YOUR SHOPPING CART --------")
    print(f"{'Item':<10} {'Price':<10} {'Qty':<5} {'Total':<10}")
    print("--------------------------------------")
    
    grand_total = 0
    for item in cart:
        item_total = item['price'] * item['quantity']
        grand_total += item_total
        print(f"{item['name']:<10} ₹{item['price']:<10} {item['quantity']:<5} ₹{item_total:<10.2f}")
    
    print("--------------------------------------")
    print(f"{'GRAND TOTAL:':<28} ₹{grand_total:.2f}")
    print("======================================")

# --- Testing the System ---
add_to_cart("Laptop", 60000, 1)
add_to_cart("Watch", 5000, 2)
add_to_cart("Mobile", 10000, 1)

display_cart()

remove_from_cart("Watch")
display_cart()