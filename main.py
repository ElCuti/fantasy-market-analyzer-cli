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
    urlLeNormand = "https://www.jornadaperfecta.com/jugador-min/raphinha?hideHeader=true"
    priceBuy = 40123156
    return urlLeNormand, priceBuy


def extractDataPlayers():
    leNormandData = copy.deepcopy(basicDataPlayer)
    urlLeNormand, priceBuy = leNormand()
    fantasyPage = session.get(urlLeNormand)
    #leNormandData["name"] = fantasyPage.html.find(".info-right", first=True).text
    webPage1 = fantasyPage.html.find(" div.column-jp.full-width.center.p-8.card.fixed-prices.market-container > div:nth-child(1) > div.row-jp > div ", first=False)[1].text
    leNormandData["actualPrice"] = fantasyPage.html.find(".MuiTypography-root.MuiTypography-body1", first=False)[1].text
    print(leNormandData["name"])
    print(webPage1)


def main():
    extractDataPlayers()

if __name__ == "__main__":
    main()