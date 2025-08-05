from fetcher import extractDataPlayers
from constants import PLAYERS_LIST, PRICE_SELL, LOST_AND_WIN, PRICE_BUY
from time import sleep
from extractor import cleanInfo, dayWorthIt, totalResult, dayResult, daysToRentability


def analizeTeam():
    for a in PLAYERS_LIST:
        playerInfo = extractDataPlayers(a)
        if playerInfo["name"] in PRICE_SELL:
            result = PRICE_SELL[a] - PRICE_BUY[a]
            print("")
            print("{} ya ha sido vendido con {} de {}".format(playerInfo["name"], "beneficios" if result >= 0 else "perdidas", result))
            print("")
            print("")
            sleep(1)
            LOST_AND_WIN.append(result)
        else:
            cleanInfo(playerInfo)
            sleep(1)
    totalResult()
    dayResult()