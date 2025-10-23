import re 
texto="Si neseistas ayuda llama al siguiente numero 685-598-9977 las 24 horas al servicio"

patron='nada'
busqueda=re.search(patron,texto)
busqueda=re.findall(patron,texto)
print(busqueda)
print(busqueda.span())#Busca las ubicaciones la palabras
print(busqueda.start())#ubicacion del la primera)
print(busqueda.end())#la ultima
for hallazgo in re.finditer(patron, texto):
    print(hallazgo.span())
print(len(busqueda))
palabra='ayuda' in texto
print(palabra)


patron1=r'(\d{3})-(\d{3})-(\d{4{})}'
patron1=r'\d\d\d-\d\d\d-\d\d\d\d'
resultado=re.search(patron,texto)

print(resultado.group(1))


clave =input('clave: ')
patron2=r'\D{1}\w{7}'
chequear=re.search(patron2,clave)
print(chequear )

texto="No atendemos los lunes por las tardes"
buscar=re.search(r'lunes|martes', texto)
print(buscar)