import requests

def get_crypto_price(coin_id):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": coin_id, "vs_currencies": "usd"}
    response = requests.get(url, params=params)
    return response.json()

coins = ["bitcoin", "ethereum"]
for coin in coins:
    price = get_crypto_price(coin)
    print(f"{coin.upper()}: {price}")
