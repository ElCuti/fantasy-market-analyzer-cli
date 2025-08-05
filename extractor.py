from constants import  LOST_AND_WIN, LOST_AND_WIN_DAY

def dayWorthIt(playerInfo):
    """
    Función encargada de calcular los días para recuperar la inversión por un jugador.
    :param playerInfo: Diccionario con la información del jugador
    :return: Días para rentabilizar a un jugador
    """
    toPay = playerInfo["priceToBuy"] - playerInfo["actualPrice"] #toPay = Precio de compra - Precio actual
    daysToWorthIt = round(toPay/playerInfo["pricePerDay"], 0) #daysToWorthIt =(Redondeado)= toPay / variación de precio diaria
    return daysToWorthIt

def formatBasicInfo(playerInfo):
    """
    Funcion encargada de printear la información del jugador de forma clara para el usuario.
    :param playerInfo: Diccionario con la información del jugador
    :return: Texto claro y adaptado al usuario con la información del jugador
    """
    result = playerInfo["actualPrice"] - playerInfo["priceToBuy"] #Diferencia de precio actual con lo pagado por el jugador
    formatted = ("{:,}".format(result)).replace(",", ".") #Aplicar separador de miles para mayor simpleza (3000000 → 3.000.000)
    return ("Jugador: {}\n"
            "Precio de compra: {:,}\n"
            "Precio Actual: {:,}\n"
            "Has {}: {}\n"
            "Ha {} hoy: {:,}").format(
                playerInfo["name"],
                playerInfo["priceToBuy"],
                playerInfo["actualPrice"],
                "ganado" if playerInfo["actualPrice"] >= playerInfo["priceToBuy"] else "perdido",
                formatted,
                "subido" if playerInfo["typeChange"] == "+" else "bajado",
                playerInfo["pricePerDay"]
            ).replace(",", ".")

def formatSummary(playerInfo):
    """
    Función encargada de decirle al usuario si su jugador esta: generando ingresos, recuperando inversion o generando perdidas.
    :param playerInfo: Diccionario con la información del jugador
    :return: Texto claro y adaptado al usuario con el estado actual del jugador
    """
    daysToWorthIt = dayWorthIt(playerInfo) #Usamos la función para extraer los días necesarios para rentabilizar la inversión
    diff = playerInfo["actualPrice"] - playerInfo["priceToBuy"]
    formatted = ("{:,}".format(diff)).replace(",", ".") #Aplicar separador de miles para mayor simpleza (3000000 → 3.000.000)

    if playerInfo["priceToBuy"] > playerInfo["actualPrice"] and playerInfo["typeChange"] == "+": #Si el jugador vale menos de lo que pagaste y su valor ha subido hoy
        return "- Para recuperar la inversión por este jugador deben de pasar {} dias con la rentabilidad de hoy".format(daysToWorthIt)

    elif playerInfo["priceToBuy"] > playerInfo["actualPrice"]: #Si el jugador vale menos de lo que pagaste y su valor ha bajado hoy
        return "- Este jugador no esta ganando valor y esta por debajo del precio de compra, diferencia entre lo que pagaste y lo que vale: {}".format(formatted)

    else: #Si el jugador vale más de lo que pagaste
        return "- ¡Este jugador ya vale mas de lo que pagaste por el! Beneficio: {}".format(formatted)

def cleanInfo(playerInfo):
    """
    Función encargada de almacenar el beneficio o perdida de un jugador en la lista LOST_AND_WIN / LOST_AND_WIN_DAY y de enseñar
    al usuario la información de cada jugador de forma clara
    :param playerInfo: Diccionario con la información del jugador
    """
    result = playerInfo["actualPrice"] - playerInfo["priceToBuy"] #Diferencia entre lo que vale y lo que pagaste
    LOST_AND_WIN.append(result) #Guardar la diferencia en la lista

    if playerInfo["typeChange"] == "+":                      #Si el jugador está subiendo de precio
        LOST_AND_WIN_DAY.append(playerInfo["pricePerDay"])   #Añadimos la variación de ese día

    elif playerInfo["typeChange"] != "+":                       #Si el jugador está bajando de precio
        LOST_AND_WIN_DAY.append(playerInfo["pricePerDay"] * -1) #Transformamos el número en negativo y lo añadimos

    # Imprimimos la info básica y el resumen separados
    print(formatBasicInfo(playerInfo))
    print(formatSummary(playerInfo))
    print()


def totalResult():
    """
    Función encargada de enseñar al usuario los resultados de su inversión en total
    :return: Resultado de su inversión en total (+/-)
    """
    profitPlayer1 = 0
    for profitPlayer in LOST_AND_WIN: #Extraemos los resultados de todos los jugadores
        profitPlayer1 += profitPlayer # y los sumamos
    x = ("Tu inversión actual lleva un rendimiento {} de {:,}€".format("positivo" if profitPlayer1>=0 else "negativo", profitPlayer1))
    xy = x.replace(",", ".") #Escribimos el mensaje para el usuario usando el separador por mil (3000000 → 3.000.000)
    print(xy)
    return profitPlayer1

def dayResult():
    """
    Función encargada de enseñar al usuario los resultados de su inversión DIARIA
    :return: Resultado de su inversión DIARIA (+/-)
    """
    profitDay1= 0
    for profitDay in LOST_AND_WIN_DAY: #Extraemos los resultados diarios de todos los jugadores
        profitDay1 += profitDay        # y los sumamos
    x = ("Tu inversión HOY lleva un rendimiento {} de {:,}€".format("positivo" if profitDay1 >= 0 else "negativo", profitDay1))
    xy = x.replace(",", ".") #Escribimos el mensaje para el usuario usando el separador por mil (3000000 → 3.000.000)
    print(xy)
    return profitDay1

def daysToRentability(profitPlayer1, profitDay1):
    """
    Función encargada de calcular los días para recuperar la inversión TOTAL con el beneficio generado ese día
    :param profitPlayer1: Resultado de su inversión en total (+/-)
    :param profitDay1: Resultado de su inversión DIARIA (+/-)
    :return:
    """
    profitPlayer2= 0
    if profitPlayer1 <0:                    #Si el beneficio es negativo lo transformamos en positivo para expresar
        profitPlayer2= (profitPlayer1 * -1) # los días en positivo (Así evitamos "Le quedan -2 días para recuperar la inversión")
    daysRentability = round(profitPlayer2/profitDay1, 0) #daysRentability =(Redondeado)= Beneficio (en positivo) / variación de precio diaria

    if profitPlayer1 >= 0: #Si el valor de tu inversión es mayor al invertido
        print("Tu inversión ya ha sido rentabilizada, tus ganancias son de {:,}".format(profitPlayer1))

    elif profitDay1 > 0 > profitPlayer1: #Si el valor de la inversión es menor al invertido y tienes beneficios diarios
        print("Para rentabilizar tu inversión en total deben de pasar {:,} dias con tu rentabilidad diaria".format(daysRentability))

    else: #Si el valor de la inversión es menor al invertido y tienes perdidas diarias
        print("¡Tu inversión total esta en negativo y tambien estas teniendo perdidas diariamente! Tus perdidas son de: {:,} y diariamente pierdes: {:,}".format(profitPlayer1, profitDay1))