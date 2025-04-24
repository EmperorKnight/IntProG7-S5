# Cálculo del consumo de combustible

precio_gasolina_super_litro = 47.81

distancia = int(input(f"Introduzca la distancia recorrida en kilometros \n-> "))
combustible_consumido = int(input(f"Introduzca la cantidad de combustible consumido en litros \n-> "))

rendimiento_kml = distancia // combustible_consumido
gasto_total_combustible = combustible_consumido * precio_gasolina_super_litro

print(f"Distancia recorrida: {distancia} km \nLitros de gasolina usados: {combustible_consumido}")
print(f"Precio por litro de gasolina (super): {precio_gasolina_super_litro}")
print(f"Rendimiento del vehiculo: {rendimiento_kml} km/l \nGasto total en combustible: C${gasto_total_combustible}")
