# add cart option
# display cart 
# place order
f = open("shopping_cart.txt","a")
f2 = open("shopping_cart.txt","r").read()
item = None
a = input("Get a cart for shopping!! [y/N]")
while True:
    if a == "y":
        print("1. Display Cart.")
        print("2. Add to Cart.")
        print("3. Place order.")
        choice = int(input("Enter your choice:"))
        if choice == 1:
            print(item)
        elif choice == 2:
            item = input("Enter item name you want to add: ")
            f.write(item)
            f.write(", ")
            print(item)
        elif choice == 3:
            print("Your order of",item,"is placed!!")
            print("Thank you!")
            break
        else:
            print("invalid option!!")
    elif a == "N":
        print("Thank you!")
        break
    else:
        print("Invalid option!!")
f.close()
