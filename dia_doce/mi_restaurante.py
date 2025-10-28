from tkinter import *
import random
import datetime
from tkinter import filedialog, messagebox


operador=''
precios_comida = [1.32, 1.65, 2.31, 3.22, 1.22, 1.99, 2.05, 2.65]
precios_bebida = [0.25, 0.99, 1.21, 1.54, 1.08, 1.10, 2.00, 1.58]
precios_postres = [1.54, 1.68, 1.32, 1.97, 2.55, 2.14, 1.94, 1.74]

def click_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0,END)
    visor_calculadora.insert(END, operador)

def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0,END)

def obtener_resutado():
    global operador
    resultado=str(eval(operador))
    visor_calculadora.delete(0,END)
    visor_calculadora.insert(0,resultado)
    operador=''

def revisar_check():
    x=0 
    for c in cuadros_comida:
        if variables_comida[x].get() == 1:
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get() == '0':
                cuadros_comida[x].delete(0,END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state=DISABLED)
            texto_comidas[x].set(0)
        x += 1
    x=0 
    for c in cuadros_bebidas:
        if variables_bebidas[x].get() == 1:
            cuadros_bebidas[x].config(state=NORMAL)
            if cuadros_bebidas[x].get() == '0':
                cuadros_bebidas[x].delete(0,END)
            cuadros_bebidas[x].focus()
        else:
            cuadros_bebidas[x].config(state=DISABLED)
            texto_bebidas[x].set(0)
        x += 1

    x=0 
    for c in cuadros_postres:
        if variables_postres[x].get() == 1:
            cuadros_postres[x].config(state=NORMAL)
            if cuadros_postres[x].get() == '0':
                cuadros_postres[x].delete(0,END)
            cuadros_postres[x].focus()
        else:
            cuadros_postres[x].config(state=DISABLED)
            texto_postres[x].set(0)
        x += 1


def total():
    sub_total_comida = 0
    precio = 0
    for cantidad in texto_comidas:
        sub_total_comida = sub_total_comida + float(cantidad.get()) * precios_comida[precio]
        precio += 1

    sub_total_bebida = 0
    precio = 0
    for cantidad in texto_bebidas:
        sub_total_bebida = sub_total_bebida + float(cantidad.get()) * precios_bebida[precio]
        precio += 1


    sub_total_postre = 0
    precio = 0
    for cantidad in texto_postres:
        sub_total_postre = sub_total_postre + float(cantidad.get()) * precios_postres[precio]
        precio += 1
    
    sub_total=sub_total_comida + sub_total_bebida + sub_total_postre 
    impuesto =sub_total * 0.07
    total = sub_total + impuesto

    Varcosto_comida.set(f'$ {round(sub_total_comida,2)}')
    Varcosto_bebida.set(f'$ {round(sub_total_bebida,2)}')
    Varcosto_postre.set(f'$ {round(sub_total_postre,2)}')
    Var_subtotal.set(f'$ {round(sub_total,2)}')
    Var_impuesto.set(f'$ {round(impuesto,2)}')
    Var_total.set(f'$ {round(total,2)}')


def recibo():
    texto_recibo.delete(1.0 , END)
    numero_recibo=f'N# _ {random.randint(1000,9999)}'
    fecha = datetime.datetime.now()
    fecha_recibo= f'{fecha.day}/{fecha.month}/{fecha.year} - {fecha.hour}:{fecha.minute}'
    texto_recibo.insert(END, f'Datos:\t{numero_recibo}\t\t{fecha_recibo}\n')
    texto_recibo.insert(END, f'*'*63 + '\n')
    texto_recibo.insert(END, 'Items\t\tCant\t\Precios \n')
    
    x = 0
    for comida in texto_comidas:
        if comida.get()!= '0':
            texto_recibo.insert(END, f'{lista_comidas[x]}\t\t{comida.get()}\t$ {int(comida.get()) * precios_comida[x]}\n')
        x += 1
    
    x = 0
    for postre in texto_postres:
        if postre.get()!= '0':
            texto_recibo.insert(END, f'{lista_postres[x]}\t\t{postre.get()}\t$ {int(postre.get()) * precios_postres[x]}\n')
        x += 1

    x = 0
    for bebida in texto_bebidas:
        if bebida.get()!= '0':
            texto_recibo.insert(END, f'{lista_bebidas[x]}\t\t{bebida.get()}\t$ {int(bebida.get()) * precios_bebida[x]}\n')
        x += 1
    texto_recibo.insert(END, f'_'*42+'\n')
    texto_recibo.insert(END, f'Costo de la comida:\t\t\t{Varcosto_comida.get()}\n')
    texto_recibo.insert(END, f'Costo de las bebidas:\t\t\t{Varcosto_bebida.get()}\n')
    texto_recibo.insert(END, f'Costo de los postres:\t\t\t{Varcosto_postre.get()}\n')
    texto_recibo.insert(END, f'_'*42+'\n')
    texto_recibo.insert(END, f'Costo del  subtotal:\t\t\t{Var_subtotal.get()}\n')
    texto_recibo.insert(END, f'Costo de los impuestos:\t\t\t{Var_impuesto.get()}\n')
    texto_recibo.insert(END, f'Costo del total:\t\t\t{Var_total.get()}\n')
    texto_recibo.insert(END, f'*'*63 + '\n')
    texto_recibo.insert(END, "esperamos  que vuelva")


def guardar():
    info_recibo=texto_recibo.get(1.0 , END)
    archivo = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
    archivo.write(info_recibo)
    archivo.close()
    messagebox.showinfo('Infomacion de la factura','Su factura ha sudo guardada')

def resetear():
    texto_recibo.delete(0 ,END)
    for texto in texto_comidas:
        texto.set('0')
    for texto in texto_bebidas:
        texto.set=('0')
    for texto in texto_postres:
        texto.set=('0')
    
    for cuadro in cuadros_comida:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_bebidas:
        cuadro.config(state=DISABLED)
    for cuadro in cuadros_postres:
        cuadro.config(state=DISABLED)

    for v in variables_comida:
        v.set('0')
    for v in variables_bebidas:
        v.set('0')
    for v in variables_postres:
        v.set('0')

    Varcosto_comida.set('')
    Varcosto_bebida.set('')
    Varcosto_postre.set('')
    Var_subtotal.set('')
    Var_impuesto.set('')
    Var_total.set('')



#Inicar el TKinter
aplicacion=Tk()

#Tamaño de la ventana
aplicacion.geometry('1300x630+0+0')

#Evitar maximizar
aplicacion.resizable(0, 0)

#Titulo de la ventana
aplicacion.title("Restaurante")

#Color de fondo
aplicacion.config(bg='burlywood')

#Parte superios de la ventana
panel_superior=Frame(aplicacion, bd=1, relief = FLAT )
panel_superior.pack(side = TOP)

#Contenido del titulo
etiqueta_titulo = Label(panel_superior, text = 'Sistema de facturacion', fg = 'azure4',
                        font = ('Dosis',58), bg = 'burlywood', width = 27) 
etiqueta_titulo.grid(row=0, column=0)
panel_izquierdo= Frame(aplicacion, bd=1 , relief=FLAT, width=18, height=20)
panel_izquierdo.pack(side=LEFT)

panel_costos=Frame(panel_izquierdo, bd=1, relief=FLAT, bg='azure4', padx=50)
panel_costos.pack(side=BOTTOM)

#Panel de comida
panel_comidas = LabelFrame(panel_izquierdo, text='Comida' , font=('Dosis',19,'bold'), bd=1, relief=FLAT,fg='azure4')
panel_comidas.pack(side=LEFT)

#Panel de bebidas
panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas' , font=('Dosis',19,'bold'), bd=1, relief=FLAT,fg='azure4')
panel_bebidas.pack(side=LEFT)

#panel del postres
panel_postres = LabelFrame(panel_izquierdo, text='Postres' , font=('Dosis',19,'bold'), bd=1, relief=FLAT,fg='azure4')
panel_postres.pack(side=LEFT)

#panel derecha
panel_derecha= Frame(aplicacion, bd=1, relief=FLAT)
panel_derecha.pack(side=RIGHT)

#panel calculadora
panel_calculadora=Frame(panel_derecha, bd=1, relief=FLAT, bg='Burlywood')
panel_calculadora.pack()

#panel recibo 
panel_recibo=Frame(panel_derecha, bd=1, relief=FLAT, bg='Burlywood')
panel_recibo.pack()

#panel botones
panel_botones=Frame(panel_derecha, bd=1, relief=FLAT, bg='Burlywood')
panel_botones.pack()


#lsita de productos
lista_comidas = [
    "Hamburguesa",
    "Pizza",
    "Ensalaa",
    "Pollo",
    "Tacos",
    "Lasaña",
    "Arroz",
    "lentejas"
]

lista_bebidas = [
    "Agua",
    "Jugo",
    "Coca-Cola",
    "Limonada",
    "Té",
    "Cafe",
    "Batido",
    "Cerveza"
]

lista_postres = [
    "Pastel",
    "Helado",
    "Flan",
    "Tarta",
    "Brownie",
    "Gelatina",
    "Cheesecake",
    "leche"
]

#Biclo para crear un checkbuttom
#generar items comida
variables_comida=[]
cuadros_comida=[]
texto_comidas=[]
contador=0

for comida in lista_comidas:

    #Crear los checkbuttoms
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas, 
                         text=comida.title(), 
                         font=('Dosis',19,'bold')
                         , onvalue=1, 
                         offvalue=0, 
                         variable=variables_comida[contador],
                         command=revisar_check)
    comida.grid(row=contador, 
                column=0, 
                sticky=W)

    #Cuadros de entrada
    cuadros_comida.append('')
    texto_comidas.append('')
    texto_comidas[contador] = StringVar()
    texto_comidas[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas, 
                                     font=('Dosis',18,'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_comidas[contador])
    cuadros_comida[contador].grid(row=contador,
                                 column=1)
    contador += 1

#generar items bebidas
variables_bebidas=[]
cuadros_bebidas=[]
texto_bebidas=[]
contador=0
for bebidas in lista_bebidas:
    variables_bebidas.append('')
    variables_bebidas[contador] = IntVar()
    bebidas = Checkbutton(panel_bebidas,
                          text=bebidas.title(),
                          font=('Dosis',19,'bold')
                         , onvalue=1,
                         offvalue=0,
                         variable=variables_bebidas[contador],
                         command=revisar_check)
    bebidas.grid(row=contador,
                 column=0, 
                 sticky=W)
    
    cuadros_bebidas.append('')
    texto_bebidas.append('')
    texto_bebidas[contador] = StringVar()
    texto_bebidas[contador].set('0')
    cuadros_bebidas[contador] = Entry(panel_bebidas, 
                                     font=('Dosis',18,'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_bebidas[contador])
    cuadros_bebidas[contador].grid(row=contador,
                                 column=1)
    contador += 1

#generar items postres
variables_postres=[]
cuadros_postres=[]
texto_postres=[]
contador=0
for postres in lista_postres:
    variables_postres.append('')
    variables_postres[contador] = IntVar()
    postres = Checkbutton(panel_postres,
                          text=postres.title(),
                          font=('Dosis',19,'bold')
                         ,onvalue=1,
                         offvalue=0,
                         variable=variables_postres[contador],
                         command=revisar_check)
    postres.grid(row=contador, column=0, sticky=W)


    cuadros_postres.append('')
    texto_postres.append('')
    texto_postres[contador] = StringVar()
    texto_postres[contador].set('0')
    cuadros_postres[contador] = Entry(panel_postres, 
                                     font=('Dosis',18,'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_postres[contador])
    cuadros_postres[contador].grid(row=contador,
                                 column=1)
    contador += 1

Varcosto_comida=StringVar()
Varcosto_bebida=StringVar()
Varcosto_postre=StringVar()
Var_subtotal=StringVar()
Var_impuesto=StringVar()
Var_total=StringVar()


#Etiqueta de costos 

etiqueta_costo_comida = Label(panel_costos,
                              text='costo comida',
                               font=('Dosis,',12,'bold'),
                               bg='azure4',
                               fg='white')
etiqueta_costo_comida.grid(row=0,column=0)

texto_costo_comida=Entry(panel_costos,
                        font=('Dosis,',12,'bold'),
                        bd=1,
                        width=10,
                        state='readonly',
                        textvariable=Varcosto_comida)

texto_costo_comida.grid(row=0, column=1, padx=41)


etiqueta_costo_bebida = Label(panel_costos,
                              text='costo bebida',
                               font=('Dosis,',12,'bold'),
                               bg='azure4',
                               fg='white')
etiqueta_costo_bebida.grid(row=1,column=0)

texto_costo_bebida=Entry(panel_costos,
                        font=('Dosis,',12,'bold'),
                        bd=1,
                        width=10,
                        state='readonly',
                        textvariable=Varcosto_bebida)

texto_costo_bebida.grid(row=1, column=1, padx=41)


etiqueta_costo_postre = Label(panel_costos,
                              text='costo postre',
                               font=('Dosis,',12,'bold'),
                               bg='azure4',
                               fg='white')
etiqueta_costo_postre.grid(row=2,column=0)

texto_costo_postre=Entry(panel_costos,
                        font=('Dosis,',12,'bold'),
                        bd=1,
                        width=10,
                        state='readonly',
                        textvariable=Varcosto_postre)
texto_costo_postre.grid(row=2, column=1, padx=41)

etiqueta_subtotal = Label(panel_costos,
                              text='Subtotal',
                               font=('Dosis,',12,'bold'),
                               bg='azure4',
                               fg='white')
etiqueta_subtotal.grid(row=0,column=2)

texto_subtotal=Entry(panel_costos,
                        font=('Dosis,',12,'bold'),
                        bd=1,
                        width=10,
                        state='readonly',
                        textvariable=Var_subtotal)

texto_subtotal.grid(row=0, column=3, padx=41)

etiqueta_impuesto = Label(panel_costos,
                              text='Impuesto',
                               font=('Dosis,',12,'bold'),
                               bg='azure4',
                               fg='white')
etiqueta_impuesto.grid(row=1,column=2)

texto_impuesto=Entry(panel_costos,
                        font=('Dosis,',12,'bold'),
                        bd=1,
                        width=10,
                        state='readonly',
                        textvariable=Var_impuesto)

texto_impuesto.grid(row=1, column=3, padx=41)

etiqueta_total = Label(panel_costos,
                              text='Total',
                               font=('Dosis,',12,'bold'),
                               bg='azure4',
                               fg='white')
etiqueta_total.grid(row=2,column=2)

texto_total=Entry(panel_costos,
                        font=('Dosis,',12,'bold'),
                        bd=1,
                        width=10,
                        state='readonly',
                        textvariable=Var_total)

texto_total.grid(row=2, column=3, padx=41)

#Botones 

botones =['total', 'recibo', 'guardar', 'resetear']
botones_creados=[]

columnas= 0

for boton in botones:
    boton= Button(panel_botones, 
                  text=boton.title(),
                  font=('Dosis', 14 ,'bold'),
                  fg='white',
                  bg='azure4',
                  bd=1,
                  width=9)
    botones_creados.append(boton)
    boton.grid(row=0, column=columnas)
    columnas+=1
botones_creados[0].config(command=total)
botones_creados[1].config(command=recibo)
botones_creados[2].config(command=guardar)
botones_creados[3].config(command=resetear)
                         
#Area de recibo
texto_recibo=Text(panel_recibo,
                  font=('Dosis',12,'bold'),
                  bd=1,
                  width=42,
                  height=10)
texto_recibo.grid(row=0,column=0)

#calculadora 
visor_calculadora=Entry(panel_calculadora,
                        font=('Dosis',16,'bold'),
                        width=32,
                        bd=1)
visor_calculadora.grid(row=0, column=0, columnspan=4)

#Bucle para los botones
botones_calculadora=['7','8','9','+','4','5','6','-',
                     '1','2','3','x','R','B','0','/']
botones_guardado=[]
fila=1
columnas=0
for boton in botones_calculadora:
    boton=Button(panel_calculadora,
                 text=boton.title(),
                 font=('Dosis',16,'bold'),
                 fg='white',
                 bg='azure4',
                 bd=1,
                 width=8)
    botones_guardado.append(boton)
    boton.grid(row=fila, 
               column=columnas)
    if columnas == 3:
        fila+=1

    columnas+=1
    if columnas ==4:
        columnas= 0

botones_guardado[0].config(command = lambda : click_boton('7'))
botones_guardado[1].config(command = lambda : click_boton('8'))
botones_guardado[2].config(command = lambda : click_boton('9'))
botones_guardado[3].config(command = lambda : click_boton('+'))
botones_guardado[4].config(command = lambda : click_boton('4'))
botones_guardado[5].config(command = lambda : click_boton('5'))
botones_guardado[6].config(command = lambda : click_boton('6'))
botones_guardado[7].config(command = lambda : click_boton('-'))
botones_guardado[8].config(command = lambda : click_boton('1'))
botones_guardado[9].config(command = lambda : click_boton('2'))
botones_guardado[10].config(command = lambda : click_boton('3'))
botones_guardado[11].config(command = lambda : click_boton('*'))
botones_guardado[12].config(command =obtener_resutado)
botones_guardado[13].config(command = borrar)
botones_guardado[14].config(command = lambda : click_boton('0'))
botones_guardado[15].config(command = lambda : click_boton('/'))



#Evita que la pantalla se cierre
aplicacion.mainloop()