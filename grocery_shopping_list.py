grocery=["milk","vegetables","bread","fruit"]

# sorting list alphabetically
grocery.sort()
print(grocery,"\n")

# adding items in list
add_item=input("Enter an item you want to add: ")
grocery.append(add_item)
print("After adding new item:",add_item)
print("Updated list is this:",grocery,"\n")

# remove items from list
del_item=input("Enter an item which you want to remove from list: ")
grocery.remove(del_item)
print("After removing item:",del_item)
print("Updated list is this:",grocery,"\n")

# count number of items in list
print("Number of items in list are:",len(grocery),"\n")

# searching an item in list
sh=input("Enter an item you want to search: ")
for i in grocery:
    if sh==i:
        print(sh," is in the list!!")
        break
else:
    print(sh,"is not in the list!!")