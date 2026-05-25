import requests

url=requests.get("https://openlibrary.org/subjects/science_fiction.json")
data=url.json()

# number of keys
print(len(data))

# keys
print(len(data["works"]))


# type of keys
print(type(data))

# loop for all data
for i in range(len(data["works"])):
    print("=================BOOK INFORMATION REPORT====================")
    print("Book Title:",data["works"][i]["title"])
    print("Primary Authors:",data["works"][i]["authors"][0]["name"])
    print("First Publisher Yr:",data["works"][i]["first_publish_year"])
    print("Edition Count:",data["works"][i]["edition_count"])
    print("Unique Identifier:",data["works"][i]["availability"]["identifier"])
    print("========================END OF RECORD=======================\n")
