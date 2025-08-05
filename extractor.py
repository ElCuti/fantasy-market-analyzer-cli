from constants import  LOST_AND_WIN, LOST_AND_WIN_DAY

def dayWorthIt(playerInfo):
    toPay = playerInfo["priceToBuy"] - playerInfo["actualPrice"]
    daysToWorthIt = round(toPay/playerInfo["pricePerDay"], 0)
    return daysToWorthIt

def cleanInfo(playerInfo):
    result = playerInfo["actualPrice"] - playerInfo["priceToBuy"]
    LOST_AND_WIN.append(result)
    if playerInfo["typeChange"] == "+":
        LOST_AND_WIN_DAY.append(playerInfo["pricePerDay"])
    elif playerInfo["typeChange"] != "+":
        LOST_AND_WIN_DAY.append(playerInfo["pricePerDay"]*-1)
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
    if  playerInfo["priceToBuy"] > playerInfo["actualPrice"] and playerInfo["typeChange"] == "+":
        print("- Para recuperar la inversión por este jugador deben de pasar {} dias con la rentabilidad de hoy".format(daysToWorthIt))
    elif playerInfo["priceToBuy"] > playerInfo["actualPrice"] != "+":
        print("- Este jugador no esta ganando valor y esta por debajo del precio de compra, diferencia entre lo que pagaste y lo que vale: {}". format(result))
    else:
        print("- ¡Este jugador ya vale mas de lo que pagaste por el! Beneficio: {}".format(result))

    print("")
    print("")

def totalResult():
    profitPlayer1 = 0
    for profitPlayer in LOST_AND_WIN:
        profitPlayer1 += profitPlayer
    x = ("Tu inversión actual lleva un rendimiento {} de {:,}€".format("positivo" if profitPlayer1>=0 else "negativo", profitPlayer1))
    xy = x.replace(",", ".")
    print(xy)
    return profitPlayer1

def dayResult():
    profitDay1= 0
    for profitDay in LOST_AND_WIN_DAY:
        profitDay1 += profitDay
    x = ("Tu inversión HOY lleva un rendimiento {} de {:,}€".format("positivo" if profitDay1 >= 0 else "negativo", profitDay1))
    xy = x.replace(",", ".")
    print(xy)
    return profitDay1

def daysToRentability(profitPlayer1, profitDay1):
    if profitPlayer1 <0:
        profitPlayer2= (profitPlayer1 * -1)
    daysRentability = round(profitPlayer2/profitDay1, 0)
    if profitPlayer1 >= 0:
        print("Tu inversión ya ha sido rentabilizada, tus ganancias son de {:,}".format(profitPlayer1))
    elif profitDay1 > 0 and profitPlayer1 < 0:
        print("Para rentabilizar tu inversión en total deben de pasar {:,} dias con tu rentabilidad diaria".format(daysRentability))
    else:
        print("¡Tu inversión total esta en negativo y tambien estas teniendo perdidas diariamente! Tus perdidas son de: {:,} y diariamente pierdes: {:,}".format(profitPlayer1, profitDay1))