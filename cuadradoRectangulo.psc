Algoritmo cuadradoRectangulo
	// ###############################################
	// # Nombre del Programa: Calcula Cuadrados      #
	// # Autor: Mónica Tahan                         #
	// # Versión: 1.0                                #
	// # Descripción: programa para calcular el área #
	// # de un cuadrado o rectángulo                 #
	// ###############################################
	// DEFINICION DE VARIABLES
	Definir lado1,lado2 Como Real
	Definir area Como Real
	Definir tipoMedida Como Entero
	Definir tipoMedida_cms, tipoMedida_mts, medida_string Como Caracter
	// INICIALIZACION DE VARIABLES
	lado1 <- 0.0
	lado2 <- 0.0
	area <- 0.0
	tipoMedida <- 1 // tipoMedida=1 para Metros(mts) y tipoMedida=2 para centimetros (cms)
	tipoMedida_mts <- 'METROS CUADRADOS (mts^2)'
	tipoMedida_cms <- 'CENTIMETROS CUADRADOS (cms^2)'
	medida_string <- ''
	// SOLICITUD DE LAS VARIABLES DE ENTRADA AL USUARIO
	Escribir '**************************************************************************************************'
	Escribir '**   BIENVENIDOS AL PROGRAMA CALCULA CUADRADOS POR FAVOR SIGUE LAS INSTRUCCIONES A CONTINUACION **'
	Escribir '**************************************************************************************************'
	Escribir ' POR FAVOR INDIQUE SI VA A CALCULAR EL AREA EN CENTIMETROS O METROS :							   **'
	Escribir ' PARA METROS (MTS) PRESIONE 1																	   **'
	Escribir ' PARA CENTIMETROS (CMS) PRESIONE 2															   **'
	Leer tipoMedida
	Mientras tipoMedida<1 o tipoMedida>2 hacer	
		Escribir "RECUERDE QUE PARA INDICAR EL TIPO DE MEDIDA DEBE: 											   **"
		Escribir ' PARA METROS (MTS) PRESIONE 1																	   **'
		Escribir ' PARA CENTIMETROS (CMS) PRESIONE 2 **'
		Leer tipoMedida
	Fin Mientras
	//SEGUN EL TIPO DE MEDIDA CONFIGURAMOS CUAL STRING SE VA A MOSTRAR EN PANTALLA
	si tipoMedida = 1 Entonces
		medida_string = tipoMedida_mts
	SiNo
		medida_string = tipoMedida_cms
	FinSi
	
	Escribir 'USTED INDICO QUE CALCULARA EL AREA EN: ', medida_string
	Escribir ' POR FAVOR INDIQUE EL VALOR DEL LADO 1: '
	Leer lado1
	Escribir 'EL VALOR DEL LADO 1 ES ',lado1
	Escribir ' POR FAVOR INDIQUE EL VALOR DEL LADO 2'
	Leer lado2
	Escribir 'EL VALOR DEL LADO 2 ES ',lado2
		// PROCESO DE CALCULO DEL AREA DEL RECTANGULO O CUADRADO
	area <- lado1*lado2
	Si tipoMedida=1 Entonces
		Escribir 'EL AREA DEL RECTANGULO O CUADRADO ES DE: ',area,' METROS CUADRADOS (MTS^2)'
	SiNo
		Escribir 'EL AREA DEL RECTANGULO O CUADRADO ES DE: ',area,' CENTIMETROS CUADRADOS(CMS^2)'
	FinSi
		Escribir '*** GRACIAS POR UTILIZAR NUESTRO SOFTWARE CALCULA CUADRADO, VUELVA PRONTO ***'
		Esperar Tecla
		
FinAlgoritmo
