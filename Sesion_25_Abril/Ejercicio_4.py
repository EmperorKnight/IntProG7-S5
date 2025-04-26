# Ingresa tres lados de un triángulo y determina si es equilátero, isósceles o escaleno.

lados1 = float(input(f"Introduzca la longitud de un lado del triangulo \n-> "))
lados2 = float(input(f"Introduzca la longitud de un lado del triangulo \n-> "))
lados3 = float(input(f"Introduzca la longitud de un lado del triangulo \n-> "))

if lados1 == lados2 == lados3:
    print("Es un triangulo equilatero")
elif lados1 == lados2 or lados2 == lados3 or lados1 == lados3:
    print("Es un triangulo isosceles")
elif lados1 != lados2 != lados3:
    print("Es un triangulo escaleno")