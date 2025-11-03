def generar_horas_liquidadas():
    try:
        pf = open("jornada.csv", "rt", encoding="utf-8")
        pf2 = open("horas_liquidadas.csv", "wt", encoding="utf-8")
    except IOError:
        print("No se pudo crear el archivo horas_liquidadas.csv")
    else:
        pf2.write("ID Empleado;Nombre;Apellido;Horas Liquidadas; Horas Extras\n")
      
        totales = {}

        pf.readline()  
        for linea in pf:
            linea = linea.strip()
            if not linea:
                continue

            idEmpleado, nombre, apellido, diaTrabajado, mesTrabajado, horaEntrada, horaSalida, horaExtra = linea.split(";")

         
            if idEmpleado not in totales:
                totales[idEmpleado] = {
                    "nombre": nombre,
                    "apellido": apellido,
                    "horas_liquidadas": 0,
                    "hExtra": 0
                }

       
            totales[idEmpleado]["horas_liquidadas"] += (int(horaSalida) - int(horaEntrada))
            totales[idEmpleado]["hExtra"] += int(horaExtra)

        for idEmpleado, datos in totales.items():
            linea_out = f"{idEmpleado};{datos['nombre']};{datos['apellido']};{datos['horas_liquidadas']};{datos['hExtra']}\n"
            pf2.write(linea_out)

        pf.close()
        pf2.close()

        print("Archivo horas_liquidadas.csv creado con éxito.")

