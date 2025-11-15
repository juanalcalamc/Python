import bs4
import requests

# Resultado de una busqueda
resultado = requests.get(
    "https://www.escueladirecta.com/l/products?sortKey=name&sortDirection=asc&page=1"
)


sopa = bs4.BeautifulSoup(resultado.text, "lxml")
# # print(sopa.select('title')[0].getText())

# columna = sopa.select('.post-body entry-content float-container')
# print(columna)
# for  p in columna:
#     print(p.getText())


imagen = sopa.select(".ProductImage.object-cover.w-full.aspect-video")[0]["src"]
print(imagen)
imagen_curso = requests.get(imagen)

f = open("imagen.jpg", "wb")
f.write(imagen_curso.content)
f.close
