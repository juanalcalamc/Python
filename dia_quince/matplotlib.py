import matplotlib.pyplot as plt
import numpy as np

%matplotlib inline

plt.plot()

a = [1,5,4,6,7,2,34,34,5,6,6,666]

plt.plot(a)


x = list(range(101))
y = []

for numero in x:
    y.append(numero**2)


plt.plot(x , y)

fig, ax =plt.subplots()

ax.plot(x, y)

ax.set(title="Grafico de casos de covid-19 en LATAM", xlabel="dias",ylabel="Casos confirmados")
fig.savefig("/ejemplograficoscovid-19.png")
#___________________________________________________________________________________________________

x_1= np.linspace(0,100, 20)
y_1 = x_1**2

fig,ax = plt.subplots()

ax.scatter(x_1, y_1)

fig, ax = plt.subplots()

x_2 = np.linspace(-10,10,100)
y_2 = np.sin(x_2)

ax.scatter(x_2,y_2)

#__________________________________________________________________________________________________

comida = {"lasaña":350,"sopa":150,"roast beef":650}

fig, ax =plt.subplot()
ax.bar(comida.keys(), comida.values())
ax.set(title="Precios de comidas", xlabel="Comidas", ylabel="Precios")

fig, ax =plt.subplot()
ax.barh(list(comida.keys()),list(comida.values()))
ax.set(title="Precios de comidas", xlabel="Comidas", ylabel="Precios")


x= np.random.randn(1000)

fig, ax =plt.subplot()
ax.hist(x)


fig, ((ax1, ax2),(ax3,ax4)) = plt.subplot(nrows=2,ncols=2, figsize=(10,5))

ax1.plot(x_1, y_1)

ax2.scatter(x_2, y_2)

ax3.bar(comida.keys(), comida.values())

ax4.hist(np.random.randn(1000))

plt.style.available()

plt.style.use('seaborn-whitegrid')

fig, ((ax1, ax2),(ax3,ax4)) = plt.subplot(nrows=2,ncols=2, figsize=(10,5))

ax1.plot(x_1, y_1, color='#faba03')

ax2.scatter(x_2, y_2, color='#ffba04')

ax3.bar(comida.keys(), comida.values(), color='#fbba03')

ax4.hist(np.random.randn(1000),color='#fcba03')