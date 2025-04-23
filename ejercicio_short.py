    #escribe un programa que pide al usuario la contraseña y la valide 
    #El programa debe seguir pidiendo la contraseña hasta que sea correcta 

pswd_correcta = "el_pepe123"
pswd_user = ""

while pswd_user != pswd_correcta:
    pswd_user = input("Ingrese contraseña: ")

    if pswd_user != pswd_correcta:
        print("La contraseña es incorrecta")

print("la contraseña es correcta")