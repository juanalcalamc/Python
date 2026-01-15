from numero import *


def menu():
    print("""¡Hola! Bienvenido a nuestra farmacia Alcanax.
Tenemos algunas cosas que decirte para que tengas en cuenta:

- Elige la letra C si quieres ir a la sección de cosmética.
- Elige la letra F si quieres ir a la farmacia.
- Elige la letra L si lo que quieres es ir a la sección de lociones.
- Espera tu turno pacientemente y no te saltes la fila.

¡Esperamos que te agrade la experiencia en nuestro local!
""")

    while True:
        var = input(
            "¿Ya tomaste una decisión? Digita tu respuesta (C/F/L o N para salir): "
        ).lower()
        try:
            if var == "c":
                cosmetica()
            elif var == "f":
                farmacia()
            elif var == "l":
                lociones()
            elif var == "n":
                print("Gracias por visitarnos. ¡Hasta pronto!")
                break
            else:
                print("Opción no válida. Por favor elige C, F, L o N.")
        except Exception as e:
            print("Ocurrió un error:", e)


menu()
