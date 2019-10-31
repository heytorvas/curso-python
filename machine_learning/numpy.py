import numpy as np

data = np.genfromtxt('iris.data', delimiter=',', usecols=(0,1,2,3))

print(data)