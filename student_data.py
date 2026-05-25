f = open("student.txt","a")
f2 = open("student.txt","r")
data = f2.read()

a = input("To know about you student enter: [y/N]")
while True:
    if a == "y":
        print("1. Student Attendance.")
        print("2. Student Name.")
        print("3. Status.")
        print("4. Exit.")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            attendance = input("Enter Student Attendance: ")
            f.write(attendance)
            f.write("\n")
            print(data)
        elif choice == 2:
            name = input("Enter student name: ")
            f.write(name)
            f.write("\n")
            print(data)
        elif choice == 3:
            status = input("Enter [present/abset]")
            f.write(status)
            f.write("\n")
            print(data)
        elif choice == 4:
            print("Thank you!!")
            break
        else: 
            print("Invalid option!")
    elif a == "N":
        print("Thank you!!")
        break
    else:
        print("Invalid option!")
f.close()
f2.close()
