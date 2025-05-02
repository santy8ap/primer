calificacion = int(input("ingrese un valor: "))

while 0 <= calificacion >= 100:
    print("la calificacion que ingresaste no es un rango valido")
    calificacion = int(input("ingrese un valor: "))

if calificacion >= 70:
    print("has aprobado, felicitacionbes")
else:
    print("reprobaste")

calificaciones = []

print("Ingrese 10 calificaciones")

for i in range(10):
    calif = float(input("Ingrese las calificaciónes: "))
    calificaciones.append(calif)
print(calificaciones)  

promedio = sum(calificaciones) / len(calificaciones)#se hace Suma y divide entre el total
print("calificaciones ingresadas: ",calificaciones)
print("promedio: ", promedio)



# Pedir valor específico para comparar
valor_filtro = float(input("Ingrese un valor especifico para filtrar: "))

i = 0
contador = 0

while i < len(calificaciones):
    if calificaciones[i] > valor_filtro:
        contador += 1
    
    i  += 1

print(f"Cantidad de calificaciones mayores que {valor_filtro} son: {contador}")



valor_buscar = float(input("Ingrese una calificacion especifica que buscar"))
contador_encontrados = 0 


for cal in calificaciones:
    if cal < 0 or cal > 10:
        continue  # Salta valores inválidos, por seguridad
    if cal == valor_buscar:
        contador_encontrados += 1
    if contador_encontrados >= 5:  # Ejemplo: si se encuentra muchas veces, se interrumpe
        print("Se encontró esta calificación 5 veces, se detiene la búsqueda.")
        break

if contador_encontrados == 0:
    print(f"La calificación {valor_buscar} no está en la lista.")
else:
    print(f"La calificación {valor_buscar} aparece {contador_encontrados} veces.")