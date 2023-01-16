import requests

base = "USD"
response = requests.get("https://api.exchangerate.host/latest?base=" + base)

if response.ok == True:
    data = response.json()
    rates = data["rates"]
    base = data["base"]
    date = data["date"]

    print("base: " + base)
    print("date: " + date)

  #  print(rates)
    for key in rates:
        print(key + " : ", rates[key])