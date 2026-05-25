# no argument and no return type

def welcome():{
    print("function 1.")
}
welcome()

# Argument with no return type 
def sq_find(num):{
    print(f"Square is {num*num}")
}
sq_find(5)

# no argument with return type
def fixed_salary():
    return 10000
salary = fixed_salary()
print(salary)

# argument with return type
def division(num1,num2):
    return num1/num2
div = 