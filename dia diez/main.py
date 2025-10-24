import pygame
import random
import math
from pygame import mixer

#Iniciando pygames 
pygame.init()

#Creando y dar tamaño de la pantalla pantalla
pantalla=pygame.display.set_mode((800 , 600))

#Titulo e Icono
pygame.display.set_caption('Invación Espacial')
icono=pygame.image.load("alien.png")
pygame.display.set_icon(icono)
fondo=pygame.image.load("espacios.png")

#agregar musica 

mixer.music.load('MusicaFondo.mp3')
mixer.music.play(-1)


#Variables jugador 
img_jugador=pygame.image.load("rocket.png")
jugador_X=368
jugador_y=500
jugadorx_cambio=0

#Variables de enemigo 
img_enemigo=[]
enemigo_x=[]
enemigo_y=[]
enemigo_x_cambio=[]
enemigo_y_cambio=[]
cantidad_enemigos=8

for e in range(cantidad_enemigos):
    img_enemigo.append(pygame.image.load("ufo.png"))
    enemigo_x.append(random.randint(0,766))
    enemigo_y.append(random.randint(0,300))
    enemigo_x_cambio.append(1)
    enemigo_y_cambio.append(30)


#Variables de la bala 
img_bala=pygame.image.load("bullet.png")
bullet_x=0
bullet_y=500
bullet_x_cambio=0
bullet_y_cambio=4
bala_visible=False

#Puntaje
puntaje=0
fuente=pygame.font.Font('freesansbold.ttf',32)
txtox=10
textoy=10

#texto del final
fuente_final=pygame.font.Font('freesansbold.ttf',40)

def texto_final():
    mi_fuente_final=fuente_final.render("JUEGO TERMINADO",True,(255,255,255))
    pantalla.blit(mi_fuente_final,(60,200))

#funcion para mostrar puntaje 
def mostrar_puntaje(x, y):
    texto =fuente.render(f"Puntaje :{puntaje}",True,(250,255,255))
    pantalla.blit(texto,(x, y))



#Funcion jugador
def jugador(x, y):
    pantalla.blit(img_jugador,(x, y))

#Funcion de enemigo
def enemigo(x, y, ene):
    pantalla.blit(img_enemigo[ene], (x, y))

def disparar_bala(x, y):
    global bala_visible
    bala_visible=True
    pantalla.blit(img_bala,(x + 23, y + 10))

#Detectar  coliciones
def hay_colicion(x_1, y_1, x_2, y_2):
    distancia = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_1 - y_2, 2))
    if distancia < 27:
        return True
    else:
        return False


#Bucle del juego 
se_ejecuta=True
while se_ejecuta:
    #imagen del fondo
    pantalla.blit(fondo,(0,0))
    #Iteracion de eventos

    #Evento para cerrar el programam
    for evento in pygame.event.get():
        if evento.type==pygame.QUIT:
            se_ejecuta=False
        #Movimeito para las teclas derecha y izquierda 
        if evento.type==pygame.KEYDOWN:
            print("Una tecla fue precionada ")
            if evento.key == pygame.K_LEFT:
                jugadorx_cambio= -0.7
            if evento.key == pygame.K_RIGHT:
                jugadorx_cambio= 0.7
            #Balas 
            if evento.key == pygame.K_SPACE:
                if bala_visible == False:
                    sonido_bala=mixer.Sound('disparo.mp3')
                    sonido_bala.play()
                    bullet_x=jugador_X
                    disparar_bala(bullet_x,bullet_y)
        #Chequeo por si suelta la flecha 
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                jugadorx_cambio= 0

     #Crear el movimiento de jugardor            
    jugador_X+=jugadorx_cambio   

    #Mantener dentro de bordes al jugador
    if jugador_X <= 0:
        jugador_X=0  
    elif jugador_X >= 736:
        jugador_X= 736       

    #Crear el movimiento del enemigo            
    for e in range(cantidad_enemigos):
        #Fin del juego
        if enemigo_y[e] > 500:
            for k in range(cantidad_enemigos):
                enemigo_y[k]=1000
            texto_final()
            break

        enemigo_x[e]+=enemigo_x_cambio[e]  

    #Mantener dentro de bordes al jugador
        if enemigo_x[e] <= 0:
            enemigo_x_cambio[e]=0.5
            enemigo_y[e]+= enemigo_y_cambio[e]
        elif enemigo_x[e] >= 766:
            enemigo_x_cambio[e]=-0.5
            enemigo_y[e]+= enemigo_y_cambio[e]
            #Colicion
        colicion= hay_colicion(enemigo_x[e], enemigo_y[e], bullet_x, bullet_y)
        if colicion:
            sonido_colicion=mixer.Sound('Golpe.mp3')
            sonido_colicion.play()
            bullet_y=500
            bala_visible=False
            puntaje+=1
            print(puntaje)
            enemigo_x[e]=random.randint(0,766)
            enemigo_y[e]=random.randint(0,300)
    
        enemigo(enemigo_x[e], enemigo_y[e],e)
    #Movimiento bala
    if bullet_y<=-24:
        bullet_y=500
        bala_visible=False
    if bala_visible:
        disparar_bala(bullet_x,bullet_y)
        bullet_y -= bullet_y_cambio


    jugador(jugador_X, jugador_y)
    mostrar_puntaje(txtox,textoy)

    #Actualiza el juego
    pygame.display.update()

