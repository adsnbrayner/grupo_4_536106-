def ranking_sector():
    try:
        pf = open("ranking.csv", "rt", encoding="utf-8")
        pf2 = open("ranking_sector.csv", "wt", encoding="utf-8")
    except IOError:
        print("No se pudo crear el archivo ranking_sector.csv o abrir ranking.csv")
    else:
        sector_dict = {}
        total_general_horas = 0
        
        pf.readline()
        for linea in pf:
            try:
                idEmpleado, nombre, apellido, sector, horas_extras_total = linea.strip().split(";")
                horas_extras_total = int(horas_extras_total)
                
                total_general_horas += horas_extras_total

                if sector not in sector_dict:
                    sector_dict[sector] = 0
                sector_dict[sector] += horas_extras_total
            except ValueError:
                print(f"Advertencia: Omitiendo línea mal formada: {linea.strip()}")
            except Exception as e:
                print(f"Error procesando línea: {linea.strip()} - {e}")


        lista_ordenada = sorted(sector_dict.items(), key=lambda x: x[1], reverse=True)
        
        pf2.write("Sector;Nombre;Horas Extras Totales;Porcentaje de Horas Extras\n")
        
        for sector, horas_extras_total in lista_ordenada:
            nombre = "Desconocido"
            if int(sector) == 1:
                nombre = "Recursos Humanos"
            elif int(sector) == 2:
                nombre = "Desarrollo"
            elif int(sector) == 3:
                nombre = "Ventas"
            
            if total_general_horas > 0:
                porcentaje = (horas_extras_total / total_general_horas) * 100
            else:
                porcentaje = 0

            linea = f"{sector};{nombre};{horas_extras_total};{porcentaje:.2f}%\n"
            pf2.write(linea)

        pf.close()
        pf2.close()
        print("Archivo ranking_sector.csv creado con éxito.")