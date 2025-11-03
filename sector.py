def generar_archivo_sector():
    try:
        pf = open("sector.csv", "wt", encoding="utf-8")
    except IOError:
        print("No se pudo crear el archivo sector.txt")
    else:
        sectores = [
            (1, "Recursos Humanos"),
            (2, "Desarrollo"),
            (3, "Ventas")
        ]
        for idSector, nombreSector in sectores:
            linea = f"{idSector};{nombreSector}\n"
            pf.write(linea)
        
        pf.close()
        print("Archivo sector.txt creado con éxito.")

