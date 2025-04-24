# Cálculo del consumo de agua por persona

consumo_mensual_vivienda = int(input(f"Introduzca el total de litros en un mes en una vivienda \n-> "))
cantidad_personas_vivienda = int(input(f"Introduzca la cantidad de personas que viven en la casa \n-> "))

consumo_mensual_por_persona = consumo_mensual_vivienda // cantidad_personas_vivienda
consumo_diario_por_persona = consumo_mensual_por_persona // 30

print(f"Consumo total de litros en un mes: {consumo_mensual_vivienda} litros \nTotal de personas en la vivienda {cantidad_personas_vivienda} personas")
print(f"Consumo mensual por persona: {consumo_mensual_por_persona} litros al mes \nConsumo diario por persona: {consumo_diario_por_persona} litros por persona")
