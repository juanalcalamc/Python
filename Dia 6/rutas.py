import os
from pathlib import Path,PureWindowsPath
carpeta=Path('C:/Users/alcalaju/Download/Curso Python')
archivo= carpeta/'prueba.txt'

mi_archivo =open(archivo)
print  (mi_archivo.read)