'''
	Colecciones de datos en Python (Sets)
	
	Existe cuatro tipos de datos en Python:
	Listas, Tuplas, Sets y Diccionarios
'''

# SETS
# Un set es una colección de datos no ordenada y no indexada
# Se declaran de la siguiente forma:
esteSet = {"manzana", "banana", "cereza"}
miSetNumeros = {1, 9, 4, 2, 5, 8}
# no se asegura la forma en la que se ordenan los datos
# a su vez como no tienen índice su acceso es un tanto más caótico

# Pueden recorrerse con un for
for k in esteSet:
  print(k)

print(esteSet)
# También puede preguntarse si existe un elemento
if "banana" in esteSet:
  print("banana esta en esteSet")

try:
    print(esteSet["banana"])
except:
    print("Lo siento, banana no esta en esteSet")
finally:
    print("Continuamos ejecutando el programa")

# No es posible cambiar los elementos de un set
# pero si añadir nuevos
esteSet.add("kiwi")
print(esteSet)

# o añadir múltiples (a partir de...[])
esteSet.update(["naranja", "mango", "uva"])
print(esteSet)

# Aunque si es posible remover un elemento del set
esteSet.remove("banana")
print(esteSet)

# Unir dos sets, puede utilizarse union() o update()
# descartando los elementos repetidos
superSet = esteSet.union(miSetNumeros)
print(superSet)

# O encontrar la intersección entre ellos
interSet = superSet.intersection(miSetNumeros)
print(interSet)

interSet = superSet.intersection(esteSet)
print(interSet)
