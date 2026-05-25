# import api

import requests

url = requests.get("https://isro.vercel.app/api/spacecrafts")
data = url.json()

print(data)

# type
print(type(data))

# keys
print(data.keys())
print(len(data["spacecrafts"]))

# accessing data aryabhata
print(data["spacecrafts"][0]["name"])

#last name
print(data["spacecrafts"][-1]["name"])

# multiple data
# SR NO:-----    NAME:-----
# for loop (2 ways)
# 1 way(accessing data directly)
for i in data["spacecrafts"]:
    print("SR NO:",i["id"]," | NAME:",i["name"])

# 2 way(by range)
for i in range(len(data["spacecrafts"])):
    print("SR NO:",i+1," | NAME:",data["spacecrafts"][i]["name"])
