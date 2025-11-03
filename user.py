from log import escribir_log

def generar_admin():
    try:
        pf = open("user.txt", "rt", encoding="utf-8")
        contenido = pf.read()
        pf.close()
    except IOError:
        try:
            pf = open("user.txt", "wt", encoding="utf-8")
            pf.write("ADMIN,1234\n")
            pf.close()
            escribir_log("Archivo user.txt creado con usuario ADMIN")
        except IOError:
            print("No se pudo crear el archivo user.txt")
            escribir_log("Error creando user.txt")
    else:
        if "ADMIN," not in contenido:
            try:
                pf = open("user.txt", "at", encoding="utf-8")
                pf.write("ADMIN,1234\n")
                pf.close()
                escribir_log("Usuario ADMIN agregado al archivo user.txt")
            except IOError:
                print("No se pudo actualizar el archivo user.txt")
                escribir_log("Error actualizando user.txt (ADMIN)")
        else:
            escribir_log("Usuario ADMIN ya existente en user.txt")


def cargar_nombre(desde, hasta, texto):
    try:
        nombre = input(texto).strip().upper()
        if nombre == "":
            return nombre
        if len(nombre) >= desde and len(nombre) <= hasta:
            return nombre
        else:
            raise ValueError
    except ValueError:
        print(f"Error: El nombre debe tener entre {desde} y {hasta} caracteres.")
        return cargar_nombre(desde, hasta, texto)


def cargar_password(desde, hasta, texto):
    try:
        password = int(input(texto))
        if password >= desde and password <= hasta:
            return password
        else:
            print(f"Error: La contraseña debe ser un número entre {desde} y {hasta}.")
            return cargar_password(desde, hasta, texto)
    except ValueError:
        print(f"Error: La contraseña debe ser un número entre {desde} y {hasta}.")
        return cargar_password(desde, hasta, texto)


def generar_user():
    existentes = set()
    try:
        pf_read = open("user.txt", "rt", encoding="utf-8")
        for linea in pf_read:
            if not linea.strip():
                continue
            nombre, _ = linea.strip().split(",")
            existentes.add(nombre.upper())
        pf_read.close()
    except IOError:
        pass

    try:
        pf = open("user.txt", "at", encoding="utf-8")
    except IOError:
        print("No se pudo abrir/crear el archivo user.txt")
        escribir_log("Error al abrir user.txt para agregar usuarios")
    else:
        users = []
        while True:
            nombre = cargar_nombre(1, 10, "Ingrese un nombre de usuario (vacío para terminar): ")
            if nombre == "":
                break
            if nombre in existentes or nombre in users:
                print("El nombre de usuario ya existe. Intente con otro.")
                continue

            password = cargar_password(1000, 9999, "Ingrese una contraseña numérica entre 1000 y 9999: ")
            pf.write(f"{nombre},{password}\n")
            escribir_log(f"Usuario creado: {nombre}")
            users.append(nombre)

        pf.close()
        print("Archivo user.txt actualizado con éxito.")
        escribir_log("Actualización de usuarios completada")


def modificar_user():
    try:
        pf = open("user.txt", "rt", encoding="utf-8")
        lineas = pf.readlines()
        pf.close()
    except IOError:
        print("No se pudo abrir el archivo user.txt")
        escribir_log("Error al abrir user.txt para modificación")
    else:
        nombre_buscar = input("Ingrese el nombre de usuario a modificar: ").strip().upper()
        while nombre_buscar == "ADMIN":
            nombre_buscar = input("No se puede modificar ADMIN. Ingrese el nombre de usuario a modificar: ").strip().upper()
        encontrado = False
        for i in range(len(lineas)):
            if not lineas[i].strip():
                continue
            nombre, password = lineas[i].strip().split(",")
            if nombre == nombre_buscar:
                nuevo_password = cargar_password(1000, 9999, "Ingrese la nueva contraseña numérica entre 1000 y 9999: ")
                lineas[i] = f"{nombre},{nuevo_password}\n"
                encontrado = True
                break
        if encontrado:
            try:
                pf = open("user.txt", "wt", encoding="utf-8")
                pf.writelines(lineas)
                pf.close()
                print("Contraseña modificada con éxito.")
                escribir_log(f"Contraseña modificada para el usuario {nombre_buscar}")
            except IOError:
                print("No se pudo guardar el archivo user.txt")
                escribir_log("Error al guardar user.txt después de modificar")
        else:
            print("El nombre de usuario no existe.")
            escribir_log(f"Intento de modificar usuario inexistente: {nombre_buscar}")


def deletar_user():
    try:
        pf = open("user.txt", "rt", encoding="utf-8")
        lineas = pf.readlines()
        pf.close()
    except IOError:
        print("No se pudo abrir el archivo user.txt")
        escribir_log("Error al abrir user.txt para eliminar")
    else:
        nombre_buscar = input("Ingrese el nombre de usuario a eliminar: ").strip().upper()
        while nombre_buscar=="ADMIN":
            nombre_buscar = input("No se puede deletar ADMIN. Ingrese el nombre de usuario a eliminar: ").strip().upper()
        encontrado = False
        nueva_lista = []
        for linea in lineas:
            if not linea.strip():
                continue
            nombre, password = linea.strip().split(",")
            if nombre == nombre_buscar:
                encontrado = True
            else:
                nueva_lista.append(linea)
        if encontrado:
            try:
                pf = open("user.txt", "wt", encoding="utf-8")
                pf.writelines(nueva_lista)
                pf.close()
                print("Usuario eliminado con éxito.")
                escribir_log(f"Usuario eliminado: {nombre_buscar}")
            except IOError:
                print("No se pudo guardar el archivo user.txt")
                escribir_log("Error al guardar user.txt después de eliminar")
        else:
            print("El nombre de usuario no existe.")
            escribir_log(f"Intento de eliminar usuario inexistente: {nombre_buscar}")
