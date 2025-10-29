from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox

from mi_restaurante import *


operador = ""
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]


def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(END, operador)


def borrar():
    global operador
    operador = ""
    visor_calculadora.delete(0, END)


def obtener_resutado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0, resultado)
    operador = ""


def revisar_check():
    x = 0
    for c in cuadros_comida:
        if variables_comida[x].get() == 1:
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get() == "0":
                cuadros_comida[x].delete(0, END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state=DISABLED)
            texto_comidas[x].set(0)
        x += 1
    x = 0
    for c in cuadros_bebidas:
        if variables_bebidas[x].get() == 1:
            cuadros_bebidas[x].config(state=NORMAL)
            if cuadros_bebidas[x].get() == "0":
                cuadros_bebidas[x].delete(0, END)
            cuadros_bebidas[x].focus()
        else:
            cuadros_bebidas[x].config(state=DISABLED)
            texto_bebidas[x].set(0)
        x += 1

    x = 0
    for c in cuadros_postres:
        if variables_postres[x].get() == 1:
            cuadros_postres[x].config(state=NORMAL)
            if cuadros_postres[x].get() == "0":
                cuadros_postres[x].delete(0, END)
            cuadros_postres[x].focus()
        else:
            cuadros_postres[x].config(state=DISABLED)
            texto_postres[x].set(0)
        x += 1


def total():
    sub_total_comida = 0
    precio = 0
    for cantidad in texto_comidas:
        sub_total_comida = (
            sub_total_comida + float(cantidad.get()) * precios_comida[precio]
        )
        precio += 1

    sub_total_bebida = 0
    precio = 0
    for cantidad in texto_bebidas:
        sub_total_bebida = (
            sub_total_bebida + float(cantidad.get()) * precios_bebida[precio]
        )
        precio += 1

    sub_total_postre = 0
    precio = 0
    for cantidad in texto_postres:
        sub_total_postre = (
            sub_total_postre + float(cantidad.get()) * precios_postres[precio]
        )
        precio += 1

    sub_total = sub_total_comida + sub_total_bebida + sub_total_postre
    impuesto = sub_total * 0.07
    total = sub_total + impuesto

    Varcosto_comida.set(f"$ {round(sub_total_comida, 2)}")
    Varcosto_bebida.set(f"$ {round(sub_total_bebida, 2)}")
    Varcosto_postre.set(f"$ {round(sub_total_postre, 2)}")
    Var_subtotal.set(f"$ {round(sub_total, 2)}")
    Var_impuesto.set(f"$ {round(impuesto, 2)}")
    Var_total.set(f"$ {round(total, 2)}")


def recibo():
    texto_recibo.delete(1.0, END)
    numero_recibo = f"N# _ {random.randint(1000, 9999)}"
    fecha = datetime.datetime.now()
    fecha_recibo = (
        f"{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}"
    )
    texto_recibo.insert(END, f"Datos:\t{numero_recibo}\t\t{fecha_recibo}\n")
    texto_recibo.insert(END, f"*" * 63 + "\n")
    texto_recibo.insert(END, "Items\t\tCant\t\Precios \n")

    x = 0
    for comida in texto_comidas:
        if comida.get() != "0":
            texto_recibo.insert(
                END,
                f"{lista_comidas[x]}\t\t{comida.get()}\t$ {int(comida.get()) * precios_comida[x]}\n",
            )
        x += 1

    x = 0
    for postre in texto_postres:
        if postre.get() != "0":
            texto_recibo.insert(
                END,
                f"{lista_postres[x]}\t\t{postre.get()}\t$ {int(postre.get()) * precios_postres[x]}\n",
            )
        x += 1

    x = 0
    for bebida in texto_bebidas:
        if bebida.get() != "0":
            texto_recibo.insert(
                END,
                f"{lista_bebidas[x]}\t\t{bebida.get()}\t$ {int(bebida.get()) * precios_bebida[x]}\n",
            )
        x += 1
    texto_recibo.insert(END, f"_" * 42 + "\n")
    texto_recibo.insert(END, f"Costo de la comida:\t\t\t{Varcosto_comida.get()}\n")
    texto_recibo.insert(END, f"Costo de las bebidas:\t\t\t{Varcosto_bebida.get()}\n")
    texto_recibo.insert(END, f"Costo de los postres:\t\t\t{Varcosto_postre.get()}\n")
    texto_recibo.insert(END, f"_" * 42 + "\n")
    texto_recibo.insert(END, f"Costo del  subtotal:\t\t\t{Var_subtotal.get()}\n")
    texto_recibo.insert(END, f"Costo de los impuestos:\t\t\t{Var_impuesto.get()}\n")
    texto_recibo.insert(END, f"Costo del total:\t\t\t{Var_total.get()}\n")
    texto_recibo.insert(END, f"*" * 63 + "\n")
    texto_recibo.insert(END, "esperamos  que vuelva")


def guardar():
    info_recibo = texto_recibo.get(1.0, END)
    archivo = filedialog.asksaveasfile(mode="w", defaultextension=".txt")
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo("Infomacion de la factura", "Su factura ha sudo guardada")


def resetear():
    texto_recibo.delete(0, END)
    for texto in texto_comidas:
        texto.set("0")
    for texto in texto_bebidas:
        texto.set = "0"
    for texto in texto_postres:
        texto.set = "0"

    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebidas:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postres:
        cuadro.config(state=DISABLED)

    for v in variables_comida:
        v.set("0")
    for v in variables_bebidas:
        v.set("0")
    for v in variables_postres:
        v.set("0")

    Varcosto_comida.set("")
    Varcosto_bebida.set("")
    Varcosto_postre.set("")
    Var_subtotal.set("")
    Var_impuesto.set("")
    Var_total.set("")
