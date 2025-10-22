def mi_funcion():
    lista=[]
    for x in range(1,5):
        lista.append(x * 10)
    return lista

def mi_generador():
    for x in range(1,5):
        yield x * 10

g = mi_generador()
print(next(g))
 
print(mi_funcion())
print(mi_generador())

def mi_generado1():
    x = 1
    yield x

    x += 1
    yield x

    x += 1
    yield x

    x += 1
    yield x

g = mi_generado1()

print(next(g))
print(next(g))
print(next(g))