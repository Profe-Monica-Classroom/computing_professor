//#############################################
//# Nombre del Programa: Registrar Inventario #
//# de libros en una biblioteca	y listarlos	  #
//# Autor: Mónica Tahan                       #
//#Versión: 1.0                               #
//#Descripción: programa para registrar el    #
//#inventario de libros por autor             #
//#############################################
Algoritmo inventarioLibros
	
	Definir titulo, autor, tipoLibro, disponible, editorial, ubicacion como caracter
	Definir total, cantidad, qpaginas, year, i Como Entero
	Definir libros como caracter
	Dimension libros[1000000,9]
	
	//INICIALIZAR VARIABLES
	
	titulo<-''
	autor<-''
	tipoLibro<-''
	disponible<-''
	editorial<-''
	ubicacion<-''
	total<-0
	cantidad<-0
	qpaginas<-0
	year<-0
	i<-1
	
	Escribir "---------------------------------------------------------------"
	Escribir "-       BIENVENIDOS AL REGISTRO DE INVENTARIO DE LIBROS      -"
	Escribir "---------------------------------------------------------------"
	Escribir "                                               "
	Escribir "Ingrese la cantidad de LIBROS a Registrar:"
	
	leer total
	
	Para i<-1 Hasta total Hacer
		Escribir "Ingrese el titulo  del libro ",i,":" //solicitando Nombre y Apellido
		Leer titulo
		libros[i,1]=titulo //Guardando la marca del caucgo en el arreglo libros
		Escribir "Ingrese el autor del libro ",i,":"
		leer autor
		libros[i,2]=autor
		Escribir "Ingrese el tipo de libro ",i,":"
		Leer tipoLibro
		libros[i,3]=tipoLibro
		Escribir "Indique si el libro ",i,"está disponible (Escribe SI o NO):"
		Leer disponible
		libros[i,4]=disponible
		Escribir "Ingrese la editorial del libro ",titulo,":"
		Leer editorial
		libros[i,5]=editorial
		Escribir "Ingrese la cantidad de libros ",titulo,":"
		Leer cantidad
		libros[i,6]=ConvertirATexto(cantidad)
		Escribir "Ingrese la cantidad de páginas del libro ",titulo,":"
		Leer qpaginas
		libros[i,7]=ConvertirATexto(qpaginas)
		Escribir "Ingrese el año del libro ",titulo,":"
		Leer year
		libros[i,8]=ConvertirATexto(year)
		Escribir "Ingrese la Ubicación Física del libro ",titulo,":"
		Leer ubicacion
		libros[i,9]=ubicacion
		
	FinPara
	
	Imprimir  "Gracias por ingresar los datos, por favor presione cualquier tecla para continuar"
	
	Esperar Tecla
	
	Limpiar Pantalla
	//MOSTRANDO LOS DATOS
	Escribir "------------------------------"
	Escribir "- Usted ingresó estos datos: -"
	Escribir "------------------------------"
	i<-1
	
	Escribir " Titulo | Autor | Tipo de Libro | Disponibilidad | Editorial | Cantidad de Libros | Cantidad de Páginas | Año | Ubicación del Libro"	
	
	Para i<-1 Hasta total Hacer
		Escribir "| ",libros[i,1]," | ",libros[i,2]," | ",libros[i,3]," | ",libros[i,4]," | ", libros[i,5]," | ",libros[i,6]," | ",libros[i,7]," | ",libros[i,8]," | " ,libros[i,9]
		
	FinPara
	
	
	
FinAlgoritmo
