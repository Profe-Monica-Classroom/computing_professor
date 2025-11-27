Algoritmo inventarioLibros
	//#############################################
	//# Nombre del Programa: Registrar Inventario #
	//# de libros en una biblioteca	y listarlos	  #
	//# Autor: Mónica Tahan y Alumnos Comp. 1. S37#
	//#Versión: 1.1                               #
	//#Descripción: programa para registrar el    #
	//#inventario de libros por autor             #
	//#############################################	
	
	Definir total, qpaginas, cantidad, i, j Como Entero
	Definir titulo, autor como cadena
	Definir editorial, disponible, libros, ubicacion, tipolibro  Como Caracter
	Dimension libros[1000000,9]
	
	//INICIALIZAR VARIABLES
	
	titulo<-''
	autor<-''
	tipolibro<-''
	disponible<-''
	editorial<-''
	ubicacion<-''
	total<-0
	cantidad<-0
	qpaginas<-0
	year<-0
	i<-1
	
	
	//INICIO DEL PROGRAMA
	Escribir "-----------------------------------------------------------------"
	Escribir "- Bienvenido al PROGRAMA DE REGISTRO de Libros de la Biblioteca -"
	Escribir "-----------------------------------------------------------------"
	
	Escribir "Por favor indique la cantidad de libros a registrar: "
	leer total
	
	Escribir "A continuación usted debe indicar los datos que el sistema le solicite:"
	
	Para i<-1 Hasta total Hacer
		Escribir "Ingrese el titulo  del libro ",i,": "
		leer titulo
		libros[i,1]=titulo //Guardando el titulo
		Escribir "Ingrese el autor del libro ",i,": "
		leer autor
		libros[i,2]=autor
		Escribir "Ingrese el tipo de libro ",i,": "
		Leer tipoLibro
		libros[i,3]=tipolibro
		Escribir "Indique si el libro ",i,"está disponible (Escribe SI o NO): "
		Leer disponible
		libros[i,4]=disponible
		Escribir "Ingrese la editorial del libro ",titulo,": "
		Leer editorial
		libros[i,5]=editorial
		Escribir "Ingrese la cantidad de libros ",titulo,": "
		Leer cantidad
		libros[i,6]=ConvertirATexto(cantidad)
		Escribir "Ingrese la cantidad de páginas del libro ",titulo,": "
		Leer qpaginas
		libros[i,7]=ConvertirATexto(qpaginas)
		Escribir "Ingrese el año del libro ",titulo,": "
		Leer year
		libros[i,8]=ConvertirATexto(year)
		Escribir "Ingrese la Ubicación Física del libro ",titulo,": "
		Leer ubicacion
		libros[i,9]=ubicacion
	FinPara
	
	Imprimir  "****** Gracias por ingresar los datos, por favor presione cualquier tecla para continuar *****"
	
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
