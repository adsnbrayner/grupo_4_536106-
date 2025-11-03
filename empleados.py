import random

def generar_archivo_empleados():
    try:
        pf = open("empleados.csv", "wt", encoding="utf-8")
    except IOError:
        print("No se pudo crear el archivo empleados.csv")
    else:
        idempleadoelegidos = []
        nombres_disponibles = ["Ana", "Luis", "Marta", "Carlos", "Sofía", "Jorge", "Lucía", "Miguel", "Elena", "Pedro"]
        apellidos_disponibles = ["Gómez", "Rodríguez", "López", "Martínez", "Pérez", "Sánchez", "Ramírez", "Cruz", "Flores", "Rivera"]

        random.shuffle(nombres_disponibles)

        nombres_para_usar = nombres_disponibles[0:5] 

        for nombre in nombres_para_usar:
            idEmpleado = random.randint(1000, 9999)
            while idEmpleado in idempleadoelegidos:
                idEmpleado = random.randint(1000, 9999)
            idempleadoelegidos.append(idEmpleado)
            
            apellido = random.choice(apellidos_disponibles)
            idSector = random.randint(1, 3)
            
            linea = f"{idEmpleado};{nombre};{apellido};{idSector}\n"
            pf.write(linea)
        
        pf.close()
        print("Archivo empleados.csv creado con éxito.")
