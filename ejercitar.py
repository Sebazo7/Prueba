def registraralumno(datos):
    print("(1)Registrar alumno\n(2)VER DATOS DEL ALUMNO\n(3)Salir")
    print("")
    int(input("Ingrese una opcion: "))
    print("")
    nombre = input("Ingrese nombre: ")
    direccion = input("ingrese direccion: ")
    telefono = str(input("Ingrese celular: "))
    datos = (nombre, direccion, telefono)
    return datos

alumno2 = registraralumno(datos=[])



while True:
    print("(1)Registrar alumno\n(2)VER DATOS DEL ALUMNO\n(3)Salir")
    op = int(input("Ingrese una opcion: "))
    
    if op == 1:
        registraralumno()
    elif op == 2:
        print(f"Ver datos: {alumno2}")
    elif op == 3:
        print("Has salido del programa")
        break


        
