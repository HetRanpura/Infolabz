import requests

search = input("Enter TV show name:")
url = requests.get(f"http://api.tvmaze.com/search/shows?q={search}")

data = url.json()

print(data)

print(type(data))

# keys
print(data[0].keys())

# multiple names
for i in data:
    print(i["show"]["name"])

# searching
for i in data:
    if "english" in i["show"]["language"].lower():
        print(i["show"]["name"])

# count
count = 0
for i in data:
    if "scripted" in i["show"]["type"].lower():
        count += 1
print(count)

# startswith
for i in data:
    if i["show"]["name"].startswith("S"):
        print(i["show"]["name"])

# endswith
for i in data:
    if i["show"]["name"].endswith("r"):
        print(i["show"]["name"])
