edad = int(input("ingrese su edad: "))

if edad <= 12:
    print("Eres un niño, no puedes ingresar")
elif edad <= 17:
    print("Eres un adolecente pidele ayuda a un mayor de edad responsable")
elif edad <= 59:
    print("Eres un adulto, bienvenido a nuestros servicios")
elif 60 <= edad <= 120:
    print("Usted está en la tercera edad, si necesita ayuda comuníquese con nuestros asistentes en +57 3014412967")
else:
    print("Edad no válida")
