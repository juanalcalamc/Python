import numpy as np
import pandas as pd

array_unidim = np.array([1,2,3,4,5])
array_bidim = np.array([[1,2,3], [4,5,6]])
array_tridim = np.array([[[1,2,3],[4,5,6]], [[7,8,9],[10,11,12]]])

# Inspección
print(array_unidim.shape, array_unidim.ndim, array_unidim.dtype, array_unidim.size, type(array_unidim))
print(array_bidim.shape, array_bidim.ndim, array_bidim.dtype, array_bidim.size, type(array_bidim))
print(array_tridim.shape, array_tridim.ndim, array_tridim.dtype, array_tridim.size, type(array_tridim))

# DataFrame
datos = pd.DataFrame(array_bidim)
print(datos)

# Arrays especiales
print(np.ones((4, 3)))
print(np.zeros((2,4,3)))
print(np.arange(0,100,5))
print(np.random.randint(0,10,(2,5)))
print(np.random.random((3,5)))

# Semilla y array único
np.random.seed(27)
array_4 = np.random.randint(0,10,(3,5))
print(array_4)
print(np.unique(array_4))

array_4[:2, :2]

array_4[1]

array_4[:2] 

array_4[:2,:2]

array_5 = np.random.randint(0,10,(3,5))
array_6= np.ones((3,5))

array_7=np.ones((5,3))

array_8=np.ones((5,3))

array_9=np.random.randint(1,5,(3,3))
array_10=np.random.randint(1,5,(3,3))