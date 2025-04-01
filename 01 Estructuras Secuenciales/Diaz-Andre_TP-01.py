#punto 1
print("Hola mundo!")

#punto 2
nombre = input("Escriba su nombre: ")
print(f"Hola {nombre}!")

#punto 3
nombre = input("Escriba su nombre: ")
apellido = input("Escriba su apellido: ")
edad = input("Escriba su edad: ")
lugar = input("Escriba el nombre del lugar donde reside: ")

print(f"Soy {nombre}, tengo {edad} años y vivo en {lugar}")

#punto 4
radio = int(input("escriba el radio de su circulo: "))

pi = 3.141592
diametro = radio * 2

perimetro = pi * diametro

area = pi * (radio ** 2)

print(f"El area de su circulo es de {area} y su perimetro es de {perimetro}")

#punto 5
segundos = int(input("ingrese una cantidad de segundos: "))

hora = segundos // 3600

print(f"los {segundos} segundos equivalen a {hora} hora/s")

#punto 6
numero = int(input("inserte un numero: "))

num0 = numero * 0
num1 = numero * 1
num2 = numero * 2
num3 = numero * 3
num4 = numero * 4
num5 = numero * 5
num6 = numero * 6
num7 = numero * 7
num8 = numero * 8
num9 = numero * 9
num10 = numero * 10

print(f"{numero} x 0 = {num0}")
print(f"{numero} x 1 = {num1}")
print(f"{numero} x 2 = {num2}")
print(f"{numero} x 3 = {num3}")
print(f"{numero} x 4 = {num4}")
print(f"{numero} x 5 = {num5}")
print(f"{numero} x 6 = {num6}")
print(f"{numero} x 7 = {num7}")
print(f"{numero} x 8 = {num8}")
print(f"{numero} x 9 = {num9}")
print(f"{numero} x 10 = {num10}")

#punto 7
#ingreso de variables
num1 = int(input("ingrese el primer numero que no sea 0: "))
num2 = int(input("ingrese el segundo numero que no sea 0: "))

#ejecucion de codigo 
if num1 and num2 != 0:

    #calculos
    numplus = num1 + num2
    numext  = num1 - num2 
    numx    = num1 * num2
    numdiv  = num1 / num2

    #devuelta por consola
    print(f"{num1} + {num2} = {numplus}")
    print(f"{num1} - {num2} = {numext}")
    print(f"{num1} * {num2} = {numx}")
    print(f"{num1} / {num2} = {numdiv}")
else:
    #en caso de ingresar un numero no valido
    print("ingrese un numero distinto al cero")
    exit

#punto 8
altura = float(input("ingrese su altura en metros: "))
peso = float(input("ingrese su peso en KG: "))

imc = peso / (altura **2)

print(f"su IMC o indice de masas corporal es de {imc}.")

#punto 9
celsius = float(input("ingrese una temperatura en celsius "))
fahr = (celsius * 9/5) + 32

print(f"{celsius}° celsius equivale a {fahr}° fahrenheit")

#punto 10
num1 = float(input("ingrese el primer numero: "))
num2 = float(input("ingrese el segundo numero: "))
num3 = float(input("ingrese el tercer numero: "))

numpromedio = (num1 + num2 + num3) / 3

print(f"el promedio de {num1}, {num2} y {num3} es de {numpromedio}")