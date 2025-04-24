#se le pide al usuario que ingrese el nombre del producto que desea llevar
nom_pro = input("Ingrese el nombre del producto: ")

#se le pide que ingrese el precio
pre_u = int(input("Ingrese el precio de la unidad: "))

#se hace la verificacion de que el precio no sea menor a 0 y si es precio es menor o 
# igual a cero vuelve a entrar en el ciclo
while pre_u <= 0:
    print("El precio de la unidad no es valido")
    pre_u = int(input("Ingrese el precio de la unidad: "))

#se le pide al usuario que ingrese la cantidad de productos que desea llevar
canti_ad = int(input("Ingrese la cantidad: "))

#se hace la verificacion de que la cantidad sea mayor o igual a 0 
# y si el parametro no es valido vuelve a entrar en el ciclo
while canti_ad <= 0:
    print ("la cantidad no cumple los parametros")
    canti_ad = int(input("Ingrese la cantidad: "))

#se le pide al usuario que ingrese el descuento
por_des = int(input("Ingrese el descuento: "))

#se hace la verificacion de que el descuento este entre el rango de 0 a 100

while por_des < 0 or por_des >= 100:
    print ("El descuento no cumple los parametros")
    por_des = int(input("Ingrese el descuento: "))

#se crea una variable para calcular el precio por la cantidad

Resultado = pre_u * canti_ad

#se calcula el monto a restar al monto final

descuento = Resultado * (por_des / 100)

#se imprime el resultado
print ("tu te llevaste un: ",nom_pro,"con un precio de: ",pre_u,"una cantidad de:",canti_ad,"con un descuento de:",por_des,"%")
print ("el monto total de la compra es:",int(Resultado) - int(descuento))