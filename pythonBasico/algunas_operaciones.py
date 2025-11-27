x = True
y = False
z = x and not y
w = not y #convierte al valor de y en su valor negado, es decir si es True sera False y viceversa
print(z)

""" La operacion logica and not en la siguiente expresion:
z = x and not y primero aplicara la operacion not a y,
luego la operacion and con el valor que habia en x

Esto significa que si x es True y (y) es False, entonces (not y) sera True, por lo que z sera True.
Si x es True y (y) es True, entonces (not y) sera False, por lo que z sera False.
"""