import cv2
import facial_recognition as fr
import os
import numpy
import datetime

ruta  = 'Empleados'
mis_imagenes= []
nombres_empleados=[]
lista_empleados= os.listdir(ruta)

for nombre in lista_empleados:
    imagen_actual = cv2.imread(f'{ruta}/{nombre}')
    mis_imagenes.append(imagen_actual)
    nombres_empleados.append(os.path.splitext(nombre)[0])

def codificar(imagenes):

    lista_codificada=[]
    

    for imagen in imagenes:
        imagen = cv2.cvColor(imagen, cv2.COLOR_BGR2RGB)

        codificado = fr.face_encodings(imagen)[0]

        lista_codificada.append(codificado)

    return lista_codificada

def registrar_ingresos(persona):
    f = open('registro.csv','r+')
    lista_datos= f.readlines()
    nombre_registro = []
    for linea in lista_datos:
        ingreso = linea.split(',')
        nombre_registro.append(ingreso[0])
    if persona not in nombre_registro:
        ahora = datetime.now()
        string_ahora=ahora.strftime('%H:%M:%S')
        f.writelines(f'\n{persona},{string_ahora}')
        


lista_empleados_codificada = codificar(mis_imagenes)


captura = cv2.VideoCapture(0, cv2.CAP_DSHOW)

exito, imagen = captura.read()
if not exito:
    print('No se a podido tomar la captura')
else:
    cara_captura= fr.face_locations(imagen)

    cara_captura_codificada = fr.face_encodigns(imagen,cara_captura)

    for caracodif,caraubi in zip(cara_captura_codificada, cara_captura):
        coincidencias= fr.compare_faces(cara_captura_codificada,caracodif)
        distancias = fr.face_distance(lista_empleados_codificada, caracodif)

        indice_concidencia = numpy.argmin(distancias)

        if distancias [indice_concidencia] > 0.6:
            print("No coincide con ninguno de mis empleados")

        else:
            nombre = nombres_empleados[indice_concidencia]
            y1,x2,y2,x1 = caraubi
            cv2.reactangle(imagen,(x1, y1), (x2, y2), (0,24,244), 2)
            cv2.rectangle(imagen, (x1, y2 -35), (x2, y1), (0,255,0), cv2.FILLED)
            cv2.PutText(imagen, nombre, (x1 +6, y2-6), cv2.FONT_HERHEY_COMPLEX,1 , (255,255,255))
            
            registrar_ingresos(nombre)

            cv2.imShow('imagen web', imagen)
            cv2.waitKey(0)
