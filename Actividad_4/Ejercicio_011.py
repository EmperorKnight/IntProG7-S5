# Determinar si hay saldo suficiente para una compra
# • Ingresar precio del producto y saldo disponible.
# • Si el saldo alcanza, permitir la compra.
# • Si no, mostrar “Saldo insuficiente”.

cantidad_producto = int(input(f"Introduzca la cantidad de productos \n-> "))
precio_producto = float(input(f"Introduzca el precio de los productos \n-> "))
p = 1

while p < cantidad_producto:
    precio_producto1 = float(input("-> "))
    precio_producto = precio_producto1 + precio_producto
    p += 1

saldo = float(input(f"Introduzca el saldo que dispone \n-> "))

if precio_producto > saldo:
    print("Saldo insuficiente")
else:
    print("Compra exitosa")
