//#############################################
//# Nombre del Programa: Calcula Cuadrados    #
//# Autor: Mónica Tahan                       #
//#Versión: 1.0                               #
//#Descripción: programa para calcular el área#
//#de un cuadrado o rectángulo                #
//#############################################

Algoritmo calculo_cuadrado
	//Inicialización de Variables
	Definir lado1 Como real
	Definir lado2 Como real
	Definir  area Como real
	Definir tipoMedida Como Entero
	lado1<-0.0 //incialización de la variable lado1
	lado2<-0.0 //inicialización de la variable lado2
	area<-0.0 //inicialización de la variable area
	tipoMedida<-0
	//Solicitar entradas del algoritmo
	Imprimir "-----------------------------------------------"
	Imprimir "-   Bienvenidos al Sistema Calcula Cuadrados  -"
	Imprimir "_----------------------------------------------"
	Imprimir "Por favor seleccione la unidad de medida del area a calcular"
	Imprimir "Escriba 1 para centimetros (cms)"
	Imprimir "Escriba 2 para metros (m)"
	Imprimir "Escriba 3 para Kilometros (Km)"
	Leer tipoMedida
	Imprimir "Por favor indique el valor del lado1  "
	leer lado1
	Si ((lado1<0)O(lado1>1000000)) Entonces
		Imprimir  "Debe introducir números mayores que 0 y menores que 1.000.000"
		Imprimir "Por favor indique el valor del lado1"
		Leer lado1
	SiNo
	Fin Si	
		Imprimir  "Por favor indique el valor de lado 2"
		leer lado2
	
	Si ((lado2<0)O(lado2>1000000)) Entonces
		Imprimir "Debe introducir números mayores que 0 y menores que 1.000.000"
		Imprimir "Por favor indique el valor del lado2"
		Leer lado2
	SiNo
	fin si
	
	//Proceso de cálculo del área de un cuadrado o rectángulo
	
	area<-(lado1*lado2)
	
	Imprimir  "El valor del área del cuadrado es:"
	areaTexto = ConvertirATexto(area)
Segun tipoMedida hacer
		1:
			Imprimir  areaTexto + " centimetros (cms)"
			Imprimir "Gracias por utilizar nuestro programa de cálculo"
		2:
			Imprimir  areaTexto + " metros (m)"
			Imprimir "Gracias por utilizar nuestro programa de cálculo"
		3:
			Imprimir  areaTexto + " kilometros (Km)"
			Imprimir "Gracias por utilizar nuestro programa de cálculo"
		De Otro Modo:
			Imprimir areaTexto + " Unidad de Medida no indicada"
	FinSegun
	
FinAlgoritmo
