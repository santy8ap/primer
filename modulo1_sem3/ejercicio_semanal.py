# Inventario inicial
inventario = []

def nombre_producto():
    while True:
        nombre = input("Ingrese el nombre del producto: ")
        if nombre.strip() and all(c.isalpha() for c in nombre):
            return nombre.strip()
        else:
            print("El nombre del producto debe contener solo letras y no estar vacío.")

def solicitar_precio():
    while True:
        entrada = input("Ingrese el precio del producto: ")
        try:
            numero = float(entrada)
            return numero
        except ValueError:
            print("Precio no válido, ingrese otra vez el precio.")

def cantidad_productos():
    while True:
        cantidad = input("Ingresar cantidad: ")
        try:
            productos = int(cantidad)
            if productos >= 0:
                return productos
            else:
                print("La cantidad no puede ser negativa.")
        except ValueError:
            print("Cantidad no válida, ingrese otra vez.")

def añadir_producto(nombre, precio, cantidad):
    inventario.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})
    print(f"Producto '{nombre}' añadido al inventario.")

def buscar_producto(nombre):
    while True:
        try:
            for producto in inventario:
                if producto["nombre"].lower() == nombre.lower():
                    return producto["precio"], producto["cantidad"]
            print("Producto no encontrado. Intente nuevamente.")
            nombre = input("Ingrese el nombre del producto a buscar: ").strip()
        except Exception as e:
            print(f"Error al buscar el producto: {e}")

def actualizar_precio(nombre, nuevo_precio):
    while True:
        for producto in inventario:
            if producto["nombre"].lower() == nombre.lower():
                producto["precio"] = nuevo_precio
                print(f"Precio del producto '{nombre}' actualizado a {nuevo_precio}.")
                return True
        print(f"Producto '{nombre}' no encontrado. Intente nuevamente.")
        nombre = input("Ingrese el nombre del producto a actualizar: ").strip()
        nuevo_precio = solicitar_precio()

def eliminar_producto(nombre):
    while True:
        global inventario
        if any(producto["nombre"].lower() == nombre.lower() for producto in inventario):
            inventario = [producto for producto in inventario if producto["nombre"].lower() != nombre.lower()]
            print(f"Producto '{nombre}' eliminado del inventario.")
            return
        print(f"Producto '{nombre}' no encontrado. Intente nuevamente.")
        nombre = input("Ingrese el nombre del producto a eliminar: ").strip()

def calcular_valor_total():
    while True:
        try:
            total = sum(producto["precio"] * producto["cantidad"] for producto in inventario)
            return total
        except Exception as e:
            print(f"Error al calcular el valor total: {e}")

# Ejecución sin menú:

# Añadir producto
print("Agregar un nuevo producto:")
nombre = nombre_producto()
precio = solicitar_precio()
cantidad = cantidad_productos()
añadir_producto(nombre, precio, cantidad)

# Mostrar producto añadido
print(f"\nProducto añadido: {nombre} - Precio: {precio} - Cantidad: {cantidad}")

# Buscar producto
print("\nBuscar producto:")
nombre_buscar = input("Ingrese el nombre del producto a buscar: ").strip()
resultado = buscar_producto(nombre_buscar)
if resultado:
    precio_encontrado, cantidad_encontrada = resultado
    print(f"Producto encontrado: Precio = {precio_encontrado}, Cantidad = {cantidad_encontrada}")
else:
    print("Producto no encontrado.")

# Actualizar precio
print("\nActualizar precio de un producto:")
nombre_actualizar = input("Ingrese el nombre del producto a actualizar: ").strip()
nuevo_precio = solicitar_precio()
actualizado = actualizar_precio(nombre_actualizar, nuevo_precio)

# Eliminar producto
print("\nEliminar producto:")
nombre_eliminar = input("Ingrese el nombre del producto a eliminar: ").strip()
eliminar_producto(nombre_eliminar)

# Calcular valor total
total = calcular_valor_total()
print(f"\nEl valor total del inventario es: {total}")
