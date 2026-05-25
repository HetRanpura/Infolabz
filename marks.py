def welcome():{
    print("Welcome to know your student")
}

def total_marks(mark1,mark2,mark3):{
    print("Total marks is",mark1+mark2+mark3)
}
    
def passing_mark():
    return 35

def average_marks(m1,m2,m3):
    return (m1+m2+m3)/3

def main():
    welcome()
    sub1 = int(input("Enter marks of python:"))
    sub2 = int(input("Enter marks of java:"))
    sub3 = int(input("Enter marks of C:"))
    total_marks(sub1,sub2,sub3)
    passing = passing_mark()
    print("Passing percent is",passing)
    percent = average_marks(sub1,sub2,sub3)
    print("Percentage is",percent)

main()
