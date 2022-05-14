from cgitb import text
from decimal import ConversionSyntax
from bs4 import BeautifulSoup 
import requests 
import time
nazev_coinu = "coins"
cena_list = {}

def main():
    uvod()
    coiny = input('Vypiš měny, které máš nakoupené, odděl je mezerou: ')
    pocet = input("Napiš kolik jednotek daných měn máš: ")
    coin_list = coiny.split()
    count_list = pocet.split()
    # Udela z nazvu coinu promenne
    for i in range(len(coin_list)):
        coin_list[i] = str(coin_list[i])
        print("Název:", coin_list[i])
        count_list[i] = int(count_list[i])
        print("Počet:", count_list[i])
        # udelej z kazdeho prvku pole coinu promennou
        nazev_coinu = locals()
        nazev_coinu.__setitem__(coin_list[i], "5")
        # Odskoci zjistit cenu coinu
        cena = vrat_cenu(nazev_coinu)
        # Prida cenu do pole rovnou vynasobenou poctem jednotek daneho coinu
        cena_list.append(cena * count_list[i])
        print("Cena", nazev_coinu ,"je", cena ,"$")
        print("Hodnota tvých", nazev_coinu ,"je", cena * count_list[i] ,"$")
    # Secte vsechny ceny v poli
    celkem = sum(cena_list)
    print("Celkova cena portfolia:", celkem)
    print("\n")
    print("MWMWMWMWMWMWMWMWMWMWMWMWMWMWMMWMWMWMWWMMWMWMWMWMWMWMWWMWMWMWM")

# Ziska aktualni cenu coinu z Google
def vrat_cenu(nazev_coinu):
    # Získej URL, odkud se bude tahat aktuální cena
    url = "https://www.google.com/search?q="+nazev_coinu+"+price"
    # Posle pozadavek na stranku
    HTML = requests.get(url)
    # Vyhleda v HTML kodu cenu
    soup = BeautifulSoup(HTML.text, 'html.parser')
    cena = soup.find("div", attrs={'class':'BNeawe iBp4i AP7Wnd'}).find("div", attrs={'class':'BNeawe iBp4i AP7Wnd'}).text
    return cena

def uvod():
    print(" ".center(24," "))
    print("Pocitadlo coinu".center(24," "))
