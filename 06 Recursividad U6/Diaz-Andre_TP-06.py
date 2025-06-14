#Punto 1

#Funciones

def factoriales(num):
    if num == 0:
        return 1
    else:
        return num * factoriales(num - 1)
    
#Programa principal

num = int(input("ingrese un numero entero positivo: "))

if num > 0:
    print(factoriales(num))
else:
    print("ERROR")

#Punto 2

#Funciones

def fibonacci(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        pos_exacta = fibonacci(pos - 1) + fibonacci(pos - 2)
        return pos_exacta
    
def fibonacci_completo(pos):
    pos_lista = []
    for i in range(pos+1):
        pos_lista.append((fibonacci(i)))
    return pos_lista

#Programa principal

num = int(input("ingrese una posición: "))

pos_exacta = fibonacci(num)
pos_lista = fibonacci_completo(num)

print(f"su posición equivale al numero {pos_exacta}, los numeros anteriores en la lista son {pos_lista}")

#Punto 3

#Funciones

def potencia(n, m):
    if m == 0:
        return 1
    else:
        return n * potencia(n, m-1)

#Programa principal

n = int(input("ingrese un numero positivo como base: "))
m = int(input("ingrese un numero positivo como exponente: "))

resultado = potencia(n, m)

print(f"{n} elevado a la {m} es igual a {resultado}")

#Punto 4

#Funciones

def decimal_a_binario(num):
    if num == 0:
        return ""
    else: 
        return decimal_a_binario(num // 2) + str(num % 2)

#Programa principal

num = int(input("ingrese un numero decimal positivo: "))

binario = decimal_a_binario(num)

print(f"{num} es igual a {binario} en binario")

#Punto 5

#Funciones

def es_palindromo(texto):
    texto = texto.lower().replace(" ", "")
    for i in range(len(texto) // 2):
        if texto[i] != texto[len(texto) - 1 - i]:
            return False
    return True

#Programa principal

palabra = input("ingrese una palabra a comprobar: ")

palindromo = es_palindromo(palabra)

if palindromo:
    print(f"¿Es palindromo? {palindromo}")
else:
    print(f"¿Es palindromo? {palindromo}")

#Punto 6

#Funciones

def suma_digitos(n):
    if n < 10:
        return n
    else: 
        return (n % 10) + suma_digitos(n // 10)

#Programa principal

num = int(input("ingrese un numero: "))

suma = suma_digitos(num)

print(f"la suma de los digitos de {num} es {suma}")

#Punto 7

#Funciones

def contar_bloques(n):
    if n == 0:
        return 0 
    else:
        return n + contar_bloques(n-1)

#Programa principal

num = int(input("ingrese un numero: "))

bloques_totales = contar_bloques(num)

print(f"La cantidad de bloques que se necesitan son {bloques_totales}")

#Punto 8

Funciones

def contar_digito(num, digito):
    if num == 0:
        return 0
    else:
        num_analizado = num % 10

        if num_analizado == digito:
            cantidad = 1 + contar_digito(num // 10, digito)
            return cantidad
        else:
            cantidad = contar_digito(num // 10, digito)
            return cantidad
        
#Programa principal

numero = int(input("ingrese un numero a analizar: "))
digito = int(input("ingrese el digito a buscar: "))

if numero > 0 and (digito >= 0 and digito <= 9):
    cantidad = contar_digito(numero, digito)
    if cantidad == 1:
        print(f"En el numero {numero} el digito {digito} se repite {cantidad} vez")
    else:
        print(f"En el numero {numero} el digito {digito} se repite {cantidad} veces")