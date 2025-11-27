'''
	Manejo de estructuras de control
'''

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# ESTRUCTURA DE DECISIÓN
a = 0
b = 0
a = input("Por favor intrduzca el valor de a: ")
a = int(a)
b = input("Por favor intrduzca el valor de b: ")
b = int(b)
if a > b:
  print("{:d} es mayor que {:d}".format(a, b))
elif a < b:
  print("{:d} es mayor que {:d}".format(b, a))
else:
  print("Ambos números son iguales")
# Se debe considerar la "indentación"
# esto es colocar espacio o espacios 
# para sustituir a las llaves del lenguaje C

# DESAFORTUNADAMENTE NO EXISTE EL SWITCH EN PYTHON (aunque no se le extraña)

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# ESTRUCTURAS DE CICLOS
# Ciclo while
i = 1
while i <= 6:
  print(i)
  i += 1

# Utilizando la instrucción break
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# Utilizando la instrucción continue
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# Puede generarse un bloque infinito
while True:
  entrada = input("Salir con s> ")
  if entrada == 's':
    # Es posible romper el ciclo con la instrucción break
    break


# Ciclo for
# Puede usarse la instrucción range()
# para indicar inicio, fin y pasos que dará el for
for cont in range(0, 10, 2):
  k = cont
  # en lenguaje C sería algo como for(k = 0; k < 10; k++)
  print(k)

# Puede usarse para recorrer letra a letra una cadena de texto por ejemplo
for k in "anaconda":
  print(k)