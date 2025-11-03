
def generar_diccionario(dic = {}):
    try:
        pf = open("jornada.csv", "rt", encoding="utf-8")
        pf2 = open("empleados.csv", "rt", encoding="utf-8")
    except IOError:
        print("Imposible abrir los archivos jornada.csv o empleados.csv")
    else:
        pf.readline()
        for linea in pf2:
            idEmpleado_emp, nombre, apellido, idSector = linea.strip().split(";")
            idEmpleado_emp = int(idEmpleado_emp)

            pf.seek(0)
            pf.readline()
            for linea in pf:
                idEmpleado_jor, nombre, apellido, diaTrabajado, mesTrabajado, horaEntrada, horaSalida, horaExtra = linea.strip().split(";")
                idEmpleado_jor = int(idEmpleado_jor)
                horaExtra = int(horaExtra)
                
                if idEmpleado_jor != idEmpleado_emp:
                    continue

                if idEmpleado_emp not in dic:
                    dic[idEmpleado_emp] = {"nombre": nombre, "apellido": apellido, "sector":idSector ,"horas_extras_total": 0}
                else:
                    dic[idEmpleado_emp]["nombre"] = nombre
                    dic[idEmpleado_emp]["apellido"] = apellido

                dic[idEmpleado_emp]["horas_extras_total"] += horaExtra

        pf.close()
        pf2.close()
    return dic

