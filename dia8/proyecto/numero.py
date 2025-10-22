# Decorador simple
def decoradores(func):
    def wrapper():
        print("Bienvenido a nuestro local")
        print("Espera pacientemente")
        return func()
    return wrapper

# Generadores persistentes por sección
turno_f = 0
turno_c = 0
turno_l = 0

@decoradores
def farmacia():
    print("Elegiste la opción de farmacia")
    var = input("Si no quieres seguir en esta sección presiona N, de lo contrario digita S: ").lower()

    def generador():
        global turno_f
        turno_f += 1
        yield f"Tu turno es F-{turno_f}"

    try:
        if var == "s":
            generado = generador()
            print(next(generado))
        elif var == "n":
            print("Qué gusto haberte tenido aquí. Hasta luego.")
        else:
            print("Digita una opción válida")
            return farmacia()
    except Exception as e:
        print("Ocurrió un error:", e)
        return farmacia()


@decoradores
def cosmetica():
    print("Elegiste la opción de cosmética")
    var = input("Si no quieres seguir en esta sección presiona N, de lo contrario digita S: ").lower()

    def generador():
        global turno_c
        turno_c += 1
        yield f"Tu turno es C-{turno_c}"

    try:
        if var == "s":
            generado = generador()
            print(next(generado))
        elif var == "n":
            print("Qué gusto haberte tenido aquí. Hasta luego.")
        else:
            print("Digita una opción válida")
            return cosmetica()
    except Exception as e:
        print("Ocurrió un error:", e)
        return cosmetica()

@decoradores
def lociones():
    print("Elegiste la opción de lociones")
    var = input("Si no quieres seguir en esta sección presiona N, de lo contrario digita S: ").lower()

    def generador():
        global turno_l
        turno_l += 1
        yield f"Tu turno es L-{turno_l}"

    try:
        if var == "s":
            generado = generador()
            print(next(generado))
        elif var == "n":
            print("Qué gusto haberte tenido aquí. Hasta luego.")
        else:
            print("Digita una opción válida")
            return lociones()
    except Exception as e:
        print("Ocurrió un error:", e)
        return lociones()
