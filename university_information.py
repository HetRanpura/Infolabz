import requests

url = requests.get("http://universities.hipolabs.com/search?country=India")
data = url.json()

# number of keys
print(len(data[0].keys()))

# complete list
print(data)

# type of keys
print(type(data[0]))

# accessing data
for i in data:
    print("=============UNIVERSITY-INFORMATION-REPORT=============")
    print("Institution Name:", i["name"])
    print("State / Province:", i["state-province"])
    print("Primary Academic Domain:", i["domains"])
    print("Official Website:", i["web_pages"])
    print("Institution Identifier", i["alpha_two_code"])
    print("===========END UNIVERSITY-INFORMATION-REPORT===========\n")