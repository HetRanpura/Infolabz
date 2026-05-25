ticket=[2,8,20,80,28,69]
drawn = []
print("Here is your ticket:",ticket)

while True:
    no = int(input("Enter number drawn:"))
    if no not in drawn:
        drawn.append(no)

    print("Numbers drawn so far are:",drawn)

    matched = 0
    for i in ticket:
        if i in drawn:
            matched += 1
    print("Matched numbers:",matched,"/",len(ticket))

    if matched == len(ticket):
        print("You won!")
        break

    stop = input("Do you want to continue? (y/n)")
    if stop == "n":
        print("Game stopped!!")
        break
