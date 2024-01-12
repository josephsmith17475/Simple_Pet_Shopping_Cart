import os

quit = True
store_items = ["Catnip","Dog Leash", "Fish Food", "Bird Seeds", "Hamster Wheel"]
store_item_prices = [2.50, 4.50, 9.99, 14.99, 16]
cart = []
cart_prices = []

def clear_screen():
    os.system("cls||clear")

def print_list(store_items, store_item_prices, choice):
    """handles the printing of the store items"""
    if choice == 0:
        for index,element in enumerate(store_items):
             print(f"{index+1}. {element}: £{store_item_prices[index]}")
    if choice == 1:
        for index,element in enumerate(store_items):
             print(f"{index+1}. {element}")
        


while quit:
    print("\nItems in stock are:")
    print_list(store_items, store_item_prices, 0)
    print("\n1 - add to shopping cart")
    print("2 - remove top item from shopping cart")
    print("3 - display cart")
    print("4 - purchase whats in the cart")
    try:
        choice = int(input("\nPlease enter a choice (1, 2, 3, 4) : "))
        clear_screen()
        if choice == 1:
            print("\nItems in stock are:")
            print_list(store_items, store_item_prices, 0)
            item = int(input("\nPlease enter the item you want to add to the cart(1, 2, 3, 4, 5): "))
            amount = int(input("\nHow many of this item do you want(1 to 10): "))
            clear_screen()
            if amount == 0 or amount > 10:
                print("This is a invalid amount, either you inputted 0 or you asked for more than the limit")
            elif amount == 1:
                cart.append(store_items[item-1])
                cart_prices.append(store_item_prices[item-1])
            else:
                cart.append(str(amount) + "x "+ store_items[item-1])
                cart_prices.append(amount*store_item_prices[item-1])
            print("Items added to cart:\n")
            print_list(cart, cart_prices, 0)
        elif choice == 2:
            print(f"Item removed from list was: {cart[len(cart)-1]}\n")
            cart.pop()
            cart_prices.pop()
        elif choice == 3:
            print("Cart:\n")
            print_list(cart, cart_prices, 0)
        elif choice == 4:
            print("Cart:\n")
            print_list(cart, cart_prices, 0)
            choice = input("\nThis is what is in the cart. Do you want to go to the checkout?(yes, no): ")
            if choice.lower().strip() == "no":
                clear_screen()
            elif choice.lower().strip() == "yes":
                clear_screen()
                print("\nHere is what is in your cart:\n")
                print_list(cart, cart_prices, 0)
                print(f"\nTotal is : £{round(sum(cart_prices),2)}")
                buy = input("\nWould you like to buy these products?(yes or no): ")
                if buy.lower().strip() == "yes":
                    clear_screen()
                    print(f"\nThank you for shopping here is your products: \n")
                    print_list(cart, cart_prices, 0)
                    quit = False
                elif buy.lower().strip() == "no":
                    clear_screen()
                else:
                    clear_screen()
            else:
                clear_screen()
    except ValueError:
        clear_screen()
        print("Value error. Please enter one of the options listed")
