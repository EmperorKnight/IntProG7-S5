# Control de inventario de un producto

inventario_inicial = int(input(f"Introduzca el inventario inicial \n-> "))
inventario_vendido = int(input(f"Introduzca la cantidad de inventario vendido \n-> "))
inventario_recibido = int(input(f"Introduzca la cantidad de inventario recibido \n-> "))

inventario_actual = (inventario_inicial + inventario_recibido) - inventario_vendido

print(f"Cantidad de inventario vendido: {inventario_vendido} \nCantidad de inventario recibido: {inventario_recibido}")
print(f"Inventario actual: {inventario_actual}")