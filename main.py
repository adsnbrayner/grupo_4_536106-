from user import modificar_user, deletar_user, generar_user, generar_admin
from empleados import generar_archivo_empleados
from sector import generar_archivo_sector
from jornada import generar_archivo_jornada
from diccionario import generar_diccionario
from ranking_empleado import generar_ranking
from ranking_sector import ranking_sector
from horas_liquidadas import generar_horas_liquidadas
from estadisticas import generar_estadisticas
from log import escribir_log


def main():
    escribir_log("=== INICIO DEL PROGRAMA ===")
    generar_admin()
    escribir_log("Verificación/creación de ADMIN completada")

    # ENTRADA DE DATOS
    try:
        generar_archivo_empleados()
        generar_archivo_sector()
        generar_archivo_jornada()
        escribir_log("Archivos de entrada generados correctamente")
    except Exception as e:
        escribir_log(f"Error al generar archivos de entrada: {e}")
        print(f"Error al generar archivos de entrada: {e}")
        return

    login = input("Ingrese su nombre de usuario: ").strip().upper()
    try:
        pf = open("user.txt", "rt", encoding="utf-8")
        lineas = pf.readlines()
        pf.close()
    except IOError:
        print("No se pudo abrir el archivo user.txt")
        escribir_log("Error al abrir user.txt durante el login")
        return
    else:
        autenticado = False
        for linea in lineas:
            if not linea.strip():
                continue
            nombre, password = linea.strip().split(",")
            if nombre == login:
                intento_password = input("Ingrese su contraseña: ").strip()
                if intento_password == password:
                    autenticado = True
                break

        if autenticado:
            print(f"Bienvenido, {login}!")
            escribir_log(f"Usuario {login} inició sesión correctamente")

            # BUCLE CRUD
            while True:
                accion = input("¿Desea modificar (M), eliminar (E) o crear (C) un usuario? (N) para seguir: ").strip().upper()

                if accion == "M":
                    modificar_user()
                elif accion == "E":
                    deletar_user()
                elif accion == "C":
                    generar_user()
                elif accion == "N":
                    break
                else:
                    print("Opción inválida.")

            # REPORTES
            accion2 = input("¿Desea generar los reportes? (S/N): ").strip().upper()
            if accion2 == "S":
                try:
                    dic = generar_diccionario()
                    generar_ranking(dic)
                    ranking_sector()
                    generar_horas_liquidadas()
                    generar_estadisticas(dic)
                    escribir_log("Reportes generados correctamente")
                    print("Reportes generados con éxito.")
                except Exception as e:
                    escribir_log(f"Error generando reportes: {e}")
                    print("Error al generar reportes.")
            else:
                print("No se generaron los reportes.")
                escribir_log("Usuario decidió no generar reportes")

        else:
            print("Nombre de usuario o contraseña incorrectos.")
            escribir_log(f"Intento fallido de login para {login}")

    escribir_log("=== FIN DEL PROGRAMA ===")


if __name__ == "__main__":
    main()
