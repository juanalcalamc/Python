import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

# Escuchas nuestro microfono y devolver el audio


def transformar_audio_en_texto():
    # Almacenar el reconocedor en una variable
    r = sr.Recognizer()

    # Configurar el micrifono
    with sr.Microphone() as origen:
        # Tiempo de espera
        r.pause_threshold = 0.8

        # informar que comenzo la grabacion
        print("Ya puedes hablar")

        # Guardar lo que escuche como audio
        audio = r.listen(origen)

        try:
            # Buscar en google lo que haya escuchado
            pedido = r.recognize_google(audio, language="es-ES")

            # prueba de que pudo ingresar y transfomar
            print("Dijiste: " + pedido)

            # devolver a pedido
            return pedido

        # En casa de que no comprendan
        except sr.UnknownValueError:
            # prueba de que no comprendio el audio
            print("No je,repite ")
            # Devovler algo
            return "Sigo esperando"
        except sr.RequestError:
            # prueba de audioi
            print("No je,El audio no se pudo mandar correctamente a la nube ")
            # Devovler algo
            return "Sigo esperando"
        # Error inesperado
        except:
            # prueba de que no comprendio el audio
            print("No je,lo que pudo malir sal salio mal  ")
            # Devovler algo
            return "Sigo esperando"


def hablar(mensaje):
    # Encerder el motor de pytttsxx3
    engine = pyttsx3.init()

    # Pronunciar el mensaje
    engine.say(mensaje)
    engine.runAndWait()


# Informar dia de la semana


def pedir_dia():
    dia = datetime.date.today()
    print(dia)

    dia_semana = dia.weekday()
    print(dia_semana)

    # diccionario nombre de dias
    calendario = {
        0: "lunes",
        1: "Martes",
        2: "Miércoles",
        3: "Jueves",
        4: "Viernes",
        5: "Sabado",
        6: "Domingo",
    }
    # Decir el dia de la semana
    hablar(f"Hoy es {calendario[dia_semana]}")


def pedir_hora():
    hora = datetime.datetime.now()
    hora = f"En este momento son las {hora.hour} horas y  {hora.minute} minutos"
    print(hora)

    hablar(hora)


def saludo_inical():
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = "Buenas noches"
    elif hora.hour >= 6 and hora.hour < 13:
        momento = "Buen dia "
    else:
        momento = "Buenas tardes"
    hablar(f"{momento}, Soy DaCO, Tu asistente personal")


def pedir_cosas():
    saludo_inical()

    comenzar = True

    while comenzar:
        pedido = transformar_audio_en_texto().lower()

        if "abrir youtubr" in pedido:
            hablar("Con gusto")
            webbrowser.open("https://www.youtube.com/?app=desktop&hl=es")
            continue
        elif "abrir navegador" in pedido:
            hablar("Claro estoy en eso")
            webbrowser.open("https://www.google.com/?hl=es")
            continue
        elif "que dia es hoy" in pedido:
            pedir_hora()
            continue
        elif "busca en wikipedia" in pedido:
            hablar("Buscando eso en wikipedia")
            pedido = pedido.replace("busca en wikipedia", "")
            wikipedia.set_lang("es")
            resultado = wikipedia.summary(pedido, sentences=3)
            hablar("wikipedia dice lo siguente")
            hablar(resultado)
            continue
        elif "Busca en internet" in pedido:
            hablar("Muy bien estoy trabajando en eso ")
            pedido = pedido.replace("Busca en internet", "")
            pywhatkit.search(pedido)
            hablar("Esto es lo que he encontrado")
            continue
        elif "reproducir" in pedido:
            hablar("Buena idea ya estoy en su reproduccion")
            pywhatkit.playonyt(pedido)
            continue
        elif "broma" in pedido:
            hablar(pyjokes.get_joke("es"))
            continue
        elif "precio de las acciones" in pedido:
            accion = pedido.split("de")[-1].strip()
            cartera = {"apple": "APPL", "amazon": "AMZN", "google": "GOOGL"}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info["regularMarketPrice"]
                hablar(f"La encontre el precio de {accion} es {precio_actual}")
                continue
            except:
                hablar("Perdon pero no la he encontrado")
                continue
        elif "adiós" in pedido:
            hablar(
                "Esta bien estare pendiente de igual formar si requieres algo avisama"
            )
            break


pedir_cosas()
