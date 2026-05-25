# open 

# file = open("city.txt","r").read()
# print(file)

# write
# file2 = open("city.txt","w")
# file2.write("Paldi")


# file3 = open("city.txt","r").read()
# print(file3)

# append
# file4 = open("city.txt","a")
# file4.write("Ahmedabad")
# print(file4)

# file5 = open("city.txt","r").read()
# print(file5)

# f1 = open("city.txt","a")
# f1.write("\nDelhi")

# f2 = open("city.txt","r").read()
# print(f2)

# 2 files --> merge print
# f3 = open("city.txt","r")
# f4 = open("state.txt","r")

# data1 = f3.read()
# data2 = f4.read()

# f3.close()
# f4.close()

# print(data1, data2)

# mumbai --> first

f5 = open("city.txt","r")
data3 = f5.read()
f5.close()

f6 = open("city.txt","w")
f6.write("\nMumbai")
f6.close()

f = open("city.txt","a")
f.write(data3)
f.close()

f7 = open("city.txt","r").read()
print(f7)