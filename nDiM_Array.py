
import numpy as np

# One D
ar1=np.arange(1,10).reshape(1,9,1)
print(ar1.ndim)
# Two D
arr1=np.arange(1,9).reshape(4,2)
print(arr1)
# three D
arr2=np.arange(1,21).reshape(2,5,2)
print(arr2)

# Attributes 
print(ar1.ndim)
print(arr1.shape)
print(ar1.size)
print(arr1.dtype)
print(ar1.itemsize)
print(ar1.data)

