luckydraw=[1111,2222,3333,4444]

# user in
user_in=int(input("Enter your choice: "))
print("Your chosen number is:",user_in)

print("here are winners!!!!")
for i in luckydraw:
    print(i)

# check
# for i in luckydraw:
#     if i==user_in:
#         print("you win!!")
#         break
# else:
#     print("you lose!!")


# 2nd way
if user_in in luckydraw:
    print("you win!!")
else:
    print("you lose!!")