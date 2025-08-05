import copy
from requests_html import HTMLSession
from constants import BASIC_DATA_PLAYER, PRICE_BUY

session = HTMLSession() #Iniciamos la sesión

def fetchPlayerPrice(playerID):
    """
    Función encargada de extraer los parametros de la página web "jornadaperfecta"
    :param playerID: Nombre del jugador adaptada para la URL de la página (Le Normand → le-normand)
    :return: Precio actual del jugador, variación diaria (Siempre +) y tipo de variación (- o +)
    """
    URLPLAYER = "https://www.jornadaperfecta.com/jugador/"+ playerID +"?hideHeader=true" #Ocultamos el header de la página para reducir modificaciones de formato
    fantasyPage = session.get(URLPLAYER)

    actualPrice = fantasyPage.html.find(
        " div.column-jp.full-width.center.p-8.card.fixed-prices.market-container > div:nth-child(1) > div.row-jp > div ",
        first=False)[1].text #Precio actual

    priceChange = fantasyPage.html.find(
        ".player-page div.column-mobile-jp.center.mt-12 div.ai-top div.row-jp.space-between:nth-child(1) div.column-jp.center.card:nth-child(2) div.row-jp span:nth-child(2)",
        first=True).text #Cambio de precio

    typeChange = fantasyPage.html.find(
        ".player-page div.column-mobile-jp.center.mt-12 div.ai-top div.row-jp.space-between:nth-child(1) div.column-jp.center.card:nth-child(2) div.row-jp span:nth-child(1)",
        first=True).text #Tipo de cambio
    return actualPrice, priceChange, typeChange

def extractDataPlayers(playerID):
    """
    Función encargada de adaptar la información extraída de la página web al diccionario básico
    :param playerID: Nombre del jugador adaptada para la URL de la página (Le Normand → le-normand)
    :return: Diccionario con la información del jugador
    """
    playerData = copy.deepcopy(BASIC_DATA_PLAYER) #Hacemos deepcopy del diccionario básico
    actualPrice, incrementPrice, typeChange = fetchPlayerPrice(playerID)
    playerData["actualPrice"] = int(actualPrice.replace(".", "").replace("€", "")) #Quitamos los puntos y símbolos para transformarlo en integers
    playerData["pricePerDay"] = int(incrementPrice.replace(".", "").replace("€", ""))
    playerData["priceToBuy"] = PRICE_BUY[playerID] #Extraemos el precio al que compramos el jugador
    playerData["name"] = playerID
    playerData["typeChange"] = typeChange
    return playerData
