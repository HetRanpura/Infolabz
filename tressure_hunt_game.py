print("🏴‍☠️ Welcome to the Tressure Hunt game")

# locations
places=["los santos","mount fuji","epstein island","new york"]

# tressure place
tressure="new york"

# inventory
inventory = []

# main game logic
while True:
    for i in range(len(places)):
        print(i+1,".",places[i])

    choice = int(input("Enter your choice: "))
    if choice==1:
        print("You entered Los santos")
        print("you found the map!")
        inventory.append("map")

    elif choice==2:
        print("You entered mount fuji")
        print("You found the key!")
        inventory.append("key")

    elif choice==3:
        print("You entered epstein island")
        print("You are scared of there activities")

    elif choice==4:
        print("You entered new york")

        if "key" in inventory and "map" in inventory:
            print("Congratulations you found the tressure!!!!")
            print("You win!!!!")
            break
        else:
            print("You don't have key or map")

    else:
        print("Invalid choice")

    print("Here is your inventory:",inventory)

print("Game over!")