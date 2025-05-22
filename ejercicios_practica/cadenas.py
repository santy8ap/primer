# #Escribir un programa que pregunte el nombre de
# #usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

# name = input("Como te llamas: ")
# n = input("introduce un numero entero: ")
# print ((name + "\n") * int(n))


# #Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces,
# #una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra de
# #nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

# name = input("como te llamas? ")
# print(name.lower())
# print(name.upper())
# print(name.title())

# #Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre 
# # por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.

# name = input("¿Como te llamas? ")
# print(name.upper() + " tiene " + str(len(name)) + " letras ")

# #Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34,
# #  y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa
# #  que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.

# tel = input("Introduce un numero de telefono con el formato +57 ")
# print('El numero de telefono es: ', tel[4:-3])



# #Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.

# frase = input("Introduce una frase: ")
# print(frase[::-1])

# #Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal en minúscula,
# #  y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.+

# frase = input("Introduce una frase: ")
# vocal = input("introduce una vocal en minuscula: ")
# print(frase.replace(vocal, vocal.upper()))


# #Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por 
# # pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio riwi.es.

# email = input("Introduce el nombre que quieres para tu correo: ")
# print ("tu correo es: " + email[:email.find('@')] + '@Riwi.io')

# #Escribir un programa que pregunte por consola el precio de un
# #producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.

# precio = input("introduce el precio en euros con 2 decimanles: ")
# print("el precio es: " + precio[:precio.find('.')], 'euros y', precio[precio.find('.') + 1:], "centimos")


# #Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año.

# fecha = input("introduce tu fecha de nacimiento en formato dia/mes/año: ")
# dia = fecha [:fecha.find('/')]
# mes_a = fecha [:fecha.find('/')+1:]
# mes =  mes_a [:mes_a.find('/')]
# year = mes_a [:mes_a.find('/') +1]
# print('dia', dia)
# print('mes', mes)
# print('año', year)


# #Escribir un programa que pregunte por consola por los productos de una cesta de la compra,
# #  separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.

# cesta = input('Introduce los productos de la cesta de la compra separados por comas: ')
# print(cesta.replace(',', '\n'))



# #Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el siguiente formato:

# #<producto>: <unidades> unidades x <precio>€ = <total>€

# #donde <unidades> es el número de unidades con cinco dígitos, <precio> es el precio unitario con 6 dígitos enteros y 2 decimales y <total> es el coste total con 8 dígitos enteros y 2 decimales.

# producto = input('Introduce el nombre del producto: ')
# precio = float(input('Introduce el precio unitario: '))
# unidades = int(input('Introduce el numero de unidades: '))
# print('{producto}: {unidades:3d} unidades x {precio:9.2f}€ = {total:11.2f}€'.format(producto = producto, unidades = unidades, precio = precio, total = unidades * precio))


# nombres = {"ana":1,"pepito":2, "juan":3,}
# print("el tipo de de nombre es: ", type(nombres))
# for nombre, valor in nombres.items():
#     print("buenos dias", nombre, valor)

# for i in range(1,10):
#     if i % 3 == 0 and i % 5 ==0:
#        print("fizzbazz")
#     elif i % 3==0:
#         print("fizz")
#     elif i % 5==0:
#         print("buzz")
#     else:
#         print(i)

# for x in  range(0,5):
#     print("hola el numero es: ",x)

# for x in  "hola":
#     print(x)

#     nombres = ("ana", "juan", "maria")

#     for nombre in nombres:
#         print(nombre)

# for i in range(5):
#     print(f"numero de rango {i}")
# from statistics import mean

# lista = []
# n = int(input("ingrese la cantidad de notas que desea \
# promediar:"))
# for i in range(1, n+1):
#     lista.append(int(input(f"ingrese la nota numero {i}: ")))

#     lista.sort()

#     print(f"la lista de notas ingresadas {lista}")
#     print(f"el promedio de las notas es: {mean(lista): .2f}")

# from pickle import TRUE

# from ejercicios_practica import practicando2


# def main():
#     print("Pares e impares")
    
#     numero_1 = int(input("Escriba un numero entero: "))
#     numero_2 = int(input(f"Escriba un numero entero o mayor o igual que {numero_1}: "))



#     while True:
#         if numero_2 < numero_1:
#             print(f"El numero que ingresaste no es mayor que {numero_1}")
#             numero_2 = int(input("Inténtelo otra vez, ingrese un número entero mayor o igual que el primero: "))

#         else:
#             for i in range(numero_1, numero_2 + 1):
#                 if i % 2 == 0:
#                     print(f"EL NUMERO {i} ES PAR")
#                     numero_1 = int(input("Escriba otro numero entero: "))
#                 else:
#                     print(f"EL NUMERO {i} ES IMPAR")
#                     numero_1 = int(input("Escriba otro numero entero: "))
        
# if __name__ == "__main__":
#     main()

# #esto es un comentario

# #tipos de variables

# caja1 = 123456
# caja1 = 3.1415
# caja1 = True
# Caja1 = "The cake is lie"


# #si las variables tienen numeros

# numero1 = 8
# numero2 = 2

# suma = numero1 + numero2
# resta = numero1 - numero2
# multiplicacion = numero1 * numero2
# division = numero1 / numero2

# #si la vasriables son tipo str

# palabra1 = "El pastel"
# palabra2 = "es mentira"

# frase = palabra1 + palabra2

# #funciones
# #nombrefuncion (argumento1, arguemento2, argumento3 ..... argumentoN)

# print("Alabado seas mi  jesus")
# print(2025)
# print(1.1416)
# print(False)
# print(numero1, numero2)
# print(suma, resta, multiplicacion, division)
# print(frase)

# #funcion suma

# def suma  (num1, num2):
#     return num1 + num2
# print(suma(5,3))


# numero1 = 5
# numero2 = 4

# print("La suma de",numero1,"y",numero2,"es",suma(numero1,numero2))


# #Funcion media

# def mediaNumeros(num1, num2):
#     media = num1 + num2
#     media = media/2
#     return media


# print(mediaNumeros(5,2))

# #funcion insulta

# def insulta(nombre):
#     print(nombre,"es una persona de dudosa inteligencia")

# insulta("BitBoss")

# #lista

# fibonaci = [0,12,32,43,78,45,78,34]

 

# print(fibonaci[3])
# print(fibonaci[5])

# cosas = [0,5,2,True,"mac"]

# print(cosas[0],cosas[3],cosas[1],cosas[0])
# print(cosas)

# print(len(cosas))

# #metodos

# print("Antes", fibonaci)
# fibonaci.append(91)
# print("Despues de apped",fibonaci)

# fibonaci.insert(7,True)
# print("despues de inserte", fibonaci)

# #IF-ELSE

# #if ValorBolean:
# #   bloque de codigo

# insultado = True

# if insultado:
#     print("ey tu, si tu ven pa aca")


import random

numero_secreto = random.randint(1,100)

max_intentos = 10
intentos=0

print("Bienvenido al juego de adivinar el número")
print("Tienes que adivinar un número entre 0 y 100:")
print("Tendras 10 intentos. El sistema te dira si estas caliente o frio.")
while intentos < max_intentos:
    try:
        numero_usuario= int(input(f"intento{intentos+1}/{max_intentos}-ingresa un numero: "))

        if numero_usuario < 0 or numero_usuario > 100:
          print("Por favor, Escribe un número de 0 a 100.\n")
          continue
        intentos+=1

        if numero_usuario==numero_secreto:
           print(f" ¡Felicidades! Adivinaste el número en {intentos} intento(s).")
           break
        else:
            diferencia=abs(numero_usuario-numero_secreto)
            if diferencia <=5:  
             print("Muy caliente\n")
            elif diferencia <=15:
             print("Caliente\n")
            elif diferencia <=30:
             print("Frio\n")
            else:
             print("Muy frio\n")

    except ValueError:
     print("por favor ingresa solo numeros.\n")
if intentos==max_intentos and numero_usuario != numero_secreto:
         print(f"Has usado todos tus intentos. El número correcto era:{numero_secreto}")
