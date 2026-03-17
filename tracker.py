import requests

def get_crypto_price(coin_id):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": coin_id, "vs_currencies": "usd,idr"}
    response = requests.get(url, params=params)
    data = response.json()
    return data

def display_prices(coins):
    print("=" * 40)
    print("   CRYPTO PRICE TRACKER")
    print("=" * 40)
    for coin in coins:
        price = get_crypto_price(coin)
        usd = price[coin]["usd"]
        idr = price[coin]["idr"]
        print(f"{coin.upper():<12} | ${usd:>10,} | Rp{idr:>15,}")
    print("=" * 40)

coins = ["bitcoin", "ethereum", "solana"]
display_prices(coins)
```
