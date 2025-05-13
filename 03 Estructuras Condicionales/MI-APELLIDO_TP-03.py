#Punto 1

edad = int(input("Ingrese su edad: "))

if edad >= 18:  
    print("usted es mayor de edad")
else:
    print("usted no es mayor de edad")

#punto 2

nota = int(input("Ingrese su nota: "))

if nota >= 6:  
    print("usted esta aprobado")
else:
    print("usted no esta aprobado")

#punto 3

par = int(input("Ingrese un numero par: "))

if par % 2 == 0:  
    print("Ha ingresado un numero par")
else:
    print("Por favor, ingrese un numero par")

#punto 4

edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("usted pertenece al grupo de niño/a")
elif edad >= 12 and edad < 18:
    print("usted pertenece al grupo de adolescente")
elif edad >= 18 and edad < 30:
    print("usted pertenece al grupo de joven adulto/a")
else:
    print("usted pertenece al grupo de adulto")

#punto 5

contraseña = str(input("Ingrese una contraseña de entre 8 y 14 caracteres: "))

num_con = len(contraseña)

if num_con >= 8 and num_con <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#punto 6

from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

mea = mean(numeros_aleatorios)
med = median(numeros_aleatorios)
mod = mode(numeros_aleatorios)

if mea > med > mod:

    print("tiene sesgo positivo")

elif mea < med < mod:
    
    print("tiene sesgo negativo")

elif mea == med == mod:

    print("no tiene sesgo")

else:
    print("distribucion con sesgo no definido claramente")

#punto 7

frase = input("ingrese una frase o palabra: ")

frase_letra = frase[-1].lower()
vocales = ["a", "e", "i", "o", "u"]


if frase_letra in vocales:
    print(f"{frase}" + "!")
else:
    print(frase)

#punto 8

nombre = input("ingrese su nombre: ")

print("que desea hacer con su nombre? ingrese el numero referente a la opcion deseada")
print("1. convertir todas las letras en mayusculas \n2. convertir todas las letras en minusculas \n3. convertir la primera letra en mayuscula")
print("ingrese cualquier otro caracter para salir del menu")

opcion = int(input())

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    pass

#punto 9

magnitud = int(input("ingrese la magnitud de un terremoto: "))

if magnitud < 3:
    print("Muy leve (imperceptible).")
elif magnitud < 4 and magnitud >= 3:
    print("Leve (ligeramente perceptible).")
elif magnitud < 5 and magnitud >= 4:
    print("Moderado (sentido por personas, pero generalmente no causa daños).")
elif magnitud < 6 and magnitud >= 5:
    print("Fuerte (puede causar daños en estructuras débiles).")
elif magnitud < 7 and magnitud >= 6:
    print("Muy Fuerte (puede causar daños significativos).")
elif magnitud >= 7:
    print("Extremo (puede causar graves daños a gran escala).")
else:
    print("caracter no valido")

#punto 10

dia = int(input("ingrese el dia de hoy (numero): "))
mes = int(input("ingrese el mes actual (numero): "))
año = int(input("ingrese el año actual: "))
hem = input("ingrese si se encuentra en el hemisferio norte (n) o sur (s): ").strip().upper()

if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
    if hem == "N":
        print("Invierno")
    else:
        print("Verano")

elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
    if hem == "N":
        print("Primavera")
    else:
        print("Otoño")

elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
    if hem == "N":
        print("Verano")
    else:
        print("Invierno")

elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
    if hem == "N":
        print("Otoño")
    else:
        print("Primavera")

else:
    print("Fecha inválida.")