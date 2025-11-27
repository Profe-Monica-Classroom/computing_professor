//#############################################
//# Nombre del Programa: Registrar Inventario #
//# de cauchos de una tienda en línea		  #
//# Autor: Mónica Tahan                       #
//#Versión: 1.0                               #
//#Descripción: programa para registrar el    #
//#inventario de cauchos por marca            #
//#############################################
Algoritmo inventarioCauchos
	
	Definir marca, tipo como caracter
	Definir rin, ancho, costo, precio, porcentaje como real
	Definir nitems, cantidad, i Como Entero
	Definir cauchos como caracter
	Dimension cauchos[1000000,8]
	
	//INICIALIZAR VARIABLES
	
	marca<-''
	tipo<-''
	rin<-0.0
	ancho<-0.0
	costo<-0.0
	precio<-0.0
	porcentaje<-0.0
	nitems<-0
	cantidad<-0
	i<-1
	
	Escribir "---------------------------------------------------------------"
	Escribir "-       BIENVENIDOS AL REGISTRO DE INVENTARIO DE CAUCHOS      -"
	Escribir "---------------------------------------------------------------"
	Escribir "                                               "
	Escribir "Ingrese la cantidad de MARCAS DE CAUCHOS a Registrar:"
	
	leer nitems
	
	Para i<-1 Hasta nitems Hacer
		Escribir "Ingrese la marca del caucho ",i,":" //solicitando Nombre y Apellido
		Leer marca
		cauchos[i,1]=marca //Guardando la marca del caucgo en el arreglo cauchos
		Escribir "Ingrese el número de rin del caucho ",i,":"
		leer rin
		cauchos[i,2]=ConvertirATexto(rin)
		Escribir "Ingrese el ancho del caucho ",i,":"
		Leer ancho
		cauchos[i,3]=ConvertirATexto(ancho)
		Escribir "Ingrese el costo del caucho ",i,":"
		Leer costo
		cauchos[i,4]=ConvertirATexto(costo)
		Escribir "Ingrese el tipo del caucho ",marca,":"
		Leer tipo
		cauchos[i,5]=tipo
		Escribir "Ingrese la cantidad de cauchos ",marca,":"
		Leer cantidad
		cauchos[i,6]=ConvertirATexto(cantidad)
		Escribir "Ingrese el porcentaje del caucho ",i,":"
		Leer porcentaje
		cauchos[i,7]=ConvertirATexto(porcentaje)
		precio<-costo+(costo*porcentaje/100)
		cauchos[i,8]=ConvertirATexto(precio)
		
	FinPara
	
	Imprimir  "Gracias por ingresar los datos, por favor presione cualquier tecla para continuar"
	
	Esperar Tecla
	
	Limpiar Pantalla
	//MOSTRANDO LOS DATOS
	Escribir "------------------------------"
	Escribir "- Usted ingresó estos datos: -"
	Escribir "------------------------------"
	i<-1
	
	Escribir " Marca | Rin | ancho | Costo | Tipo | Cantidad | Porcentaje | Precio "	
	
	Para i<-1 Hasta nitems Hacer
		Escribir "| ",cauchos[i,1]," | ",cauchos[i,2]," | ",cauchos[i,3]," | ",cauchos[i,4]," | ", cauchos[i,5]," | ",cauchos[i,6]," | ",cauchos[i,7]," | ",cauchos[i,8]," | "
		
	FinPara
	
	
	
FinAlgoritmo
