import pandas as pd
from google.colab import drive
import matplotlib as plt

drive.mount('/content/drive')

ventas_autos = pd.read_csv('/content/drive/MyDrive/tu_carpeta/tu_achivo')

numeros= pd.Series([1,2,3,4,5,67,35,235,62])
numeros.mean()#Promedio
numeros.sum()#Suma

colores= pd.Series(['rojos','amarillos','verdes'])
tipos_autos = pd.Series(['sedan','SUV', 'Pick up'])

tabla_autos= pd.DataFrame({'Tipo de auto': tipos_autos,"Color":colores})

ventas_autos.to_csv( '/content/drive/MyDrive/tu_carpeta/tu_nombrearchivo')

ventas_autos.describe()

ventas_autos.info()

ventas_autos.coloums()

ventas_autos.head()

ventas_autos.head(7)

ventas_autos.tail()

ventas_autos.loc[3]

ventas_autos.iloc[3,7,9]

ventas_autos['kilometraje']

ventas_autos['kilometraje'].mean()

ventas_autos[ventas_autos['kilometraje'] > 100000]

pd.crosstab(ventas_autos['fabricante'],ventas_autos['puertas'])

ventas_autos.groupby(['fabricante']).mean()

#matplotlib


ventas_autos['kilometraje'].plot
ventas_autos['kilometraje'].hist

ventas_autos['Precios (USD)'].plot

ventas_autos['Precios (USD)'] = ventas_autos['Precios (USD)'].str.replace("[\,\.\$]","")
ventas_autos['Precios (USD)'] = ventas_autos['Precios (USD)'].astype(int)/100
ventas_autos['Precios (USD)']

ventas_autos['Precios (USD)'].plot