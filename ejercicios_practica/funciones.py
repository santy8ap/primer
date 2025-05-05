# def Factorial(n):
#     """Funcion que calcula el factorial de un numero entero positivo
#     parámetros
#     n: Es un entero positivo.
#     Devuelve el factorial de n.
#     """
#     tmp = 1
#     for i in range(n):
#         tmp *= i+1
#     return tmp

# print(Factorial(4))
# print(Factorial(20))


# def iva(monto, porcentaje=21):
#     """Funcion de aplicacion del IVA a una factura.
#     Parametros
#     monto: Es la cantidad sin IVA
#     porcentaje: Es el porcentaje de IVA
#     Devuelve el total de la factura una vez aplicado el IVA.
#     """

#     return monto + monto*porcentaje/100


# print(iva(1000,10))
# print(iva(1000))

# def ciculo_area(radio):
#     """Función que calcula el area de un círculo.
#     Parámetros
#     radius: Es el radio del círculo.
#     Devuelve el área del círculo de radio radius. 
#     """
        
#     pi = 3.1415
#     return pi*radio**2

# def volumen_cilindro(radio, altura):
#         """Función que calcula el volumen de un cilindro.
#     Parámetros
#     radius: Es el radio de la base del cilindro.
#     high: Es la altura del cilindro.
#     Devuelve el volumen del clindro de radio radius y altura high.
#     """
#         return ciculo_area(radio)*altura

# print(ciculo_area(3,5))


# def promedio(*muestra):
    
#     return sum(muestra)/len(muestra)

# print (promedio(1,2,3,4,5))
# print (promedio(2.3, 5.7, 6.8, 9.7, 15.6))



# def cuadrado(*muestra):

#     list = []
#     for i in muestra:
#         list.append(i**2)
#     return list

# def estadisticas(muestra):
    
#     dato = {}
#     dato['media'] = sum (muestra)/len(muestra)
#     dato['varianza'] = sum(cuadrado(*muestra))/len(muestra)-dato['media']**2
#     dato['desviacion tipica'] = dato['varianza']**0.5
#     return dato

# print(cuadrado(1, 2, 3, 4, 5))
# print(cuadrado(2.3, 5.7, 6.8, 9.7, 12.1, 15.6))

# def minimo_comun_divisor(n, m):
#     """Función que calcula el máximo común divisor de dos números.
#     Parámetros:
#         - n: Es un número entero.
#         - m: Es un número entero.
#     Devuelve:
#         El máximo común divisor de n y m.
#     """
#     rest = 0
#     while(m > 0):
#         rest = m
#         m = n % m
#         n = rest
#     return n  


# def minimo_comun_multiplo(n, m):
#     """Función que calcula el mínimo común múltiplo de dos números.
#     Parámetros:
#         - n: Es un número entero.
#         - m: Es un número entero.
#     Devuelve:
#         El mínimo común múltiplo de n y m.
#     """

#     if n > m:
#         mayor = n
#     else:
#         mayor = m
#     while (mayor % n != 0) or (mayor % m != 0):
#         mayor += 1
#     return mayor

# print(minimo_comun_divisor(24,36))
# print(minimo_comun_multiplo(24,36))

# def to_decimal(n):
#     """Función que convierte un número binario en decimal.
#     Parámetros:
#         - n: Es una cadena de ceros y unos.
#     Devuelve:
#         El número decimal correspondiente a n.
#     """
#     n = list(n)
#     n.reverse()
#     decimal = 0
#     for i in range(len(n)):
#         decimal += int(n[i]) * 2 ** i
#     return decimal

# def to_binary(n):
#     """Función que convierte un número decimal en binario.
#     Parámetros:
#         - n: Es un número entero.
#     Devuelve:
#         El número binario correspondiente a n.
#     """
#     binary = []
#     while n > 0:
#         binary.append(str(n % 2))
#         n //= 2
#     binary.reverse()
#     return ''.join(binary)

# print(to_decimal('10110'))
# print(to_binary(22))
# print(to_decimal(to_binary(22)))
# print(to_binary(to_decimal('10110')))

# def contador_palabras (text):
#     """Funcion que cuenta el numero de veces que aparece cada palabra en un texto.
#     Parametros: 
#             - Text: Es una cadena de caracteres.
#     Devuelve: 
#             Un diccionario con pares palabra: frecuencia con las palabras contenidas en el texto y su frecuencia.
#     """

#     text = text.split()
#     palabras = {}
#     for i in text:
#         if i in palabras:
#             palabras[i] += 1
#         else:
#             palabras[i] = 1
#     return palabras

# def repetir(palabras):
#     max_palabras = ''
#     max_frecuencia = 0
#     for palabras, frecuencia in palabras.items():
#         if frecuencia > max_frecuencia:
#             max_palabras = palabras
#             max_frecuencia = frecuencia
#     return max_palabras,max_frecuencia

# text = "Aqui manda Dios, un dia se va cumplir lo que Dios me a prometido, yo me siento bendecido TODAVIA NO ESTOY VENCIDO"
# print(contador_palabras(text))
# print(repetir(contador_palabras(text)))
