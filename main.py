import copy
from time import sleep

from requests_html import HTMLSession

#Diccionario basico de datos del jugador
basicDataPlayer={
    "name": "",
    "actualPrice": 0,
    "pricePerDay": 0,
    "priceToBuy": 0,
    "typeChange": "",
}

priceBuy = {
    "le-normand": 40123156,
    "david-soria": 21012345,
    "exposito": 3661823,
    "sannadi": 1850123,
    "lukebakio": 59123456,
    "samu-costa": 4370119,
    "arda-guler": 58512345,
    "giuliano-simeone": 23486593,
    "johnny": 19217330,
}

listPlayer = ["le-normand", "david-soria", "exposito", "sannadi", "lukebakio", "samu-costa", "arda-guler", "giuliano-simeone", "johnny"]

lostAndWin= []

session = HTMLSession()

def fechPlayerPrice(playerID):
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
    playerData = copy.deepcopy(basicDataPlayer)
    actualPrice, incrementPrice, typeChange = fechPlayerPrice(playerID)
    playerData["actualPrice"] = int(actualPrice.replace(".", "").replace("€", ""))
    playerData["pricePerDay"] = int(incrementPrice.replace(".", "").replace("€", ""))
    playerData["priceToBuy"] = priceBuy[playerID]
    playerData["name"] = playerID
    playerData["typeChange"] = typeChange
    return playerData

def analizeTeam():
    for a in listPlayer:
        playerInfo = extractDataPlayers(a)
        cleanInfo(playerInfo)
    totalResult()

def dayWorthIt(playerInfo):
    toPay = playerInfo["priceToBuy"] - playerInfo["actualPrice"]
    daysToWorthIt = round(toPay/playerInfo["pricePerDay"], 0)
    return daysToWorthIt

def cleanInfo(playerInfo):
    result = playerInfo["actualPrice"] - playerInfo["priceToBuy"]
    lostAndWin.append(result)
    result = ("{:,}".format(result))
    result = result.replace(",", ".")
    x = ("""Jugador: {}
    Precio de compra: {:,}
    Precio Actual: {:,}
    Has {}: {}
    Ha {} hoy: {:,}""".format(playerInfo["name"], playerInfo["priceToBuy"], playerInfo["actualPrice"], "ganado" if playerInfo["actualPrice"]>=playerInfo["priceToBuy"] else "perdido", result, "subido" if playerInfo["typeChange"] == "+" else "bajado", playerInfo["pricePerDay"]))
    xy = x.replace(",",".")

    print(xy)
    daysToWorthIt = dayWorthIt(playerInfo)
    if daysToWorthIt > 0 and playerInfo["typeChange"] == "+":
        print("- Para recuperar la inversión por este jugador deben de pasar {} dias con la rentabilidad de hoy".format(daysToWorthIt))
    elif daysToWorthIt > 0 and playerInfo["typeChange"] != "+":
        print("- Este jugador no esta ganando valor y esta por debajo del precio de compra, diferencia entre lo que pagaste y lo que vale: {}". format(result))
    else:
        print("- ¡Este jugador ya vale mas de lo que pagaste por el! Beneficio: {}".format(result))

def totalResult():
    profitPlayer1 = 0
    for profitPlayer in lostAndWin:
        profitPlayer1 += profitPlayer
    x = ("Tu inversión actual lleva un rendimiento {} de {:,}€".format("positivo" if profitPlayer1>=0 else "negativo", profitPlayer1))
    xy = x.replace(",", ".")
    print(xy)

def main():
    analizeTeam()
    input("Pulse enter para salir")

if __name__ == "__main__":
    main()