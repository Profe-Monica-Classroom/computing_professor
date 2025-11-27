#############################################
# Nombre del Programa: Registrar Inventario #
# de cauchos en una cauchera	y listarlos	#
# Autor: MOnica Tahan                       #
#VersiOn: 1.0                               #
#DescripciOn: programa para registrar el    #
#inventario de cauchos y su precio             #
#############################################

# INICIALIZANDO LAS VARIABLES NECESARIAS
marca=''
tipo=''
rin=0.0
ancho=0.0
costo=0.0
precio=0.0
cantidad=0
porcentaje=0
simbolo_porcentaje='%'

terminar='C'
cauchos = {
              "Marca" : marca,
              "Tipo" : tipo,
              "Rin" : rin,
              "Ancho" : ancho,
              "Costo" : costo,
              "Precio" : precio,
              "Cantidad" : cantidad,
              "Porcentaje" : porcentaje
            }

print("============================================================")
print("=Bienvenidos al programa de ingreso de Cauchos de la UNEXPO=")
print("============================================================")


while terminar =='C' or terminar=='c':

    marca = (input("Indique la marca del caucho: "))
    ancho = (input("Indique el ancho: "))
    rin = (input("Indique Nro de Rin: "))
    tipo= (input("Indique el Tipo de Caucho: "))
    costo = (input("Indique el costo: "))
    costo=float(costo)
    cantidad = (input("Indique la cantidad de cauchos: "))
    cantidad=int(cantidad)
    porcentaje= (input("Indique el porcentaje de ganancia: "))
    porcentaje=float(porcentaje)
    precio = costo + (costo*porcentaje/100)
   

    cauchos = {
              "Marca" : marca,
              "Tipo" : tipo,
              "Rin" : rin,
              "Ancho" : ancho,
              "Costo" : costo,
              "Precio" : precio,
              "Cantidad" : cantidad,
              "Porcentaje" : porcentaje
            }
    terminar = (input("Presione cualquier tecla para terminar, sino, C o c para continuar"))
    print(terminar)

print(cauchos)
print("| Marca | Tipo | Rin | Ancho | Costo | Cantidad | Porcentaje de Ganancia | Precio |")
for cada_caucho in cauchos:
    print(cauchos[cada_caucho])
    print(cauchos[cada_caucho]," | ", tipo, " | ", rin, " | ", ancho, " | ", str(costo), " | ", 
          cantidad, " | ", str(porcentaje), " ", simbolo_porcentaje, " | ", str(precio))