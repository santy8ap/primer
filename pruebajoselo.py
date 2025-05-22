# Performance Test - Module 1
# Python Programming Fundamentals
# JOSE MANUEL BUSTAMANTE MONSALVE

inventory = [] # An empty list called 'inventory' is created

# Displays the options menu for interacting with the inventory
def menu():
   # This function displays the options menu to the user.
    print("\n--- BIENVENIDO ---\n")
    print("1. Ver inventario.")
    print("2. Añadir productos.")
    print("3. Consultar productos.")
    print("4. Actualizar precios.")
    print("5. Eliminar productos.")
    print("6. Calcular el valor total del inventario.")
    print("7. Salir.\n")

menu() # Print the options menu
option=input("Escoja una opción para interactuar con el inventario (1-7): ")

def emptyInventory():
        # This function prints a message indicating that the inventory is empty.
        print("\nEl inventario está vacío.\n")

def seeInventory():
    # This function displays the list of products in the inventory, including their name, price, and quantity.
    i=0 # A counter is started to list the products.
    print("Los productos en el inventario son los siguientes: \n")
    for product in inventory: # Iterates over each product in the inventory list.
        i+=1 # The counter is incremented for each product iterated over.
        print(f"Producto #{i}:\n Nombre: {product["Nombre"]}\n Precio: ${product["Precio"]}\n Cantidad: {product["Cantidad"]}\n")

def toContinue():
    # This function asks the user if they want to return to the main menu or exit the program.
    global option # 'Global' is used so that the 'option' variable can be used within the function.
    print("¿Qué desea hacer a continuación?\n")
    print("1. Ver menú de opciones")
    print("2. Salir\n")
    option2=int(input("Ingrese una opción: ")) 
    while option2 < 1 or option2 > 2:
        option2=int(input("Ingrese una opción valida (1-2): "))
    if option2==1:
        menu() # The menu function is called to display the options again.
        option=input("Escoja una opción para interactuar con el inventario: ")
    if option2==2: 
        print("\n Hasta pronto, Usuario! \n\n        FIN\n")
        quit() # 'quit()' is used to end the program

# 1. Add products to inventory: Allow the user to add products with attributes such as name, price and quantity available.
def addProduct():
    # This function allows the user to add a new product to the inventory, asking for its name, price and quantity.
    # The new product is stored in the list.
     
    list={} # An empty dictionary is created to begin storing information for each product.
    list["Nombre"]=input("Ingresa el nombre del producto: ").capitalize() # The name of the product is requested and saved in the dictionary with the key "Nombre".
    list["Precio"]=float(input(f"Ingresa el precio de {list["Nombre"]}: ")) # The product price is requested, converted to float and saved with the key "Precio".
    while list["Precio"] < 0.1: # Here it is validated that the price is positive and greater than 0
        list["Precio"]=float(input(f"Ingresa un precio valido para {list["Nombre"]} (mayor que 0): "))
        if list["Precio"] > 0:
            break
    list["Cantidad"]=int(input(f"Ingresa la cantidad de {list["Nombre"]} disponible: ")) # The quantity of the product is requested, converted to int and saved with the key "Cantidad".
    inventory.append(list) # The new product is added to the list.
    print(f"El producto {list["Nombre"]} fue agregado con éxito\n")
    while len(inventory)<5: # Here it is validated that there are at least 5 products in the inventory.
        addProduct()

# 2. Consult products in inventory: search for a product by its name and display its details (name, price, quantity). 
def consultProduct():
    # This function allows the user to search for a product in the inventory by name and displays its information if found.
    # If the inventory is empty, the emptyInventory function is called to tell the user that there is nothing in the inventory.
    if inventory:
        search=input("\nIngrese el nombre del producto: ").capitalize()
        for product in inventory:
            if search==product["Nombre"]:
                print(f"\n Producto: {product["Nombre"]}\n Precio: {product["Precio"]}\n Cantidad: {product["Cantidad"]}\n")
                break # The iteration stops once the product is found.
        if search!=product["Nombre"]: # It is executed if the product is not found.
            print(f"\nEl producto '{search}' no está en el inventario.\n")
    if not inventory: # Check that the inventory is not empty
        emptyInventory()

# 3. Update product prices: Change the price of a specific product in inventory.
def updatePrice():
    # This function allows the user to update the price of a product in the inventory.
    # First it shows the inventory and then asks for the product name and the new price.
    # If the inventory is empty, the emptyInventory function is called to tell the user that there is nothing in the inventory.
    if inventory:
        seeInventory() # shows the inventory
        toSelectProduct=input("Ingrese un producto del inventario (escrito de igual manera a como se ve en 'Nombre'): ").capitalize()
        for product in inventory: 
            if toSelectProduct==product["Nombre"]:
                toUpdatePrice=float(input("Ingrese el nuevo precio del producto: "))
                while toUpdatePrice < 0.1: # Here it is validated that the price is positive and greater than 0
                    toUpdatePrice=float(input("Ingrese un precio valido (mayor que 0): "))
                if toUpdatePrice > 0:
                    product["Precio"]=toUpdatePrice
                    print(f"El nuevo precio de {product["Nombre"]} ahora es ${product["Precio"]}\n")
                    break
        if toSelectProduct!=product["Nombre"]:
                print(f"\nEl producto '{toSelectProduct}' no está en el inventario.\n")       
    if not inventory:
        emptyInventory()

#4. Remove products from inventory: Allows the removal of a product that is no longer available.
def deleteProduct():
    # This function allows the user to remove a product from inventory.
    # It first displays the inventory and then asks for the name of the product to be removed.
    # If the inventory is empty, the emptyInventory function is called to tell the user that there is nothing in the inventory.
    if not inventory:
        emptyInventory()
    if inventory:
        seeInventory() # shows the inventory
        toSelectProduct=input("Ingrese el nombre del producto que será eliminado (escrito de igual manera a como se ve en 'Nombre'): ").capitalize()
        for product in inventory: # Iterates to confirm that the product is in inventory
            if toSelectProduct==product["Nombre"]:
                inventory.remove(product)
                print(f"El producto {toSelectProduct} fue eliminado del inventario.\n")
                break
        if toSelectProduct!=product["Nombre"]:
                print(f"\nEl producto '{toSelectProduct}' no está en el inventario.\n")

# 5. Calculate the total inventory value: multiply the price by the quantity of each product and display the running total.
def inventoryTotalValue():
    # This function calculates and displays the total value of the inventory, it does the following: sum of price * quantity of each product
    # If the inventory is empty, the emptyInventory function is called to tell the user that there is nothing in the inventory.
    if not inventory:
        emptyInventory()
    if inventory:
        totalValue=0 # A variable is created to save the total value.
        for product in inventory:
            totalValue += product["Precio"] * product["Cantidad"]
        print(f"\nEl valor total de los productos en el inventario es de: ${totalValue:.2f}\n")

while True:

    if option=="1": # If the selected option is 1 (View inventory).
        if len(inventory)==0: # Check that the inventory is not empty
            emptyInventory()
            toContinue() 
        else:
            seeInventory()
            toContinue()
    
    elif option=="2": # If the selected option is 2 (Add products).
        addProduct()
        toContinue()
    
    elif option=="3": # If the selected option is 3 (Consult products).
        consultProduct()
        toContinue()
    
    elif option=="4":# If the selected option is 4 (Update prices).
        updatePrice()
        toContinue()
    
    elif option=="5": # If the selected option is 5 (Delete products).
        deleteProduct()
        toContinue()
    
    elif option=="6": # If the selected option is 6 (Calculate the total value of the inventory).
        inventoryTotalValue()
        toContinue()
    
    elif option=="7": # If the selected option is 7 (Exit).
        print("\n Hasta pronto, Usuario! \n\n        FIN\n")
        break # 'break' is used to end the 'while', ending the program

    else: # Here it is validated that the entered option is valid
        option=input("Ingrese una opción valida (1-7): ")