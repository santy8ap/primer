#Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e 
# imprima por pantalla si la contraseña introducida 
# por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

key = "contraseña"
password = input("introduce la contraseña: ")

if key == password.lower():
    print("La contraseña coincide")
else:
    print("La contraseña no coincide")

#Escribir un programa que pida al usuario dos números y devuelva su división. 
# Si el usuario no introduce números debe devolver un aviso de error y si el divisor es cero también.

num1 = float(input("Introduce el divisor: "))
dividor = float(input("Introduce el divisor: "))
if dividor == 0:
    print("¡Error! No se puede dividir por 0.")
else:
    print(num1/dividor)



#Escribir un programa que pida al usuario un número entero y muestre por pantalla si es par o impar.

nume1 = int(input("Introduce un numero entero: "))
if nume1 % 2 == 0:
    print("El Numero " + str(nume1) + " es par")
else:
    print("El numero " + str(nume1) + " es impar")



#Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos superiores a 1000 € mensuales. 
# Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

age = int(input("ingrese su edad: "))
ingresos = float(input("ingrese su salario: "))

if age > 16 and ingresos >= 1000:
    print("tienes que cotizar")
else:
    print("no tiens que cotizar")

#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre.
#  El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la N y el grupo B por el resto. 
# Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

name = input("como te llams?")
genero = input("Cual es tu sexo (M O F)")

if genero == "M":
    if name.lower () < "m":
        group = "A"
    else:
        group = "B"
else: 
    if name.lower() > "n":
        group = "A"
    else:
        group = "B"
print("Tu grupo es " + group)

#Los tramos impositivos para la declaración de la renta en un determinado país son los siguientes:
#Renta 	Tipo impositivo
#Menos de 10000€ 	5%
#Entre 10000€ y 20000€ 	15%
#Entre 20000€ y 35000€ 	20%
#Entre 35000€ y 60000€ 	30%
#Más de 60000€ 	45%

#Escribir un programa que pregunte al usuario su renta anual y muestre por pantalla lo que tiene que pagar.


#preguntar al usuario por la renta
renta =  float(input("¿Cual es tu renta anual? "))
# Condicional para determinar el tipo impositivo dependiendo de la renta
if renta < 10000:
    tipo = 5
elif renta < 20000:
    tipo = 15
elif renta < 35000:
    tipo = 20
elif renta < 60000:
    tipo = 30
else:
    tipo = 45

print("tienes que pagar ", renta * tipo / 100, "€", sep='')


#En una determinada empresa, sus empleados son evaluados al final de cada año. Los puntos que pueden obtener en la evaluación comienzan en 0.0 y pueden ir aumentando, traduciéndose en mejores beneficios. Los puntos que pueden conseguir los empleados pueden ser 0.0, 0.4. o 0.6, pero no valores intermedios entre las cifras mencionadas. A continuación se muestra una tabla con los niveles correspondientes a cada puntuación. La cantidad de dinero conseguida en cada nivel es de 2.400€ multiplicada por la puntuación del nivel.
#Nivel 	Puntuación
#Inaceptable 	0.0
#Aceptable 	0.4
#Meritorio 	0.6

#Escribir un programa que lea la puntuación del usuario e indique su nivel de rendimiento, así como la cantidad de dinero que recibirá el usuario.

bonificacion = 2400
inaceptale = 0
aceptable = 0.4
merito = 0.6

puntos = float(input("Introduce tu puntuacion: "))
# Clasifiación por niveles de rendimiento
if puntos == inaceptale:
    nivel = "inaceptable"
elif puntos == aceptable:
    nivel = aceptable
elif puntos == merito:
    nivel = "meritorio"
else:
    nivel = ""
# Mostrar nivel de rendimiento
if nivel == "":
    print("Esta puntuacion no es valida")
else:
    print("Tu nivel de rendimiento es %s" % nivel)
    print("Te corresponde cobra %.2f€" % (puntos * bonificacion))


#Escribir un programa para una empresa que tiene salas de juegos para todas las edades y quiere calcular de forma automática el precio que debe cobrar a sus clientes por entrar. El programa debe preguntar al usuario la edad del cliente y mostrar el precio de la entrada. Si el cliente es menor de 4 años puede entrar gratis, si 
# tiene entre 4 y 18 años debe pagar 5€ y si es mayor de 18 años, 10€.

edad = int(input("Ingrese su edad: "))

if edad <= 4:
    print("eres menor debes pagar 5€")
elif edad >= 18:
    print("eres mayor paga 10€")

#La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes. Los ingredientes para cada tipo de pizza aparecen a continuación.

    #ngredientes vegetarianos: Pimiento y tofu.
    #Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

#Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y en función de su respuesta le muestre un menú con los ingredientes disponibles para que elija. Solo se puede eligir un ingrediente además de la mozzarella y el tomate que están en todas la pizzas. Al final se debe mostrar por pantalla si la pizza elegida 
#es vegetariana o no y todos los ingredientes que lleva.

print("Bienvenido a la pizzeria bella napoli. \nTipos de Pizza\n\t 1- Vegetariana\n\t2- No vegetariana\n")
tipo = input("Introduce el numero correspondiente al tipo de pizza que quieres: ")
#Decisio sobre el tipo de pizza 
if tipo == "1":
    print("Ingrediente de pizzas vegetarianas\n\ t 1- Pimiento  \n\t2- Tofu\n")
    ingrediente = input("Introduce el ingrediente que deseas: ")
    print("Pizza vegetariana con mozzarella, tomate y ", edad="")
    if ingrediente == "1":
        print("pimiento")
    else: 
        print("tofu")

else:
    print("Ingredientes de pizza vegetarianas\n\t1- Peperoni\n\t2- Jamón\n\t3- Salmón\n")
    ingrediente = input("Introduce el ingrediente que deseas: ")
    print("Pizza no vegetariana con mozarella, tomate y ", end="En camino")
    if ingrediente == "1":
        print("peperoni")
    elif ingrediente == "2":
        print("Jamon")
    else:
        print("salmon")