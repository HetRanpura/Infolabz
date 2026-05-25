import requests

url=requests.get("https://api.coingecko.com/api/v3/coins/bitcoin")
data=url.json()

# print(data)
# print(data.keys())
# inr price
print(data["market_data"]["current_price"]["inr"])

print(data["market_data"]["price_change_24h_in_currency"]["inr"])