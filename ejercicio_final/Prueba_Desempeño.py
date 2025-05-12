print("Hola nuevo usuaeio Bienvenido a este programa 😸")
print(f"Si es tu primera vez en este programa es necesario"
"\nQue ingreses minimo 5 productos para iniciar con tu tienda")


#List
inventory = []

# Request the product name and validate that it contains only letters with the .strip()
def get_product_name():
    while True:
        name = input("Ingrese el nombre del producto: ").strip()
        if name.isalpha():
            return name # Devuelve el nombre si es válido
        print("El nombre del producto debe contener letras y no estar vacio...")

# Request the price of the product and validate that it is a positive number
def get_product_price():
    while True:
        try:
            price = float(input("Ingrese el precio del producto: "))
            if price >= 0:
                return price # Returns the price if valid
            print("El precio es negativo, intente otra vez...")
        except ValueError:
            print("Precio no valido, ingrese un numero...")

# Request the quantity of the product and validate that it is a positive integer
def get_product_quantity():
    while True:
        try:
            quantity = int(input("Ingrese la cantidad del producto: "))
            if quantity >= 0:
                return quantity #it ​​is verified that it is valid
            print("La cantidad no puede ser negativa...")
        except ValueError:
            print("Cantidad no valida, ingrese un numero entero...")

# Add a new product to the inventory with its name, price and quantity
def add_product(name, price, quantity):
    inventory.append({"name": name, "price": price, "quantity": quantity})
    print(f"Producto'{name}' Añadido al inventario exitosamente...")

# Displays all products in the inventory with their data
def show_products():
    if inventory:
        print(f"\nInventario actual:...")
        for product in inventory:
            print(f"Nombre: {product['name']}, Precio: {product['price']:.2f}") #2f to end with 2 decimal places
    else:
        print("El inventario esta vacio...")

# Search for a product by name in the inventory
def find_product(name):
    for product in inventory:
        if product['name'].lower() == name.lower():
            return product #return the product if found
    return None

# Update the price of an existing product
def update_price(name, new_price):
    product = find_product(name)
    if product:
        if new_price >= 0:
            product['price'] = new_price
            print(f"Precio del producto '{name}' actualizado a {new_price:2f}")
        else:
            print("El precio debe ser un numero positivo...")
    else:
        print(f"Producto '{name}' No encontrado...")


# Remove a product from inventory
def delete_product(name):
    global inventory  # Access the global variable inventory (Global variables are those that are defined outside of a function and can be accessed from anywhere in the code.)
    product = find_product(name)
    if product:
        inventory = [p for p in inventory if p ['name'].lower() != name.lower()]
        print(f"Producto '{name}' Eliminado del inventario...")
    else:
        print(f"Poroducto '{name}' No existe o esta mal escrito...")
    
# Calculate the total inventory value (price * quantity per product)
def calculate_total_value():
    total = sum(p['price'] * p['quantity'] for p in inventory)
    return round(total, 2) # Returns the total rounded to two decimal places

# Main program: runs the options menu
if __name__ == "__main__":
# Asks the user to enter 5 initial products
    print("Por favor ingrese 5 productos iniciales para el inventario.")
    for i in range(5):
        name = get_product_name()
        price = get_product_price()
        quantity = get_product_quantity()
        add_product(name, price, quantity)

   # Main menu loop
    while True:
        #menu options to choose from
        print("\nMenú:")
        print("1. Añadir producto")
        print("2. Mostrar todos los productos")
        print("3. Actualizar precio del producto")
        print("4. Eliminar producto")
        print("5. Calcular valor total del inventario")
        print("6. Salir")

        option = input("Seleccione una opción: ").strip()

        if option == "1":
             # Add a new product
            name = get_product_name()
            price = get_product_price()
            quantity = get_product_quantity()
            add_product(name, price, quantity)

        elif option == "2":
            # Show full inventory
            show_products()

        elif option == "3":
            # Update the price of a product
            name = input("Ingrese el nombre del producto a actualizar: ").strip()
            product = find_product(name)
            if product:
                new_price = get_product_price()
                update_price(name, new_price)
            else:
                print(f"Producto '{name}' no encontrado.")

        elif option == "4":
            # Remove a product from inventory
            name = input("Ingrese el nombre del producto a eliminar: ").strip()
            product = find_product(name)
            if product:
                confirmation = input("¿Está seguro de que desea eliminarlo? (Y para confirmar / N para cancelar): ").upper()
                if confirmation == "Y":
                    delete_product(name)
                else:
                    print("Acción cancelada.")
            else:
                print(f"Producto '{name}' no encontrado.")

        elif option == "5":
           # Calculate the total value of the inventory
            total = calculate_total_value()
            print(f"Valor total del inventario: {total:.2f}")

        elif option == "6":
          # Exit the program
            print("Saliendo del programa.")
            break

        else:
            print("Opción inválida. Intente nuevamente.")