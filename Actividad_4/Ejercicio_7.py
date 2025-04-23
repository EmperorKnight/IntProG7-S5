# Cálculo de propina según satisfacción
# • Ingresar monto total y nivel de satisfacción (buena/mala).
# • Si es buena, calcular 15% propina; si es mala, 5%.
# • Mostrar total a pagar.

satisfacción_positiva = ["buena","bueno","excelente","extraordinario"]
satisfacción_negativa = ["mala","bueno","horrible"]

propina_buena = 15/100
propina_mala = 5/100

monto_total = float(input(f"Introduzca el monto total a pagar \n-> "))
nivel_satisfacción = input(f"Introduzca el nivel de satisfacción que experimento (bueno o malo) \n-> ")

nivel_satisfacción.lower()

if nivel_satisfacción.lower() in satisfacción_positiva:
    total_pagar = monto_total + (monto_total * propina_buena)
    print(f"El total a pagar es de C${total_pagar:.0f}")
elif nivel_satisfacción.lower() in satisfacción_negativa:
    total_pagar = monto_total + (monto_total * propina_mala)
    print(f"El total a pagar es de C${total_pagar:.0f}")
