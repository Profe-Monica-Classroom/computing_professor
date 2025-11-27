##################################################
# Nombre del Programa: Registrar Publicaciones   #
# de tesis de pregrado en un repositorio de      #
# Publicaciones y listarlas                      #
# Autor: MOnica Tahan                            #
#VersiOn: 1.0                                    #
# Descripcion: programa para registrar  las      #
# publicaciones de Tesis de Pregrado de la Unexpo# 
##################################################
"""
# Nombre del Programa: Registrar Publicaciones   #
# de tesis de pregrado en un repositorio de      #
# Publicaciones y listarlas                      #
# Autor: Monica Tahan                            #
# Version: 1.0                                   #
# DescripciOn: programa para registrar  las      #
# publicaciones de Tesis de Pregrado de la Unexpo# 
# ################################################ 
"""

# INICIALIZANDO LAS VARIABLES NECESARIAS
autor = ''
tpublicacion = ''
year = 0
espec = ''
qpaginas = 0
idioma = ''
codigo = ''
categoria = ''
i = 0

print("=========================================================================================")
print("=Bienvenidos al programa de ingreso de Publicaciones de Tesis de Pregrado de la UNEXPO=")
print("=========================================================================================")

print("A continuación usted debe indicar la operación a realizar:")
print("Escriba 1 para Ingresar Una Publicación.")
print("Escriba 2 para Editar Una Publicación.")
print("Escriba 3 para Listar todas las publicaciones.")
print("Escriba 4 para Buscar una publicación por título.")

operacion = int(input())

if operacion == 1:
    print("Indique el autor de la tesis: ")
    autor = input()
    print("Indique el Título de la publicación: ")
    tpublicacion = input()
    print("Indique el año de la publicación: ")
    year = int(input())
    print("Indique la especialidad de la tesis: ")
    espec = input()
    print("Indique la cantidad de páginas de la tesis: ")
    qpaginas = int(input())
    print("Indique el idioma de la tesis: ")
    idioma = input()
    codigo = str(i)+str(year)+espec
    i+=1
    print("Indique la categoría de la tesis: ")
    categoria = input()

    tesis = {
              "Autor" : autor,
              "Titulo" : tpublicacion,
              "Year" : year,
              "Especialidad" : espec,
              "Paginas" : qpaginas,
              "Idioma" : idioma,
              "Codigo" : codigo,
              "Categoria" : categoria
            }
    
    print("=========================================================================================")
    print("La publicación de la tesis de pregrado: ", tesis)
    print("=========================================================================================")
    print("Autor | Título | Año | Especialidad | Páginas | Idioma | Código | Categoría")
    print(tesis["Autor"]+" | "+tesis["Titulo"]+" | "+str(tesis["Year"])+" | "+tesis["Especialidad"]+" | "+str(tesis["Paginas"])+" | "+tesis["Idioma"]+" | "+tesis["Codigo"]+" | "+tesis["Categoria"])
#elif operacion == 2: