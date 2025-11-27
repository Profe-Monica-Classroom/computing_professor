Algoritmo sin_titulo
	//muestra el mayor de los numeros ingresados
	
	Definir n1, n2, n3, n4, n5, n6, n7 Como Entero;
	escribir Sin Saltar "Ingrese el numero 01: ";
	leer n1
	Escribir Sin Saltar "Ingrese el numero 02: ";
	leer n2
	escribir Sin Saltar "Ingrese el numero 03: ";
	Leer n3
	escribir Sin Saltar "Ingrese el numero 04: ";
	Leer n4
	escribir Sin Saltar "Ingrese el numero 05: ";
	Leer n5
	escribir Sin Saltar "Ingrese el numero 06: ";
	Leer n6
	Escribir Sin Saltar "Ingrese el numero 07: ";
	leer n7
	si ((n1>n2) y (n1>n3) y (n1>n4) y (n1>n5) y (n1>n6) y (n1>n7)) Entonces
		escribir "El mayor es: ", n1;
	SiNo
		si ((n2>n1) y (n2>n3) y (n2>n4) y (n2>n5) y (n2>n6) y (n2>n7)) Entonces
			Escribir "El mayor es: ", n2;
		sino
			si ((n3>n1) y (n3>n2) y (n3>n4) y (n3>n5) y (n3>n6) y (n3>n7)) Entonces
				Escribir "El mayor es: ", n3;
			SiNo
				si ((n4>n1) y (n4>n2) y (n4>n3) y (n4>n5) y (n4>n6) y (n4>n7)) Entonces
					Escribir "El mayor es: ", n4;
				SiNo
					si ((n5>n1) y (n5>n2) y (n5>n3) y (n5>n4) y (n5>n6) y (n5>n7)) Entonces
						Escribir "El mayor es: ", n5;
					SiNo
						si((n6>n1) y (n6>n2) y (n6>n3) y (n6>n4) y (n6>n5) y (n6>n7)) Entonces
							Escribir "El mayor es: ", n6;
						SiNo
							si((n7>n1) y (n7>n2) y (n7>n3) y (n7>n4) y (n7>n5) y (n7>n6)) Entonces
								Escribir "El mayor es:", n7;
							FinSi
						FinSi
					FinSi
				FinSi
			FinSi
		FinSi
	FinSi
	escribir "Gracias por usar el programa :D"
FinAlgoritmo
