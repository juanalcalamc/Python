import os
from pathlib import Path
def leer():
    print("""¿Qué categoría quieres consultar?
    1. Ensaladas
    2. Carnes 
    3. Pasta
    4. Postres""")
    
    opcion = input("Digita el número de la categoría: ")
    categorias = ["Ensaladas", "Carnes", "Pasta", "Postres"]
    
    if opcion in ["1", "2", "3", "4"]:
        categoria_elegida = categorias[int(opcion) - 1]
        print(f"\nRecetas en la categoría {categoria_elegida}:")
        for archivo in Recetas[categoria_elegida]:
            print(f"  - {archivo.stem}")
    else:
        print("Opción inválida.")

def crear():
    os.system("cls")
    print("Haz entrado en la opcion de crear")
    opcion=input("Estas dentro si quieres crear una receta digita 1")
    if opcion == "1":
        print("Categorías disponibles:")
        for i, categoria in enumerate(Recetas.keys(), 1):
            print(f"{i}. {categoria}")
        seleccion = input("Elige la categoría por número: ")
        categorias = list(Recetas.keys())

        if seleccion.isdigit() and 1 <= int(seleccion) <= len(categorias):
            categoria_elegida = categorias[int(seleccion) - 1]
            nombre = input("Nombre de la nueva receta: ").strip()
            contenido = input("Escribe el contenido de la receta: ")
            ruta = carpeta / f"{nombre}.txt"

            with open(ruta, 'w') as archivo:
                archivo.write(contenido)

            Recetas[categoria_elegida].append(ruta)
            print(f"\n Receta '{nombre}' creada exitosamente en la categoría '{categoria_elegida}'.")
        else:
            print(" Categoría inválida.")
def crear_categoria():
    nueva_categoria = input("Escribe el nombre de la nueva categoría: ").strip()
    if nueva_categoria in Recetas:
        print(" Esa categoría ya existe.")
    else:
        Recetas[nueva_categoria] = []
        print(f"Categoría '{nueva_categoria}' creada exitosamente.")
def eliminar_categoria():
    print("Categorías disponibles:")
    for i, categoria in enumerate(Recetas.keys(), 1):
        print(f"{i}. {categoria}")
    seleccion = input("Elige la categoría que deseas eliminar (por número): ")
    categorias = list(Recetas.keys())

    if seleccion.isdigit() and 1 <= int(seleccion) <= len(categorias):
        categoria_elegida = categorias[int(seleccion) - 1]
        confirmacion = input(f"¿Estás seguro de eliminar la categoría '{categoria_elegida}' y todas sus recetas? (s/n): ")
        if confirmacion.lower() == 's':
            for archivo in Recetas[categoria_elegida]:
                if archivo.exists():
                    archivo.unlink()
            del Recetas[categoria_elegida]
            print(f" Categoría '{categoria_elegida}' eliminada.")
        else:
            print("Operación cancelada.")
    else:
        print(" Opción inválida.")
def eliminar_receta():
    print("Categorías disponibles:")
    for i, categoria in enumerate(Recetas.keys(), 1):
        print(f"{i}. {categoria}")
    seleccion = input("Elige la categoría (por número): ")
    categorias = list(Recetas.keys())

    if seleccion.isdigit() and 1 <= int(seleccion) <= len(categorias):
        categoria_elegida = categorias[int(seleccion) - 1]
        recetas = Recetas[categoria_elegida]
        if not recetas:
            print("No hay recetas en esta categoría.")
            return
        print(f"Recetas en '{categoria_elegida}':")
        for i, archivo in enumerate(recetas, 1):
            print(f"{i}. {archivo.stem}")
        receta_sel = input("Elige la receta a eliminar (por número): ")
        if receta_sel.isdigit() and 1 <= int(receta_sel) <= len(recetas):
            receta = recetas[int(receta_sel) - 1]
            if receta.exists():
                receta.unlink()
            Recetas[categoria_elegida].remove(receta)
            print(f" Receta '{receta.stem}' eliminada.")
        else:
            print("Opción inválida.")
    else:
        print(" Opción inválida.")



Nombre=input("Digite su nombre para poder seguir dentro del aplicativo: ")
print(f"""Hola {Nombre}, Bienvenido a este recetario, 
      donde encontrarás recetas de carne, ensaladas y 
      muchas otras opciones deliciosas para preparar. """)

carpeta=Path('C:/Users/alcalaju/Download/Curso Python/Recetas')
Recetas = {
    "Ensaladas": [
        carpeta / 'Ensalada Griega.txt',
        carpeta / 'Ensalada Mediterranea.txt'
    ],
    "Carnes": [
        carpeta / 'Entrecot al Malbec.txt',
        carpeta / 'Matambre a la Pizza.txt'
    ],
    "Pasta": [
        carpeta / 'Raviolis de Ricotta.txt',
        carpeta / 'Canelones e Espinaca.txt'
    ],
    "Postres": [
        carpeta / 'Compota de Manzana.txt',
        carpeta / 'Tarta de Frambuesa.txt'
    ]
}
print(f"Laa recetas se encuntran en esta carpeta {carpeta}")

print("Las recetas que puedes encontrar están organizadas así:\n")
for categoria, archivos in Recetas.items():
    print(f" {categoria}:")
    for archivo in archivos:
        print(f"  - {archivo.stem}")
    print() 

var=input("Ya decidiste ? para seguir escribe s para salir escribe cualquier cosa")

if var == 's':
    os.system('cls')  
    print("Listo, ya que decidiste seguir, empezamos entonces: ")
    print("""Entonces dime que es lo que quieres hacer
          1.Leer receta
          2.crear receta
          3.Crear categoria
          4.Eliminar categoria
          5.Eliminar Raeceta
          6.Finalizar programa 
          'Teniendo en cuenta que para elegir una opcion debes digitar solo el numero '""")
    var1=input("Ya tomaste una decicion Ok dijitala: ")
    if var1=="1":
        leer()
    elif var1=="2":
        crear()
    elif var1 == "3":
        crear_categoria()
    elif var1 == "4":
        eliminar_categoria()
    elif var1 == "5":
        eliminar_receta()
else:
    os.system('cls')
    print("Este es el final")
      