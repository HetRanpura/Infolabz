print("Welcome to Los Santos ATM")

account=[50000]
account2=[0]

while True:
    print("1. Check balance")
    print("2. Deposit money")
    print("3. Withdraw money")
    print("4. Transfer money")
    print("5. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Here is the balance of both accounts:\n1.",account,"\n2.",account2)

    elif choice == 2:
        print("Which account you want to deposit:\n1. Account1.\n2. Account2.")
        a=int(input("Enter your choice: "))
        if a==1:
            amount = int(input("Enter amount to deposit: "))
            account[0] += amount
            print(amount,"Added successfully")
        elif a==2:
            amount = int(input("Enter amount to deposit: "))
            account2[0] += amount
            print(amount,"Added successfully")
        else:
            print("Invalid choice")

    elif choice == 3:
        print("From which account you want to withdraw: ")
        print("1. account1")
        print("2. account2")
        a=int(input("Enter your choice: "))
        amount= int(input("Enter amount to withdraw: "))
        if a==1:
            if amount <= account[0]:
                account[0] -= amount
                print(amount,"Withdrawn successfully")
            else:
                print("Insufficient balance")
        elif a==2:
            if amount <= account2[0]:
                account2[0] -= amount
                print(amount,"Withdrawn successfully")
            else:
                print("Insufficient balance")
        else:
            print("invalid choice")

    elif choice == 4:
        amount = int(input("Enter amount to transfer: "))
        if amount <= account[0]:
            account[0] -= amount
            account2[0] += amount
            print(amount,"Transferred successfully")
        else:
            print("Insufficient balance")
        print("Here is the balance of account2:",account2[0])

    elif choice == 5:
        print("Thank you")
        break

    else:
        print("Invalid choice")
