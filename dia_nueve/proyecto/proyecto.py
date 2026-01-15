import os
import re
import time
from datetime import datetime
from math import ceil

# Ruta del directorio raíz
directorio_raiz = "C:\\Users\\alcalaju\\Videos\\Python\\Mi_Gran_Directorio"

# Inicio del cronómetro
inicio = time.time()

# Fecha actual en formato dd/mm/aa
fecha_actual = datetime.now().strftime("%d/%m/%y")

#  Expresión regular para el número de serie
patron_serie = re.compile(r"\bN[a-zA-Z]{3}-\d{5}\b")

#  Diccionario para guardar resultados
resultados = {}

#  Recorrido del árbol de carpetas
for carpeta_actual, subcarpetas, archivos in os.walk(directorio_raiz):
    for archivo in archivos:
        if archivo.endswith(".txt"):
            ruta_completa = os.path.join(carpeta_actual, archivo)
            try:
                with open(ruta_completa, "r", encoding="utf-8") as f:
                    contenido = f.read()
                    coincidencia = patron_serie.search(contenido)
                    if coincidencia:
                        resultados[archivo] = coincidencia.group()
            except Exception as e:
                pass  # Ignorar errores de lectura

# Fin del cronómetro
fin = time.time()
duracion = ceil(fin - inicio)

#  Presentación de resultados
print(f"Fecha de búsqueda: {fecha_actual}\n")
print("ARCHIVO\t\tNRO. SERIE")
print("-------\t\t----------")
for archivo, serie in resultados.items():
    print(f"{archivo}\t{serie}")
print(f"\nNúmeros encontrados: {len(resultados)}")
print(f"Duración de la búsqueda: {duracion} segundos")
