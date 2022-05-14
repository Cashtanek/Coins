from array import array

def ETH_BTC():
    coiny = str(input("Zadej zkratku měny, kterou máš nakoupenou: "))
    portfolio = int(input("Zadej velikost portfolia v jednotkach měn: "))

    if coiny == "btc":
        usd = portfolio * 30000
        predikce = usd / 100 * 60
        print("Hodnota portfolia je", usd ,"$.")
        print("Za týden budeš mít", predikce ,"$.")
    elif coiny == "eth":
        usd = portfolio * 2100
        predikce = usd / 100 * 60
        print("Hodnota portfolia je", usd ,"$.")
        print("Za týden budeš mít", predikce ,"$.")
    else: print ("Program umí pracovat pouze s ETH nebo BTC.")

