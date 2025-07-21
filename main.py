import copy
from requests_html import HTMLSession

#Diccionario basico de datos del jugador
basicDataPlayer={
    "name": "",
    "actualPrice": 0,
    "pricePerDay": 0,
}
session = HTMLSession()

def leNormand():
    urlLeNormand = "https://www.analiticafantasy.com/jugadores/subidas-mercado-la-liga-fantasy/le-normand"
    priceBuy = 40123156
    return urlLeNormand, priceBuy


def extractDataPlayers():
    leNormandData = copy.deepcopy(basicDataPlayer)
    urlLeNormand, priceBuy = leNormand()
    fantasyPage = session.get(urlLeNormand)
   #leNormandData["name"] = fantasyPage.html.find(".info-right", first=True).text
    leNormandData["actualPrice"] = fantasyPage.html.find("p.MuiTypography-root.MuiTypography-body1.css-1n3xrwvj", first=False)
    print(leNormandData["name"])
    print(leNormandData["actualPrice"])


def main():
    extractDataPlayers()

if __name__ == "__main__":
    main()