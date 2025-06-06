#Punto 1

bandera = True
num = 0

while bandera:
    print(num)
    num += 1
    if num >= 101:
        bandera = False

# Punto 2

num = input("Ingrese un número entero: ")

if num.startswith('-'):
    num_entero = int(num) * -1
else:
    num_entero = int(num)


contador = 0


if num_entero == 0:
    contador = 1
else:
    while num_entero > 0:
        num_entero = num_entero // 10  
        contador += 1

print(f"La cantidad de dígitos en su número es de {contador}")

# Punto 3

#declaracion de variables y entrada de datos
num1 = int(input("ingrese un numero: "))
num2 = int(input("ingrese un segundo numero: "))
suma = 0

# lógica para sumar los números entre num1 y num2
if num1 < num2:
    for i in range(num1 + 1, num2):
        suma = suma + i
else:
    for i in range(num2 + 1, num1):
        suma = suma + i

# salida de datos
print(f"La suma de los números entre {num1} y {num2} es: {suma}")

# Punto 4

# Definicion de variables
bandera = False
num = int(input("Ingrese un número entero o ingrese 0 para salir en cualquier momento: "))
cont_final = num

# Verifica si el número ingresado es diferente de cero para iniciar el bucle
if num != 0:
    bandera = True

# Bucle para seguir ingresando números hasta que se ingrese 0
while bandera:
        num_var = int(input("ingrese otro número entero: "))
        cont_final = cont_final + num_var
        if num_var == 0:
            bandera = False

# Verifica si se ingresó al menos un número
if num != 0:
    print(f"el total acumulado de todos los numeros que ingreso es de: {cont_final}")

# Punto 5

import random

num = random.randint(0, 9)
bandera = True
contador = 0

eleccion = int(input("ingrese un numero entre 0 y 9: "))

while bandera:
    if eleccion == num:
        contador += 1
        print(f"Acertaste! la cantidad de intentos fueron {contador} intentos")
        bandera = False
    else:
        contador += 1
        eleccion = int(input("Incorrecto! ingrese otro numero: "))

# Punto 6

# Imprimir los números del 100 al 0, de 2 en 2
for i in range(100, 0, -2):
    print(i)

# Punto 7

#ingreso de un numero entero positivo
num_ini = int(input("ingrese un numero entero positivo: "))

# Verifica si el número ingresado es positivo
# y calcula la suma de los números desde 0 hasta el número ingresado
if num_ini >= 0:
    num_fin = 0
    for i in range(0, num_ini + 1):
        num_fin += i
    print(f"el total es: {num_fin}")
else:
    print("error, numero no valido")

# Punto 8

# Solicita al usuario ingresar 4 números enteros y cuenta cuántos son negativos, positivos, pares e impares.
for i in range(100):
    num = int(input("Ingrese un número entero: "))

    if num < 0:
        negativo += 1
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1
    else:
        positivo += 1
        if num % 2 == 0:
            pares += 1
        else:
            impares += 1

# Muestra el conteo de números negativos, positivos, pares e impares.
print(f"Cantidad de números negativos: {negativo}")
print(f"Cantidad de números positivos: {positivo}")
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")

# Punto 9

#ingreso del primer número entero positivo
num = int(input("Ingrese un número entero: "))

#inicializa la variable para la media
num_med = num
media = 0

# Verifica si el número ingresado es positivo
if num > 0:
    # Solicita al usuario ingresar 99 números enteros adicionales
    for i in range(99):
        num = int(input("Ingrese otro número entero: "))
        num_med += num
    media = num_med / 100 # Calcula la media dividiendo la suma total por 100
    # Muestra la media de los números ingresados
    print(f"La media de los números ingresados es: {media}")
else:
    # Muestra un mensaje de error si el número ingresado no es positivo
    print("El número ingresado no es válido, debe ser un número entero positivo.")

# Punto 10

# Solicitar un número al usuario
num = input("Ingrese un número entero: ")

# Convertir el número a string, invertirlo y mostrar el resultado
if num.startswith("-"):
    invertido = "-" + num[:0:-1]  # Excluye el signo y lo invierte
else:
    invertido = num[::-1]

print(f"Número invertido: {invertido}")
