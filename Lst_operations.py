lst=[46,35,16,10,25,45,10]
lst_float=[20.51,15.20,63.44]
lst_string=["hello","my","name","is","het"]
lst_mix=[13,25,52.15,55.01,"hii","meow",None,True]
print(lst,"\n")
# print(lst_mix,"\n")
# print(type(lst))
#
# #index 0
# print(lst[0],"\n")
#
# # print using loop
# for i in lst:
#     print(i)
# print("\n")
# searching
# sh=int(input("Enter a number to find if it's there or not: "))
# if sh in lst:
#     print(sh,"Found")
# else:
#     print(sh,"Not Found")
#

# emp=["EMP1","EMP2","EMP3","EMP4","EMP5"]
# a=input("Enter name for search: ")
# if a in emp:
#     print(a,"Found")
# else:
#     print(a,"Not Found")

# insert 2 way (insert, append)
lst.insert(2,50)
print(lst)

lst.append(69)
print(lst)

#remove last data pop, remove
lst.pop()
print(lst)

#pop index
lst.pop(2)
print(lst)

#specific value
lst.remove(16)
print(lst)

#sort
lst.sort()
print(lst)

#reverse
lst.reverse()
print(lst)

#clear
lst.clear()
print(lst)