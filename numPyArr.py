import numpy as np
#one dimesional array
n=np.array([1,2,3,4,5])
print(n)
print(n[2])

#2D array
a=np.array([[1,2,3],[3,4,5]])
print(a)
print(a[1,1])

#3D array
b=np.array([[[1,2,3],[3,4,5]],[[4,5,6],[5,8,9]]])
print(b)
print(b[1,1,1])

#random number generator

from numpy import random
x=random.randint(100000)
print(x)