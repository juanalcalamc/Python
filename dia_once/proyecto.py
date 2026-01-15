import bs4
import requests

# Esta es la url de la pagina web y crea una url sin numero de pagina
url_base = "https://books.toscrape.com/catalogue/page-{}.html"

# resultado=requests.get(url_base.format('1'))

# sopa=bs4.BeautifulSoup(resultado.text, 'lxml')

# libros=sopa.select('.product_pod')

# ejemplo=libros[0].select('a')[1]['title']

# print(ejemplo)

# Lista de titulos con 4 o 5 estrellas
titulos_rating_altos = []

# Bucle para entrar en las paginas

for pagina in range(1, 51):
    # Crear sopa para las pagianas
    url_pagina = url_base.format(pagina)
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, "lxml")

    # Seleccion datos de los libros
    libros = sopa.select(".product_pod")
    # Bucle para la pagina
    for libro in libros:
        # Mirar si tiene mas de 4 estrellas
        if (
            len(libro.select(".star-rating.Four")) != 0
            or len(libro.select(".star-rating.Five")) != 0
        ):
            # Guarda titulo en variable
            titulo_libro = libro.select("a")[1]["title"]

            # agregar libro a las lista
            titulos_rating_altos.append(titulo_libro)


# Ver libro de 4 y 5 estrellas en consola

for t in titulos_rating_altos:
    print(t)
