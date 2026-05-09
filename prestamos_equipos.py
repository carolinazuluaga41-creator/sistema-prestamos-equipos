# Diccionario principal del sistema
equipos = {
    "Laptop Lenovo": {
        "disponible": True,
        "prestamos": []
    },
    "PC Gamer": {
        "disponible": True,
        "prestamos": []
    },
    "Monitor Samsung": {
        "disponible": True,
        "prestamos": []
    }
}


# Mostrar equipos
def mostrar_equipos():
    print("\n--- LISTA DE EQUIPOS ---")

    for nombre, datos in equipos.items():
        estado = "Disponible" if datos["disponible"] else "Prestado"
        print(f"{nombre} -> {estado}")


# Registrar préstamo
def registrar_prestamo():
    mostrar_equipos()

    equipo = input("\nIngrese el nombre del equipo: ")

    if equipo in equipos:

        if equipos[equipo]["disponible"]:

            usuario = input("Ingrese el nombre del usuario: ")
            fecha = input("Ingrese la fecha: ")

            prestamo = (usuario, fecha)

            equipos[equipo]["prestamos"].append(prestamo)

            equipos[equipo]["disponible"] = False

            print("Préstamo registrado correctamente.")

        else:
            print("El equipo ya está prestado.")

    else:
        print("El equipo no existe.")


# Devolver equipo
def devolver_equipo():
    equipo = input("\nIngrese el nombre del equipo a devolver: ")

    if equipo in equipos:

        if not equipos[equipo]["disponible"]:

            equipos[equipo]["disponible"] = True

            print("Equipo devuelto correctamente.")

        else:
            print("El equipo ya estaba disponible.")

    else:
        print("El equipo no existe.")


# Ver historial
def ver_historial():

    print("\n--- HISTORIAL DE PRÉSTAMOS ---")

    for nombre, datos in equipos.items():

        print(f"\nEquipo: {nombre}")

        if datos["prestamos"]:

            for usuario, fecha in datos["prestamos"]:
                print(f"Usuario: {usuario} | Fecha: {fecha}")

        else:
            print("Sin préstamos registrados.")


# Agregar nuevo equipo
def agregar_equipo():

    nuevo_equipo = input("\nIngrese el nombre del nuevo equipo: ")

    if nuevo_equipo not in equipos:

        equipos[nuevo_equipo] = {
            "disponible": True,
            "prestamos": []
        }

        print("Equipo agregado correctamente.")

    else:
        print("Ese equipo ya existe.")


# Menú principal
def menu():

    while True:

        print("\n===== SISTEMA DE PRÉSTAMOS =====")
        print("1. Ver equipos")
        print("2. Registrar préstamo")
        print("3. Devolver equipo")
        print("4. Ver historial")
        print("5. Agregar equipo")
        print("6. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_equipos()

        elif opcion == "2":
            registrar_prestamo()

        elif opcion == "3":
            devolver_equipo()

        elif opcion == "4":
            ver_historial()

        elif opcion == "5":
            agregar_equipo()

        elif opcion == "6":
            print("Saliendo del sistema...")
            break

        else:
            print("Opción inválida.")


# Ejecutar programa
menu()