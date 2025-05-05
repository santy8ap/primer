# def aplicar_descuento(precio, descuento):

#     return precio - precio * descuento / 100

# def aplicar_iva(precio, porcentaje):

#     return precio + precio * porcentaje / 100

# def precio_canasta_familiar(canasta, funcion):

#     total = 0 
#     for precio, descuento in canasta.items():
#         total += funcion(precio, descuento)
#     return total
    
# print('El precio de la compra tras aplicar los descuentos es: ', precio_canasta_familiar({1000: 20, 500: 10, 100: 1}, aplicar_descuento))
# print('El precio de la compra después del IVA es: ', precio_canasta_familiar({1000: 0, 500: 0, 100: 0}, aplicar_iva))

from math import sin, cos, tan, exp, log

def aplicar_funcion(f, n):
     '''
    Función que aplica una función a los enteros desde 1 hasta n.
    Parámetros:
        f: Es una función que recibe un número real y devuelve otro.
        n: Es un número entero positivo.
    Devuelve:
        Un diccionario con los pares i:f(i) para cada valor entero i de 1 a n.
    '''
     functions = {'sin':sin, 'cos':cos, 'tan':tan, 'exp':exp, 'log':log}
     resultado = {}
     for i in range(1, n+1):
          resultado[i] = functions[f](i)
          return
