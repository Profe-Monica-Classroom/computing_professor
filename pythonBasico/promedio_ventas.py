"""
### Nombre del Programa: Promedio de Ventas                      
## Autor: Mónica Tahan                                                 
## Versión: 1.0                                                        
## Descripción: programa para calcular el promedio de ventas de una empresa                    
###
"""

# INICIALIZACION DE VARIABLES

ventAcum = 0.0
items = 0
promedioVentas = 0.0
ventaDia = 0.0
nombreMes = ''
fecha = ''
print("#############################################################")
print("BIENVENIDOS al programa de CALCULO del promedio de VENTAS,")
print("#############################################################")

print("A continuación usted debe indicar los datos siguientes:")
print("Indique el Nombre del mes:")
nombreMes = input()
print("Indique el numero de ventas a registrar en el sistema para obtener el promedio")
items = int(input())

print("#############################################################")

for i in range(items):
    print("Por favor indique el valor de la venta del día", i+1)
    ventaDia = float(input())
    print("Por favor indique la fecha de la venta del día")
    fecha = input()
    ventAcum = ventAcum + ventaDia
    print("Usted Introdujo la Fecha: ", fecha,  " y la Venta: ", ventaDia )
    print(" y la Venta: ", ventaDia)

# CALCULO DEL PROMEDIO

promedioVentas = ventAcum / items

print("#############################################################")
print("El promedio de ventas del mes de ", nombreMes, " es: ", promedioVentas)
print("#############################################################")
print("Gracias por utilizar nuestro programa, Vuelva pronto!!!")
