from fetcher import extractDataPlayers
from constants import PLAYERS_LIST, PRICE_SELL, LOST_AND_WIN, PRICE_BUY
from time import sleep
from extractor import cleanInfo, totalResult, dayResult


def analizeTeam():
    """
    Función troncal encargada de ejecutar todo el programa posterior al main, recorre a todos los jugadores y te dice si el jugador ya ha sido vendido
    """
    for a in PLAYERS_LIST: #Recorrer todos los jugadores con el formato de la URL de la página
        playerInfo = extractDataPlayers(a) #Uso de función para extraer toda la información de la página y guardarla en nuestro diccionario básico
        if playerInfo["name"] in PRICE_SELL: #Si el jugador ya está vendido
            result = PRICE_SELL[a] - PRICE_BUY[a] # comprobamos si ha dejado beneficios o perdidas
            print("")
            print("{} ya ha sido vendido con {} de {}".format(playerInfo["name"], "beneficios" if result >= 0 else "perdidas", result)) #Y se lo enseñamos al user
            print("")
            print("")
            sleep(1)
            LOST_AND_WIN.append(result) #Guardamos el resultado en la lista
        else: #Si el jugador sigue estando en nuestra plantilla
            cleanInfo(playerInfo)
            sleep(1)
    totalResult()
    dayResult()