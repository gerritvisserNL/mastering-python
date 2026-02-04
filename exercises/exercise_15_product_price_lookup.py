products = {"apple": 1, "egg": 0.25, "bread": 2.25, "milk": 1.75, "butter": 0.9}

user_input = input("Type a product ").lower()

if user_input in products:
    print(f"Price: €{products[user_input]:.2f}")
else:
    print("Product not found")
