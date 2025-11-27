'''
	Colecciones de datos en Python (Diccionarios)
	
	Existe cuatro tipos de datos en Python:
	Listas, Tuplas, Sets y Diccionarios
'''
"""sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""


# DICCIONARIOS
# Un diccionario es una colección de datos sin orden, modificables y ordenadas
# Contienen llaves y valores
cauchos = {
  "marca" : "Good Year",
  "rin" : 15,
  "ancho" : 65,
  "costo" : 50,
  "tipo" : "radial",
  "cantidad" : 15,
  "porcentaje" : 20,
  "precio" : 75
}

print(cauchos)
# Si se esta familiarizado con los archivos JSON, los diccionarios
# son muy similares

# Acceder a los elementos
print(cauchos["tipo"])
# o con el método get
print(cauchos.get("tipo"))

# Cambiar los valores
cauchos["rin"] = 14

# Recorrer un diccionario
# Puede recorrerse las llaves del diccionario
for x in cauchos:
  print(x)

# o mostrar todos los valores
for k in cauchos:
  print(cauchos[k])

# o usando el método values()
for k in cauchos.values():
  print(k)

# o ir mostrando las llaves y valores
for k in cauchos.items():
  print(k)
# Regresa una tupla

# Revisar si una llave existe en el diccionario
if "tipo" in cauchos:
  print("Tipo esta en el diccionario")

# Longitud del diccionario
print(len(cauchos))

# Añadir nuevas llaves con su valores
cauchos["tipo"] = "convencional"
print(cauchos)

# Eliminar un elemento por medio de la llave
cauchos.pop("tipo")

# Copiar un diccionario
# debe de realizarse por medio de un método
# ya que si se hace usando =, sucederá lo mismo que 
# con las listas, donde se modificará la copia al modificar el original
cauchosCopia = cauchos.copy()
print(cauchosCopia)

# o también mediante dict()
cauchosCopia2 = dict(cauchos)
print(cauchosCopia2)


# Unión de diccionarios o diccionarios anidados
# Generar diccionarios
persona1 = {
  "nombre" : "Emilio",
  "año" : 2001
}

persona2 = {
  "nombre" : "Tobias",
  "año" : 2004
}

persona3 = {
  "nombre" : "'Linus'",
  "año" : 2000
}

for k in persona3.values():
  print(k)

# Luego conjuntarlas
lasPersonas = {
  "persona1" : persona1,
  "persona2" : persona2,
  "persona3" : persona3,
}

print(lasPersonas)

for k in lasPersonas.values():
  print(k)