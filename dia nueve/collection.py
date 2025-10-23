from collections import Counter
from collections import defaultdict
from collections import namedtuple
numeros= [6,6,6,5,5,7,5,43,54,63,43,5,463,4,52,53,5]
contador=(Counter(numeros))
print(Counter("missisipi"))
frase="al pan pan y al vino vino"
print(Counter(frase.split()))
print(contador)
serie=Counter([1,1,1,1,1,1,1,2,2,2,3,3,3,3,4,4,4,4])
print(serie.most_common())
print(list(serie))


mi_dict=defaultdict(lambda:'nada')
mi_dict['uno']='verde'


Persona= namedtuple('Persona',['nombre','altura','peso'])
ariel=Persona('Ariel',1.76,79)

mi_tupla=(500,5,18)

