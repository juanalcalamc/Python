
def cambiar_letras(tipo):  
    @decorar_saludo
    def mayuscula(texto):
        print(texto.upper())
    @decorar_saludo
    def minuscla(texto):
        print(texto.lower())
        
    if tipo=='may':
        return mayuscula
    elif tipo == 'min':
        return minuscla
    
def decorar_saludo(funcion):
    
    def otra_funcion(palabra):
        print("Hola")
        funcion(palabra)
        print ("Adios")
    return(otra_funcion)


 
hola=("perro")
operacion=cambiar_letras('may')
operacion('palabra')

