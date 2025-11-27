print ('Hola, este es mi primer programa en Python')

"""
Esto es un ejemplo de un comentario en bloque o multilinea
sumary_line

Keyword arguments:
argument -- description
Return: return_description
"""
# Esto es un comentario de una sola linea

variable = input() #La variable obtiene el valor insertado por teclado

print('Este fue el mensaje que usted escribió: \n') #Imprime un mensaje
print(variable) #Imprime el valor de la variable

# Ejemplo de estructura de control if

print('Color del semáforo:')
semaforo = input()

if semaforo == 'verde': 
    print("Cruzar la calle")
else: 
    print("Esperar")

print('Valor de la compra:')
compra = int(input())

print(compra)
#compra = int(compra)
if compra <= 100: 
    print("Pago en efectivo") 
elif compra > 100 and compra <= 300: 
    print("Pago con tarjeta de débito") 
else: 
    print("Pago con tarjeta de crédito")