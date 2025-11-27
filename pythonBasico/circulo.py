"""
### Nombre del Programa: Circulo y Area                      
## Autor: Mónica Tahan                                                 
## Versión: 1.0                                                        
## Descripción: programa para calcular el área de un circulo segun su radio                     
###
"""

# Declaracion de las variables

area = 0.0
radio = 0.0

# Mensaje de bienvenida

print("Bienvenidos al programa de calculo del area del circulo,")
print("para continuar presione cualquier tecla")
print("Por favor introduzca el valor del radio del circulo: ")
radio = float(input())
#radio = float(radio)

# Calculo del area del circulo

area = 3.1416 * radio**2

# Impresion del resultado

print("El area del circulo es: ", str(area))
