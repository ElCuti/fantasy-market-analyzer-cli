import copy
from requests_html import HTMLSession
from constants import BASIC_DATA_PLAYER, PRICE_BUY

session = HTMLSession()

def fetchPlayerPrice(playerID):
    URLPLAYER = "https://www.jornadaperfecta.com/jugador/"+ playerID +"?hideHeader=true"
    fantasyPage = session.get(URLPLAYER)
    actualPrice = fantasyPage.html.find(
        " div.column-jp.full-width.center.p-8.card.fixed-prices.market-container > div:nth-child(1) > div.row-jp > div ",
        first=False)[1].text
    priceChange = fantasyPage.html.find(
        ".player-page div.column-mobile-jp.center.mt-12 div.ai-top div.row-jp.space-between:nth-child(1) div.column-jp.center.card:nth-child(2) div.row-jp span:nth-child(2)",
        first=True).text
    typeChange = fantasyPage.html.find(
        ".player-page div.column-mobile-jp.center.mt-12 div.ai-top div.row-jp.space-between:nth-child(1) div.column-jp.center.card:nth-child(2) div.row-jp span:nth-child(1)",
        first=True).text
    return actualPrice, priceChange, typeChange

def extractDataPlayers(playerID):
    playerData = copy.deepcopy(BASIC_DATA_PLAYER)
    actualPrice, incrementPrice, typeChange = fetchPlayerPrice(playerID)
    playerData["actualPrice"] = int(actualPrice.replace(".", "").replace("€", ""))
    playerData["pricePerDay"] = int(incrementPrice.replace(".", "").replace("€", ""))
    playerData["priceToBuy"] = PRICE_BUY[playerID]
    playerData["name"] = playerID
    playerData["typeChange"] = typeChange
    return playerData
