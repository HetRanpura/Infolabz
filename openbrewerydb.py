import requests

url = requests.get("https://api.openbrewerydb.org/v1/breweries")
data = url.json()

print(len(data))

for i in data:
    print("===========BREWERY INFORMATION REPORT===========")
    print("Brewery Name:",i["name"])
    print("Brewery Type:",i["brewery_type"])
    print("City:",i["city"])
    print("Country:",i["country"])
    print("Website URL:",i["website_url"])
    print("=================END OF RECORD==================\n")
