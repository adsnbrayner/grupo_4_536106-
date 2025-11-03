def generar_ranking(dic):
    try:
        pf = open("ranking_empleado.csv", "wt", encoding="utf-8")
    except IOError:
        print("No se pudo crear el archivo ranking_empleado.csv")
    else:
        lista_ordenada = sorted(dic.items(), key=lambda x: x[1]["horas_extras_total"], reverse=True)
        pf.write("ID Empleado;Nombre;Apellido;Sector;Horas Extras Totales\n")
        for idEmpleado, datos in lista_ordenada:
            nombre = datos["nombre"]
            apellido = datos["apellido"]
            sector = datos["sector"]
            horas_extras_total = datos["horas_extras_total"]
            linea = f"{idEmpleado};{nombre};{apellido};{sector};{horas_extras_total}\n"
            pf.write(linea)
        pf.close()
        print("Archivo ranking_empleado.csv creado con éxito.")
