#Punto 1

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

#Punto 2

precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

#Punto 3

solo_frutas = list(precios_frutas.keys())
print(solo_frutas)

#Punto 4

agenda = {}

for i in range(5):
    nombre = input("Ingresá el nombre del contacto: ")
    numero = input("Ingresá el número de teléfono: ")
    agenda[nombre] = numero

buscar = input("¿A quién querés buscar?: ")
if buscar in agenda:
    print(f"El número de {buscar} es {agenda[buscar]}")
else:
    print("Contacto no encontrado.")

#Punto 5

frase = input("Ingresá una frase: ").lower()
palabras = frase.split()

palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)

conteo = {}
for palabra in palabras:
    if palabra in conteo:
        conteo[palabra] += 1
    else:
        conteo[palabra] = 1

print("Frecuencia de palabras:", conteo)

#Punto 6

for i in range(3):
    nombre = input("Nombre del alumno: ")
    notas = tuple(float(input(f"Ingresá nota {j+1} de {nombre}: ")) for j in range(3))
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {nombre} es {promedio:.2f}")

#Punto 7

parcial1 = {'Ana', 'Luis', 'Pedro', 'Juan'}
parcial2 = {'Luis', 'Pedro', 'María', 'Laura'}

ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2

print("Aprobaron ambos:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", al_menos_uno)

#Punto 8

stock = {'pan': 10, 'leche': 5, 'azúcar': 8}

producto = input("Ingresá el producto a consultar: ")

if producto in stock:
    print(f"Stock de {producto}: {stock[producto]}")
    agregar = int(input("¿Cuántas unidades querés agregar?: "))
    stock[producto] += agregar
else:
    nuevo = int(input("Producto no encontrado. Ingresá stock inicial: "))
    stock[producto] = nuevo

print("Stock actualizado:", stock)

#Punto 9

agenda = {
    ('lunes', '10:00'): 'Reunión',
    ('martes', '14:00'): 'Clase de programación'
}

dia = input("Ingresá el día: ").lower()
hora = input("Ingresá la hora (HH:MM): ")

if (dia, hora) in agenda:
    print(f"Actividad: {agenda[(dia, hora)]}")
else:
    print("No hay actividad registrada en ese horario.")


#Punto 10

paises = {
    'Argentina': 'Buenos Aires',
    'Francia': 'París',
    'Japón': 'Tokio'
}

capitales = {capital: pais for pais, capital in paises.items()}
print(capitales)
