'''
	Colecciones de datos en Python (Tuplas)
	
	Existe cuatro tipos de datos en Python:
	Listas, Tuplas, Sets y Diccionarios
'''

# TUPLAS
# Una tupla es una colección de datos ordenada y NO MODIFICABLE
# Se declaran de la siguiente forma:
estaTupla = ("manzana", "banana", "cereza")
miTuplaNumeros = (1, 9, 4, 2, 5, 8)

# Se accede a los elementos de la misma forma que en las listas
print(estaTupla[1])
print(estaTupla[-1])

# Intervalo
print(miTuplaNumeros[2:6])
print(miTuplaNumeros[2:5])


# Recorrer en un for
for k in miTuplaNumeros:
  print(k)

# Una vez definida la tupla, esta no puede ser modificada
# por lo que intentar hacer
## estaTupla[1] = "kiwi"
# Producirá un error
# Por lo que, lo que regularmente se hace es utilizar listas
# o realizar conversiones
estaTuplaCopia = list(estaTupla)
print(estaTuplaCopia)
estaTuplaCopia[1] = "kiwi"
print(estaTuplaCopia)
estaTuplaCopia.append("uva") #agregando un elemento
print(estaTuplaCopia)

estaTuplaCopia.append("kiwi")
print(estaTuplaCopia)
# y luego convertirla nuevamente a tupla
# o simplemente crear una nueva tupla con los elementos
# de la lista   
estaTupla = tuple(estaTuplaCopia)
print(estaTupla)

# Verificar que un elemento exista en la tupla
if "manzana" in estaTupla:
  print("La manzana está en la tupla")
else:
  print("La manzana no está en la tupla")
# Solo puede eliminarse por completo la tupla con el operador "del"

# Unir tuplas
tuplaGrande = estaTupla + miTuplaNumeros
print(tuplaGrande)

# Esto contabiliza cuantas veces aparece un elemento en la tupla
print(tuplaGrande.count('kiwi'))

# Desempaquetar tuplas
elem1, elem2 = (1, "olakease")
print(elem2)
print(elem1)