# Paso 1: Solicitar al usuario una calificación numérica entre 0 y 100 y validarla
while True:
    grade = int(input("Ingresa una calificación entre 0 y 100: "))
    if 0 <= grade <= 100:
        break  # Si es válida, salimos del bucle
    print("La calificación que ingresaste no está en un rango válido.")

# Paso 2: Determinar si la calificación es de aprobación o no
if grade >= 70:
    print("Has aprobado, ¡felicidades!")
else:
    print("Has reprobado.")

# Paso 3: Solicitar al usuario una lista de calificaciones (separadas por comas)
input_string = input("Ingrese una lista de calificaciones (separadas por comas, entre 0 y 10): ")

# Convertimos la cadena de entrada en una lista de números flotantes
grades_list = [float(g.strip()) for g in input_string.split(',') if g.strip() != ""]

# Mostramos las calificaciones ingresadas
print("Calificaciones ingresadas:", grades_list)

# Paso 4: Calcular el promedio usando un ciclo for
sum_grades = 0  # Inicializamos la suma
for g in grades_list:
    sum_grades += g  # Acumulamos cada calificación

average = sum_grades / len(grades_list)  # Calculamos el promedio
print("Promedio de calificaciones:", average)

# Paso 5: Contar cuántas calificaciones son mayores que un valor específico (usando while)
filter_value = float(input("Ingrese un valor específico para filtrar: "))

i = 0
count_greater = 0  # Contador de calificaciones mayores

while i < len(grades_list):
    if grades_list[i] > filter_value:
        count_greater += 1  # Si es mayor, incrementamos el contador
    i += 1  # Avanzamos al siguiente índice

print(f"Cantidad de calificaciones mayores que {filter_value}: {count_greater}")

# Paso 6: Verificar y contar cuántas veces aparece una calificación específica
# usando break y continue para controlar el flujo del ciclo
search_value = float(input("Ingrese una calificación específica que desea buscar: "))
count_found = 0  # Inicializamos el contador de coincidencias

for grade in grades_list:
    if grade < 0 or grade > 10:
        continue  # Si el valor no está en el rango válido, lo ignoramos
    if grade == search_value:
        count_found += 1  # Si coincide, aumentamos el contador
    if count_found >= 5:
        print("Se encontró esta calificación 5 veces, se detiene la búsqueda.")
        break  # Terminamos el ciclo si ya se encontró muchas veces

# Mostramos el resultado final de la búsqueda
if count_found == 0:
    print(f"La calificación {search_value} no está en la lista.")
else:
    print(f"La calificación {search_value} aparece {count_found} veces.")
