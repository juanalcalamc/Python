def suma():
    n1=int(input("Ingrese un numero: "))
    n2=int(input("Ingrese un numero: "))
    print(n1 + n2)
    print("Gracias por sumar en mi programa")

try:
    suma()

except:
    print("Algo salio mal ")

else:
    print("Todo salio bien")
    
finally:
    print("Ya eso es todo")

