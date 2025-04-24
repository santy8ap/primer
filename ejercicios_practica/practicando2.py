horas = float(input("Iingrese el numero de horas trabajadas: "))
coste = float(input("Ingrese lo que cobras por hora: "))

paga = horas * coste

print("su paga es:",paga)

#Escribir un programa que pregunte al usuario una cantidad a invertir, 
# el interés porcentual anual y el número de años, y muestre por pantalla el capital obtenido en la inversión redondeado con dos decimales.

cantidad = float(input("Cantidad que deseas invertir: "))
interes = float(input("Interes porcentual anual: "))
age = int(input("cuantos años: "))

print("Capital final: " + str(round(cantidad * (interes / 100 + 1 ) ** age, 2)))



#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de 
# logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. 
# Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa
#  que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.

peso_payaso = 112
peso_muñeca = 75
payasos = int(input("introduce el numero de payasos que va enviar: "))
muñecas =int(input("introduce  el numero de muñecas que va enviar: "))

peso_total = peso_payaso * payasos + peso_muñeca + muñecas

print("el peso total de paquete es de: "+  str(peso_total))


#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, 
# que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo 
# la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y
#  mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales. 

inversion = float(input("Introduce la inversion inicial: "))
interes = 00.4
balance1 = inversion * (1 + interes)
print("balance tras el primer año; " + str(round(balance1, 2)))
balance2 = inversion * (1 + interes)
print("balance tras el segundo año: " + str(round(balance2, 2)))
balance3 = inversion * (1 + interes)
print("balance tras el tercer año:" + str(round(balance3, 2)))



#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%.
#Escribe un programa que comience leyendo el número de barras vendidas que no son del
#día. Después tu programa debe mostrar el precio habitual de una barra de pan, el descuento que se le hace por no ser fresca y el coste final total. 

barras = int(input("introduce el numero de barras vendidas que no son frescas: "))
precio = 3.99
descuento = 0,6
coste = barras + precio * (1 - descuento)
print("el precio de una barra fresca es de: " + str(precio) + "€")
print("el descuento de una barras no fresca es de: " +str(descuento * 100) + "%")
print("el coste final a pagar es de: " +str(round(coste, 2)) + "€")

