# Cálculo de interés compuesto

capital_inicial = float(input(f"Introduzca el monto inicial \n-> "))
tasa_interes_anual = int(input(f"Introduzca la tasa de interes de interes anual \n-> % "))
cantidad_años = int(input(f"Introduzca la cantidad de años \n-> "))

tasa_decimal = tasa_interes_anual / 100
monto_final = ((1 + tasa_decimal)**cantidad_años) * capital_inicial
interes_ganado = monto_final - capital_inicial

print(f"Capital inicial: C${capital_inicial:.0f} \nTasa de interes anual: {tasa_interes_anual}%")
print(f"Cantidad de años: {cantidad_años} años \nMonto final: C${monto_final:.0f} \nInteres ganado: {interes_ganado:.0f}%")

