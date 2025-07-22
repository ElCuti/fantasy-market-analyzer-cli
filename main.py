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
    urlLeNormand = "https://www.jornadaperfecta.com/jugador/le-normand?hideHeader=true"
    priceBuy = 40123156
    return urlLeNormand, priceBuy

def fechPlayerPrice(playerID):
    URLPLAYER = "https://www.jornadaperfecta.com/jugador/"+ playerID +"?hideHeader=true"
    fantasyPage = session.get(URLPLAYER)
    actualPrice = fantasyPage.html.find(
        " div.column-jp.full-width.center.p-8.card.fixed-prices.market-container > div:nth-child(1) > div.row-jp > div ",
        first=False)[1].text
    priceChange = fantasyPage.html.find(
        ".player-page div.column-mobile-jp.center.mt-12 div.ai-top div.row-jp.space-between:nth-child(1) div.column-jp.center.card:nth-child(2) div.row-jp span:nth-child(2)",
        first=True).text
    return actualPrice, priceChange

def extractDataPlayers():
    leNormandData = copy.deepcopy(basicDataPlayer)
    leNormand = fechPlayerPrice("le-normand")
    davidSoria = fechPlayerPrice("david-soria")



def main():
    extractDataPlayers()

if __name__ == "__main__":
    main()