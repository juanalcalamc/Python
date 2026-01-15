import os
import shutil

print(os.getcwd())
archivo = open("curso.txt", "w")
archivo.write("Hola de ejemplo")
archivo.close()

# shutil.move('curso.txt',"C:\\Users\\alcalaju\\Videos\\Python")

# os.unlink()#elimina archivo en ruta que proveas
# os.rmdir()#elimina una carpeta vacia en la ruta que le des
# shutil.rmtree()#elimina todo

ruta = "C:\\Users\\alcalaju\\Videos\\Python"
for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f"EN la carpeta: {ruta}")
    print(f"Las subcarpetas son ")
    for sub in subcarpeta:
        print(f"\t{sub}")
    print("los archivos son")
    for arch in archivo:
        print(f"\t{arch}")
