#############################################
# Nombre del Programa: Registrar Inventario #
# de libros en una biblioteca	y listarlos	#
# Autor: MOnica Tahan                       #
#VersiOn: 1.0                               #
#DescripciOn: programa para registrar el    #
#inventario de libros por autor             #
#############################################

# INICIALIZANDO LAS VARIABLES NECESARIAS
titulo=''
autor=''
tipoLibro=''
disponible=''
editorial=''
ubicacion=''
total=0
cantidad=0
qpaginas=0
year=0
terminar='C'
libros = {
              "Titulo" : titulo,
              "Tutor" : autor,
              "Tipo_libro" : tipoLibro,
              "Disponible" : disponible,
              "Editorial" : editorial,
              "Ubicacion" : ubicacion,
              "Total" : total,
              "Cantidad" : cantidad,
              "Cantidad_Paginas" : qpaginas,
              "Year" : year
            }

print("===========================================================")
print("=Bienvenidos al programa de ingreso de libros de la UNEXPO=")
print("===========================================================")


while terminar =='C' or terminar=='c':

    titulo = (input("Indique el titulo del libro: "))
    autor = (input("Indique el autor del libro: "))
    tipoLibro = (input("Indique el tipo de libro: "))
    disponible = (input("Indique si está disponible (Si para firmar, No para indicar que no está disponible): "))
    editorial = (input("Indique la editorial del libro: "))
    ubicacion= (input("Indique la ubicación del libro: "))
    total = (input("Indique el total de ejemplares disponibles: "))
    cantidad = (input("Indique la cantidad de ejemplares del libro: "))
    qpaginas = (input("Indique la cantidad de páginas del libro: "))
    year = (input("Indique el año de publicación del libro: "))

    libros = {
              "Titulo" : titulo,
              "Tutor" : autor,
              "Tipo_libro" : tipoLibro,
              "Disponible" : disponible,
              "Editorial" : editorial,
              "Ubicacion" : ubicacion,
              "Total" : total,
              "Cantidad" : cantidad,
              "Cantidad_Paginas" : qpaginas,
              "Year" : year
            }
    terminar = (input("Presione T o t para terminar, sino, C o c para continuar"))
    print(terminar)

print(libros)