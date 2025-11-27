# -*- coding: utf-8 -*-

lado1=0.0

lado2=0.0

lado3=0.0

base=0.0

altura=0.0

tipo_medida='A'

tipo_triangulo=''

nombre_medida=''



print("Bienvenidos al programa de calculo del area del triangulo,") 

print("para continuar presione cualquier tecla")

input()



while tipo_medida=='A' or tipo_medida=='B' or tipo_medida=='C':

    print("Por favor indique el tipo de medida de su triangulo:")

    print("A. Centimetros (cms)")

    print("B. Metros (mts)")

    print("C. Milimetros (mms)")

    tipo_medida = input()

    if tipo_medida=='A':

        nombre_medida="cms"

    if tipo_medida=='B':

        nombre_medida="mts"

    if tipo_medida=='C':

        nombre_medida="mms"

		

    #SOLICITUD DE LOS VALORES DEL TRIANGULO

		

    print("Por favor indicar el valor de la base")

    base = input()

    base = int(base)

    print(base)

    #base=int(base)

    print("Por favor indicar el valor de la altura")

    altura = int(input())

    print("Por favor indicar el valor del lado 1")

    lado1 = int(input())

    print("Por favor indicar el valor del lado 2")

    lado2 = int(input())

    print("Por favor indicar el valor del lado 3")

    lado3 = int(input())

    

    # CALCULO DEL AREA

    area=(base*altura)/2

    

    if lado1==lado3 and lado2==lado3:

        tipo_triangulo="Equilatero"

    elif lado1 == lado2  or lado1==lado3:

        tipo_triangulo="Isosceles"

    else:

        tipo_triangulo="Escaleno"

        

    

    print("El area del triangulo es: ", area, " ", nombre_medida, "y es del tipo: ", tipo_triangulo)

    print("Gracias por usar este programa")

    input()