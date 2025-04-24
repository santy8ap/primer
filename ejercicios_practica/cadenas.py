#Escribir un programa que pregunte el nombre de
#usuario en la consola y un número entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces como el número introducido.

name = input("Como te llamas: ")
n = input("introduce un numero entero: ")
print ((name + "\n") * int(n))


#Escribir un programa que pregunte el nombre completo del usuario en la consola y después muestre por pantalla el nombre completo del usuario tres veces,
#una con todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la primera letra de
#nombre y de los apellidos en mayúscula. El usuario puede introducir su nombre combinando mayúsculas y minúsculas como quiera.

name = input("como te llamas? ")
print(name.lower())
print(name.upper())
print(name.title())

#Escribir un programa que pregunte el nombre del usuario en la consola y después de que el usuario lo introduzca muestre 
# por pantalla <NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en mayúsculas y <n> es el número de letras que tienen el nombre.

name = input("¿Como te llamas? ")
print(name.upper() + " tiene " + str(len(name)) + " letras ")

#Los teléfonos de una empresa tienen el siguiente formato prefijo-número-extension donde el prefijo es el código del país +34,
#  y la extensión tiene dos dígitos (por ejemplo +34-913724710-56). Escribir un programa
#  que pregunte por un número de teléfono con este formato y muestre por pantalla el número de teléfono sin el prefijo y la extensión.

tel = input("Introduce un numero de telefono con el formato +57 ")
print('El numero de telefono es: ', tel[4:-3])



#Escribir un programa que pida al usuario que introduzca una frase en la consola y muestre por pantalla la frase invertida.

frase = input("Introduce una frase: ")
print(frase[::-1])

#Escribir un programa que pida al usuario que introduzca una frase en la consola y una vocal en minúscula,
#  y después muestre por pantalla la misma frase pero con la vocal introducida en mayúscula.+

frase = input("Introduce una frase: ")
vocal = input("introduce una vocal en minuscula: ")
print(frase.replace(vocal, vocal.upper()))


#Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por 
# pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio riwi.es.

email = input("Introduce el nombre que quieres para tu correo: ")
print ("tu correo es: " + email[:email.find('@')] + '@Riwi.io')

#Escribir un programa que pregunte por consola el precio de un
#producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.

precio = input("introduce el precio en euros con 2 decimanles: ")
print("el precio es: " + precio[:precio.find('.')], 'euros y', precio[precio.find('.') + 1:], "centimos")


#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año.