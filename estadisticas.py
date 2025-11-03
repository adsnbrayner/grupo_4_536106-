from log import escribir_log

def generar_estadisticas(dic): 
    try:
        pf = open("ranking_sector.csv", "rt", encoding="utf-8")
        pf2 = open("estadisticas_globales.csv", "wt", encoding="utf-8")
    except IOError:
        print("No se pudo crear el archivo estadisticas_globales.csv")
    else:
        pf2.write("Total horas extra; Promedio horas extra por empleado; Cantidad de empleados\n")
        total_general = 0
        pf.readline()
        for linea in pf:
            try:
                sector, nombre, horas_extras_total, porcentaje = linea.strip().split(';')
                horas_extras_total = int(horas_extras_total)
                total_general += horas_extras_total
            except ValueError:
                print(f"Omitiendo línea mal formada en ranking_sector.csv: {linea.strip()}")

        empleados = len(dic)
        if empleados > 0:
            promedio = float(total_general / empleados)
        else:
            promedio = 0
        linea = f"{total_general};{promedio:.2f};{empleados}\n"
        pf2.write(linea)

        escribir_log("Estadisticas generadas con exito.")
        pf.close()
        pf2.close()

        print("Archivo estadisticas_globales.csv creado con éxito.")


