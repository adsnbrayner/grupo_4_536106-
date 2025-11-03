import random

def generar_archivo_jornada():
    try:
        pf = open("empleados.csv", "rt", encoding="utf-8")
        pf2 = open ("jornada.csv", "wt", encoding="utf-8")
    except IOError:
        print("No se pudo crear el archivo jornada.txt o abrir empleados.txt")
    else:
        dia = 1
        finde = 6
        mes = random.randint(1, 12)
        header = "ID Empleado;Nombre;Apellido;Dia Trabajado;Mes Trabajado;Hora Entrada;Hora Salida;Hora Extra\n"
        pf2.write(header)
        
        while dia <=22:
            if dia == finde:
                dia += 2
                finde += 7
                continue
            pf.seek(0)
            for linea in pf:
                idEmpleado, nombre, apellido, idSector = linea.strip().split(";")
                idE = int(idEmpleado)
                diaTrabajado = dia
                mesTrabajado = mes
                horaEntrada = 10
                horaSalida = random.randint(18, 22)
                horaTotal = horaSalida - horaEntrada
                if horaTotal > 8:
                    horaExtra = horaTotal - 8
                else:
                    horaExtra = 0
                linea = f"{idE};{nombre};{apellido};{diaTrabajado};{mesTrabajado};{horaEntrada};{horaSalida};{horaExtra}\n"
                pf2.write(linea)
            dia += 1
        pf.close()
        pf2.close()
        print("Archivo jornada.csv creado con éxito.")

