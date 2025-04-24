#se le pide al usuario que ingrese el nombre del producto que desea llevar
Name = input("Ingrese el nombre del producto: ")

#se le pide que ingrese el precio
Price = int(input("Ingrese el precio de la unidad: "))

#se hace la verificacion de que el precio no sea menor a 0 y si es precio es menor o 
# igual a cero vuelve a entrar en el ciclo
while Price <= 0:
    print("El precio de la unidad no es valido")
    Price = int(input("Ingrese el precio de la unidad: "))

#se le pide al usuario que ingrese la cantidad de productos que desea llevar
Quantity = int(input("Ingrese la cantidad: "))

#se hace la verificacion de que la cantidad sea mayor o igual a 0 
# y si el parametro no es valido vuelve a entrar en el ciclo
while Quantity <= 0:
    print ("la cantidad no cumple los parametros")
    Quantity = int(input("Ingrese la cantidad: "))

#se le pide al usuario que ingrese el descuento
perDisc = int(input("Ingrese el descuento: "))

#se hace la verificacion de que el descuento este entre el rango de 0 a 100

while perDisc < 0 or perDisc >= 100:
    print ("El descuento no cumple los parametros")
    perDisc = int(input("Ingrese el descuento: "))

#se crea una variable para calcular el precio por la cantidad

Result = Price * Quantity

#se calcula el monto a restar al monto final

Disc = Result * (perDisc / 100)

#se imprime el resultado
print ("tu te llevaste un: ",Name,"con un precio de: ",Price,"una cantidad de:",Quantity,"con un descuento de:",perDisc,"%")
print ("el monto total de la compra es:",(Result) - (Disc))