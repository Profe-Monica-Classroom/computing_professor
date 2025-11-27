#!/usr/bin/python
# coding=<UTF-8>
"""
### Nombre del Programa: Practica Basica de Python                      #
//# Autor: Mónica Tahan                                                 #
//# Versión: 1.0                                                        #
//# Descripción: Algoritmo de Ensenanza de Python)                      #
###

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# INICIALIZACION DE VARIABLES
"""
# ESTO ES UN COMENTARIO DE 1 LINEA

print("Hola, Bienvenidos a COMPUTACION 1. Por favor dime de que color está el semáforo")

semaforo = input()

if semaforo == "verde": 
    print("Cruzar la calle")
else: 
    print("Esperar")

print(semaforo)

# Vamos a barrer un bucle while

year = 2001 
while year <= 2024: 
    print("Informes del Año", str(year)) 
    year += 1

# Ejemplo de un For

mi_tupla = ('rosa', 'verde', 'celeste', 'amarillo') 
print(mi_tupla)
for color in mi_tupla: 
    print(color)
print("Hola este es mi primer programa python de Computacion 1")