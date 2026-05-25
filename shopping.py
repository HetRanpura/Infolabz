cart = []
store = {"Milk":40,"Curd":75,"Butter Milk":20,"Butter":120,"Panner":75,"Milk Powder":20,"Noodles":14,"Ghee":100}

# ADD TO CART [], ADD
def add_cart(item):
    cart.append(item)
    print(cart)

# REMOVE FROM CART [DATA], REMOVE
def remove_cart(item):
    print(cart)
    rm = input("Enter an item you want to remove:")
    cart.remove(rm)
    print("updated cart =",cart)

# TOTAL AMOUNT LIST, CALCULATE [NOTE: NO SUM()]
def bill():
    total = 0
    for i in cart:
        if i in store.keys():
            total = total + store[i]
    print("Total amount =",total)

# APPY DISCOUNT 5000 > 20% ELSE 10%
def discount():
    total = 0
    for i in cart:
        if i in store.keys():
            total = total + store[i]
 
    if total > 5000:
        final = (total * 20) / 100
        print("Discount (20%) =", final)
        print("Final amount =", total - final)
    elif total > 0 and total <= 5000:
        final = (total * 10) / 100
        print("Discount (10%) =", final)
        print("Final amount =", total - final)
    else:
        print("Cart is empty, no discount applicable.")

# SEARCHING FIND IF IT'S THERE OR NOT 
def search(item):
    if item in store.keys():
        print(item, "is available. Price:", store[item])
    else:
        print(item, "is not available in the store.")

# MAIN FUNCTION
def main():
    print(store)
    while True:
        print("1. Display cart")
        print("2. Add item")
        print("3. Remove item")
        print("4. Total amount")
        print("5. Apply discount")
        print("6. Search item")
        print("7. Exit")
        n = int(input("Enter your choice:"))
        if n == 1:
            print(cart)

        elif n == 2:
            item = input("Enter item name: ")
            add_cart(item)

        elif n == 3:
            remove_cart(item)
        
        elif n == 4:
            bill()

        elif n == 5:
            discount()
  
        elif n == 6:
            item = input("Enter item name to search: ")
            search(item)

        elif n == 7:
            print("Thank you!")
            break

        else:
            print("Wrong option!!")


main()
