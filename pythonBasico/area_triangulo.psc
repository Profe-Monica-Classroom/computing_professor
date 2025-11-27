//#############################################
	//# Nombre del Programa: Triangulo y Tipo           #
	//# Autor: Mónica Tahan                       #
	//#Versión: 1.0                               #
	//#Descripción: programa para calcular el area#
	//#de un triangulo y decir el tipo segun lados#
	//#############################################	
	//DEFINICION DE VARIABLES
	definir lado1, lado2, lado3, base, altura como numero
	definir tipo_medida Como Entero
	definir tipo_triangulo, nombre_medida Como Caracter
	//INICIALIZACIÓN DE VARIABLES
	lado1<-0.0
	lado2<-0.0
	lado3<-0.0
	base<-0.0
	altura<-0.0
	tipo_medida<-1
	tipo_triangulo<-""
	nombre_medida<-""
	
	Escribir "Bienvenidos al programa de calculo del area del triangulo, para continuar presione cualquier tecla"
	Esperar Tecla
	
	mientras tipo_medida>0 y tipo_medida<=3
		Escribir "Por favor indique el tipo de medida de su triangulo:"
		Escribir "1. Centimetros (cms)"
		Escribir "2. Metros (mts)"
		Escribir "3. Milimetros (mms)"
		
		Leer tipo_medida
		
		si tipo_medida=1
			nombre_medida<-"cms"
		FinSi
		si tipo_medida=2
			nombre_medida<-"mts"
		FinSi
		si tipo_medida=3
			nombre_medida<-"mms"
		FinSi
		
		
		//SOLICITUD DE LOS VALORES DEL TRIANGULO
		
		Escribir "Por favor indicar el valor de la base"
		leer base
		Escribir "Por favor indicar el valor de la altura"
		leer altura
		Escribir "Por favor indicar el valor del lado 1"
		leer lado1
		Escribir "Por favor indicar el valor del lado 2"
		leer lado2
		Escribir "Por favor indicar el valor del lado 3"
		leer lado3
		//CALCULO DEL AREA
		area<-(base*altura)/2
		
		si lado1=lado3 y lado2=lado3
			tipo_triangulo<-"Equilatero"
		SiNo
			si lado1 = lado2  o lado1=lado3
				tipo_triangulo<-"Isosceles"
			SiNo
				tipo_triangulo<-"Escaleno"
			FinSi
		FinSi
		
		Imprimir "El area del triangulo es: ", area, " ", nombre_medida, "y es del tipo: ", tipo_triangulo
		Escribir "Gracias por usar este programa"
		Esperar Tecla
		Limpiar Pantalla
	FinMientras
	Escribir "Debe seleccionar el tipo de medida correcto"
	Esperar Tecla
FinAlgoritmo
