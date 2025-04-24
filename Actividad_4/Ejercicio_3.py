# Notificación de velocidad peligrosa en carretera
# • Ingresar velocidad.
# • Si supera 120 km/h, mostrar “¡Reduzca la velocidad!”

velocidad = input(f" \nIntroduzca su velocidad en (km/h)\n-> ")

velocidad1, simbologia = velocidad.split(" ")

velocidad2 = int(velocidad1)
simbologia2 = str(simbologia)

if velocidad2 > 120:
    print(f"¡Reduzca la velocidad!\n ")
else:
    print(f"Siga su camino\n ")