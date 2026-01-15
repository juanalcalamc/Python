# importanciones
from random import *


# codigo
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}, Cuenta: {self.numero_cuenta}, Balance: ${self.balance}"

    def depositar(self, monto):
        print(
            f"Dinero tranferido con exito ahora en tu cuenta se encuentra esta cantidad de dinero {self.balance}"
        )
        self.balance += monto

    def retirar(self, monto):
        if monto > self.balance:
            print("No se puede retirar ese monto no tienes tanto dinero en tu cuenta")
        else:
            print("Dinero retirado con exito")
            self.balance -= monto


def crear_usuario():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    numero_cuenta = randint(1000, 9999)
    balance = float(input("Balance inicial: "))
    return Cliente(nombre, apellido, numero_cuenta, balance)


def menu(cliente):
    var = input("¿Continuamos? Presiona S para continuar o N para cancelar: ").lower()
    while var == "s":
        var2 = input("¿Qué quieres hacer?\n1. Retirar\n2. Depositar\nOpción: ")
        if var2 == "1":
            monto = float(input("¿Qué monto quieres retirar?: "))
            cliente.retirar(monto)
        elif var2 == "2":
            monto = float(input("¿Qué monto quieres depositar?: "))
            cliente.depositar(monto)
        else:
            print("Opción inválida.")
        print(f"Tu balance actual es {cliente.balance}")
        var = input("¿Deseas hacer otra operación? (S/N): ").lower()


def inicio_menu(contrasena_guardada):
    intentos = 3
    while intentos > 0:
        contra = input("""Hola, bienvenido a bancoyo digista tu contraseña """)
        if contra == contrasena_guardada:
            print("Acceso aceptado")
            cliente = crear()
            print(cliente)
            menu(cliente)
            return
        else:
            intentos -= 1
            print(f"Haz fallado tus intentos restantes son{intentos}")
        print("Ya no tienes mas intentos")


contrasena_guardada = ""

var = input("""¿Ya tienes cuenta?
1. Si tienes, presiona 1
2. Si no tienes, presiona 2
Opción: """)

if var == "1":
    contrasena_guardada = input("Digite su contraseña: ")
    inicio_menu(contrasena_guardada)
elif var == "2":
    contrasena_guardada = input("Por favor crea una contraseña que puedas recordar: ")
    print("Cuenta creada exitosamente.")
    inicio_menu(contrasena_guardada)
else:
    print("Opción inválida.")
