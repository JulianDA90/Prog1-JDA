#Punto 1

#ingreso de los numeros a la lista via range
numeros = list(range(4, 100, 4))

print(numeros)

#Punto 2

limbus_status = ["poise", "bleed", "burn", "rupture", "sinking"]

print(limbus_status[-2])

#Punto 3

#crecion de la lista
limbus_cantos = []

#adicion de los elementos
limbus_cantos.append("the dream ending")
limbus_cantos.append("the hearthbreaking")
limbus_cantos.append("the evil defining")

print(limbus_cantos)

#Punto 4

animales = ["perro", "gato", "conejo", "pez"]

animales[-3] = "loro"
animales[-1] = "oso"
    
print(animales)

#Punto 5

#El programa identifica cual es el elemento con el valor más grande y lo remueve con la funcion .remove()

#Punto 6

numeros = list(range(10, 31, 5))

print(numeros[0:2])

#Punto 7

autos = ["sedan", "polo", "suran", "gol"]

autos[1] = "remember"
autos[2] = "me"

print(autos)

#Punto 8

dobles = []

dobles.append(5*2)
dobles.append(10*2)
dobles.append(15*2)

print(dobles)

#Punto 9

compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
["agua"]]

compras[2].append("jugo")
compras[1][1] = "tallerines"
compras[0].remove("pan")

print(compras)

#Punto 10

lista_anidada = [15, True, [25.5, 57.9, 30.6], False]

print(lista_anidada)