import requests

currency = "pln" 
coinsList = None

def getCoinsList():
    global coinsList
    # [{'id': '01coin', 'symbol': 'zoc', 'name': '01coin', 'platforms': {}},...]
    response = requests.get("https://api.coingecko.com/api/v3/coins/list?include_platform=true")
    if response.ok == True:
        print("Response ok")
        data = response.json()
        print(data[0])
        print(len(data))
        print("Ilość kryptowalut: " + str(len(data)))
        coinsList = data

def findCoinBySymbol(symbol):
    symbol = symbol.lower().strip()
    for coin in coinsList:
        if coin["symbol"] == symbol:
            return coin
    else:
        return None


def getCoinLastMarketData(coinId):
    #{'bitcoin': {'pln': 100538, 'pln_market_cap': 1939423661133.2864, 'pln_24h_vol': 167237123252.81226, 'pln_24h_change': -1.5981850085935088, 'last_updated_at': 1675100279}}
    response = requests.get("https://api.coingecko.com/api/v3/simple/price?ids="+coinId+"&vs_currencies="+currency+"&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true")
    if response.ok:
        data = response.json()
        return data 
    else:
        return None

def getCoinPriceInCurrency(coinId, currency):
    currency = currency.lower().strip()
    marketData = getCoinLastMarketData(coinId)
    return marketData[coinId][currency]

getCoinsList()

btcdata = findCoinBySymbol("btc")

print(btcdata)

marketData = getCoinLastMarketData(btcdata["id"])
print("market data: ", marketData)

coinPrice = getCoinPriceInCurrency(btcdata["id"], currency)
print("Coin price in " , currency, coinPrice)

print("\nWitamy w crypto exchange")

while True:
    cryptoSymbolToBuy = input("Wybierz symbol crypto do kupienia np btc lub exit by zakończyć: ")
    if cryptoSymbolToBuy == "exit": break

    coinData = findCoinBySymbol(cryptoSymbolToBuy)
    if coinData == None:
        print("Nie ma takiej kryptowaluty")
        continue

    coinPrice = getCoinPriceInCurrency(coinData["id"], currency)
    print("Cena " + str(coinData["id"]), coinPrice, currency)

    moneyToBuyCrypto = float(input("Ile chcesz przeznaczyć na zakup: "))
    boughtCrypto = moneyToBuyCrypto / coinPrice

    print("\nGratulacje kupiłeś " +str(boughtCrypto) + " " + cryptoSymbolToBuy)
