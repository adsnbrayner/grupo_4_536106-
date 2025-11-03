from log import escribir_log

CARACTER_BARRA = "█"
ANCHO_MAXIMO = 50

def _generar_grafico_ranking_empleados():
    """
    Genera un gráfico de barras en .txt para el ranking de empleados.
    Lee: ranking.csv
    Escribe: reporte_ranking_empleados.txt
    """
    try:
        pf = open("ranking.csv", "rt", encoding="utf-8")
        pf_reporte = open("reporte_ranking_empleados.txt", "wt", encoding="utf-8")
    except IOError:
        print("No se pudo abrir 'ranking.csv' o crear 'reporte_ranking_empleados.txt'")
        escribir_log("Error al abrir archivos para reporte de empleados (txt)")
        return

    datos = []
    max_horas = 0
    largo_nombre = 0

    try:
        pf.readline()
        for linea in pf:
            if not linea.strip():
                continue
            
            try:
                id, nombre, apellido, sector, horas_str = linea.strip().split(";")
                horas = int(horas_str)
                nombre_completo = f"{nombre} {apellido}"
                
                datos.append((nombre_completo, horas))
                
                if horas > max_horas:
                    max_horas = horas
                if len(nombre_completo) > largo_nombre:
                    largo_nombre = len(nombre_completo)

            except ValueError:
                print(f"Omitiendo línea mal formada en ranking.csv: {linea.strip()}")

        pf_reporte.write("=== Reporte Gráfico: Ranking de Horas Extras por Empleado ===\n\n")

        if max_horas == 0:
            pf_reporte.write("No hay horas extras para reportar.\n")
        else:
            escala = ANCHO_MAXIMO / max_horas

            for nombre, horas in datos:
                cantidad_barras = int(horas * escala)
                barra_grafica = CARACTER_BARRA * cantidad_barras
                
                linea_reporte = f"{nombre.ljust(largo_nombre)} | {barra_grafica} ({horas}h)\n"
                pf_reporte.write(linea_reporte)

        pf_reporte.write("\n=== Fin del Reporte ===\n")
        print("Archivo 'reporte_ranking_empleados.txt' generado con éxito.")
        escribir_log("Reporte TXT de ranking de empleados generado.")

    except Exception as e:
        print(f"Error inesperado al generar reporte de empleados: {e}")
        escribir_log(f"Error inesperado reporte empleados: {e}")
    finally:
        pf.close()
        pf_reporte.close()


def _generar_grafico_ranking_sector():
    """
    Genera un gráfico de barras en .txt para el ranking de sectores.
    Lee: ranking_sector.csv
    Escribe: reporte_ranking_sector.txt
    """
    try:
        pf = open("ranking_sector.csv", "rt", encoding="utf-8")
        pf_reporte = open("reporte_ranking_sector.txt", "wt", encoding="utf-8")
    except IOError:
        print("No se pudo abrir 'ranking_sector.csv' o crear 'reporte_ranking_sector.txt'")
        escribir_log("Error al abrir archivos para reporte de sector (txt)")
        return

    datos = []
    max_porcentaje = 0.0
    largo_nombre = 0

    try:
        pf.readline()
        for linea in pf:
            if not linea.strip():
                continue
            
            try:
                sector_id, nombre, horas_str, porcentaje_str = linea.strip().split(";")
                
                porcentaje = float(porcentaje_str.replace("%", ""))
                
                datos.append((nombre, porcentaje))
                
                if porcentaje > max_porcentaje:
                    max_porcentaje = porcentaje
                if len(nombre) > largo_nombre:
                    largo_nombre = len(nombre)

            except ValueError:
                print(f"Omitiendo línea mal formada en ranking_sector.csv: {linea.strip()}")

        pf_reporte.write("=== Reporte Gráfico: Porcentaje de Horas por Sector ===\n\n")

        if max_porcentaje == 0:
            pf_reporte.write("No hay porcentajes para reportar.\n")
        else:
            escala = ANCHO_MAXIMO / max_porcentaje

            for nombre, porcentaje in datos:
                cantidad_barras = int(porcentaje * escala)
                barra_grafica = CARACTER_BARRA * cantidad_barras
                
                linea_reporte = f"{nombre.ljust(largo_nombre)} | {barra_grafica} ({porcentaje:.2f}%)\n"
                pf_reporte.write(linea_reporte)

        pf_reporte.write("\n=== Fin del Reporte ===\n")
        print("Archivo 'reporte_ranking_sector.txt' generado con éxito.")
        escribir_log("Reporte TXT de ranking de sector generado.")

    except Exception as e:
        print(f"Error inesperado al generar reporte de sector: {e}")
        escribir_log(f"Error inesperado reporte sector: {e}")
    finally:
        pf.close()
        pf_reporte.close()


def generar_reportes_texto():
    """
    Función principal de este módulo. Llama a todas las funciones
    para generar los reportes gráficos en formato .txt.
    """
    print("\nIniciando generación de reportes gráficos en .txt...")
    _generar_grafico_ranking_empleados()
    _generar_grafico_ranking_sector()
    print("Reportes gráficos .txt finalizados.")