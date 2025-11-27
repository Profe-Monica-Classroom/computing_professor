#!/usr/bin/python
""" Esto es un comentario multilinea
    Puedo escribir todo lo que desee
"""
#############################################
# Nombre del Programa: Calcula Cuadrados    #
# Autor: Eduardo Garcia                     #
#Versión: 1.0                               #
#Descripción: programa para calcular el área#
#de un cuadrado o rectángulo                #
#############################################

lado2 = float(input("Coloque el valor de la base: "))
lado1 = float(input("Coloque el valor de la Altura: "))
medida = (input("En que medida desea el area? "))

if lado1 < 0 or lado1 > 1000000 or lado2 < 0 or lado2 >1000000:
    print("Debe introducir números mayores que 0 y menores que 1.000.000")
    lado2 = float(input("Coloque el valor de la base: "))
    lado1 = float(input("Coloque el valor de la altura: "))
    area = lado1 * lado2
    print("El area de su rectangulo es: " + str(area) + " " + medida)
    print("Gracias por utilizar nuestro programa, vuelva pronto .....")
    input()
else:
    area = lado1 * lado2
    print("El area de su rectangulo es: " + str(area) + " " + medida)
    print("Gracias por utilizar nuestro programa, vuelva pronto .....")
    input()