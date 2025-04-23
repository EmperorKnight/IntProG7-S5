# Notificación de velocidad peligrosa en carretera
# • Ingresar velocidad.
# • Si supera 120 km/h, mostrar “¡Reduzca la velocidad!”

velocidad = input(f" \nIntroduzca su velocidad en (km/h)\n-> ")
velocidad = int()

if velocidad > 120:
    print(f"¡Reduzca la velocidad!\n ")
else:
    print(f"Siga su camino\n ")