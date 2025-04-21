# Notificación de velocidad peligrosa en carretera
# • Ingresar velocidad.
# • Si supera 120 km/h, mostrar “¡Reduzca la velocidad!”

distancia_tiempo_rapido1 = ["km/h","km/m","km/s"]
distancia_tiempo_rapido2 = ["m/h","m/m","m/s"]

velocidad = int(input(f" \nIntroduzca su velocidad (solo el numero)\n-> "))
distancia_tiempo = input(f"Introduzca la distancia y el tiempo de su velocidad (distancia/tiempo)\n-> ")

if distancia_tiempo in distancia_tiempo_rapido1:
    if velocidad > 120:
        print(f"¡Reduzca la velocidad!\n ")
    else:
        print(f"Siga su camino\n ")

if distancia_tiempo in distancia_tiempo_rapido2:
    velocidad1 = velocidad * 1000
    if velocidad1 > 120000:
        print(f"¡Reduzca la velocidad!\n ")
    else:
        print(f"Siga su camino\n ")