#Punto 1

#Funciones

def imprimir_hola_mundo():
   return print("Hola Mundo!")

#Progama principal

imprimir_hola_mundo()

#Punto 2

#Funciones

def saludar_usuario_nombre(nombre):
    return print(f"Hola {nombre}!")

#Programa principal

saludar_usuario_nombre(input("Ingrese su nombre: "))

#Punto 3

#Funciones

def informacion_personal(nombre, apellido, edad, residencia):
    return print(f"Soy {nombre.capitalize()} {apellido.capitalize()}, tengo {edad} años y vivo en {residencia.capitalize()}")

#Programa principal

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")

informacion_personal(nombre, apellido, edad, residencia)

#Punto 4

#Funciones

def calcular_area_circulo(radio):
    pi = 3.14159
    return pi * (radio ** 2)

def calcular_perimetro_circulo(radio):
    pi = 3.14159
    return pi * radio * 2

#Programa principal

radio = int(input("ingrese el radio de su circulo: "))

area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)

print(f"el area de su circulo es de {area} y el perimetro es de {perimetro}")

#Punto 5

#Funciones

def segundos_a_horas(seg):
    return seg / 60

#Programa principal

horas = segundos_a_horas(int(input("Ingrese la cantidad de segundos: ")))
print(f"los segundos que ingreso equivalen a {horas} hora/s")

#Punto 6

#Funciones

def tabla_multiplicar(numero):
    for mult in range(11):
        tabla =  numero * mult
        print(f"{numero} x {mult} = {tabla}")
    return 

#Programa principal

num = int(input("ingrese un numero: "))

tabla_multiplicar(num)

#Punto 7

#Funciones

def operaciones_basicas(a, b):

    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b

    lista = (suma, resta, multiplicacion, division)
    
    return lista

#Programa principal

num1 = int(input("ingrese el primer numero: "))
num2 = int(input("ingrese el segundo numero: "))
resultados = operaciones_basicas(num1, num2)

print(f"""la suma es {resultados[0]}
la resta es {resultados[1]}
la multiplicacion es {resultados[2]}
la division es {resultados[3]}""")

#Punto 8

#Funciones

def calcular_imc(peso, altura):

    return peso / (altura**2)

#Programa principal

peso = float(input("ingrese su peso en kg: "))
altura = float(input("ingrese su altura en metros(ej: 1.80): "))

imc = calcular_imc(peso, altura)

print(f"Su imc es de {round(imc, 2)}")

#Punto 9

#Funciones

def celcius_a_fahrenheit(celsius):
    return celsius * (9/5) + 32 

#Programa principal

grado_c = float(input("ingrese su temperatura en grados celsius: "))

grado_f = celcius_a_fahrenheit(grado_c)

print(f"La temperatura que ingreso equivale a {grado_f}° fahrenheit")

#Punto 10

#Funciones

def calcular_promedio(a, b, c):
    return (a + b + c) / 3

#Programa principal

num1 = float(input("ingrese la primera nota: "))
num2 = float(input("ingrese la segunda nota: "))
num3 = float(input("ingrese la tercera nota: "))

promedio = calcular_promedio(num1, num2, num3)

print(f"el promedio de la clase es de {promedio}")

