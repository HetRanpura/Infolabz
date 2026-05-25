import requests

url = requests.get("https://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?format=json")

data = url.json()

# no. of keys
print(len(data[0].keys()))

# complete list
print(data[1][0]["country"]["value"])

# accessing datas
for i in data[1]:
    print("==========POPULATION_INDICATOR_REPORT==========")
    print("Country Name:",i["country"]["value"])
    print("Country Code:",i["countryiso3code"])
    print("Indicator Name:",i["indicator"]["value"])
    print("Reference Year:",i["date"])
    print("Recorded Population:",i["value"])
    print("==================END REPORT====================\n")