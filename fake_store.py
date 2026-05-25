import requests

url = requests.get("https://fakestoreapi.com/products")
data = url.json()

# print(data)
# for i in data[:5]:
#     print("Title",i["title"])
#     print("Prices",i["price"])
j = 0

# while j < len(data):
#     print("Title",data[j]["title"])
#     print("Prices",data[j]["price"])
#     j+=1

# for i in data[:3]:
#     print("Title",i["title"].upper())
#     print("Prices $",i["price"])

# for i in data[:5]:
#     print("Category",i["title"])

# while j < len(data):
#     if data[j]["price"] > 50:
#         print("Prices",data[j]["price"])
#     j+=1

# for i in data:
#     if i["category"] == "electronics":
#         print("Product",i["title"])

# print(data)
# for i in data[:5]:
#     print("Title and price is",i["title"],i["price"])

# while j < len(data):
#     if data[j]["price"] < 20:
#         print("Prices",data[j]["price"])
#     j+=1

# i = len(data) - 5
# while i < len(data):
#     print("Title",data[i]["title"])
#     i+=1

mydata = set()
for i in data:
    mydata.add(i["category"])
for i in mydata:
    print(mydata)