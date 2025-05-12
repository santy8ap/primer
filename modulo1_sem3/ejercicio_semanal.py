# Inventario inicial
inventario = []

def nombre_producto():
    while True:
        nombre = input("Ingrese el nombre del producto: ").strip()
        if nombre and nombre.isalpha():
            return nombre
        print("El nombre del producto debe contener solo letras y no estar vacío.")

def solicitar_precio():
    while True:
        try:
            precio = float(input("Ingrese el precio del producto: "))
            if precio >= 0:
                return precio
            print("El precio no puede ser negativo.")
        except ValueError:
            print("Precio no válido, ingrese un número.")

def cantidad_productos():
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad del producto: "))
            if cantidad >= 0:
                return cantidad
            print("La cantidad no puede ser negativa.")
        except ValueError:
            print("Cantidad no válida, ingrese un número entero.")

def añadir_producto(nombre, precio, cantidad):
    inventario.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
    print(f"Producto '{nombre}' añadido al inventario.")

def mostrar_productos():
    if inventario:
        print("Productos en el inventario:")
        for producto in inventario:
            print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")
    else:
        print("El inventario está vacío.")

def buscar_producto(nombre):
    for producto in inventario:
        if producto["nombre"].lower() == nombre.lower():
            return producto
    return None

def actualizar_precio(nombre, nuevo_precio):
    producto = buscar_producto(nombre)
    if producto:
        producto["precio"] = nuevo_precio
        print(f"Precio del producto '{nombre}' actualizado a {nuevo_precio}.")
    else:
        print(f"Producto '{nombre}' no encontrado.")

def eliminar_producto(nombre):
    global inventario
    producto = buscar_producto(nombre)
    if producto:
        inventario = [p for p in inventario if p["nombre"].lower() != nombre.lower()]
        print(f"Producto '{nombre}' eliminado del inventario.")
    else:
        print(f"Producto '{nombre}' no encontrado.")

def calcular_valor_total():
    total = sum(producto["precio"] * producto["cantidad"] for producto in inventario)
    return total

# Ejemplo de uso
if __name__ == "__main__":
    while True:
        print("\nOpciones:")
        print("1. Añadir producto")
        print("2. Mostrar todos los productos")
        print("3. Actualizar precio")
        print("4. Eliminar producto")
        print("5. Calcular valor total del inventario")
        print("6. Salir")
        
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            nombre = nombre_producto()
            precio = solicitar_precio()
            cantidad = cantidad_productos()
            añadir_producto(nombre, precio, cantidad)
        elif opcion == "2":
            mostrar_productos()
        elif opcion == "3":
            nombre = input("Ingrese el nombre del producto a actualizar: ").strip()
            nuevo_precio = solicitar_precio()
            actualizar_precio(nombre, nuevo_precio)
        elif opcion == "4":
            nombre = input("Ingrese el nombre del producto a eliminar: ").strip()
            eliminar_producto(nombre)
        elif opcion == "5":
            total = calcular_valor_total()
            print(f"El valor total del inventario es: {total}")
        elif opcion == "6":
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
