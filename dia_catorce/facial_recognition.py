import cv2  
import facial_recognition as fr


foto_control= fr.load_image_file("foto_a.jpg")
foto_prueba= fr.load_image_file("foto_b")

foto_control= cv2.cvt.cvtColor(foto_control,cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cv.tColor(foto_prueba, cv2.COLOR_BGR2RGB)


lugar_cara_a = fr.face_localtion(foto_control)[0]
cara_codificada_a = fr.face_encodig(foto_control)[0]

cv2.rectangle(foto_control,
              (lugar_cara_a[3], lugar_cara_a[0]),
              (lugar_cara_a[1], lugar_cara_a[2]),
              (0,255,0),
              2)

lugar_cara_b = fr.face_localtion(foto_prueba)[0]
cara_codificada_b = fr.face_encodig(foto_prueba)[0]

cv2.rectangle(foto_prueba,
              (lugar_cara_b[3], lugar_cara_b[0]),
              (lugar_cara_b[1], lugar_cara_b[2]),
              (0,255,0),
              2)

resultado = fr.compare_faces([cara_codificada_a], cara_codificada_b)

distance = fr.face_distance([cara_codificada_a], cara_codificada_b)

cv2.putText(foto_prueba,
            f'{resultado} {distance.round(2)}',
            (50,50),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (255,0,0),
            2)


cv2.imgShow('foto_control',foto_control)
cv2.imgShow('foto_prueba',foto_prueba)

cv2.waitKey(0)