from datetime import datetime

def escribir_log(mensaje):
    try:
        with open("log.txt", "at", encoding="utf-8") as log:
            fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            log.write(f"[{fecha_hora}] {mensaje}\n")
    except IOError:
        print("No se pudo escribir en log.txt")
