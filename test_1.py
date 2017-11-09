from numpy.random import *
import matplotlib.pyplot as plt
import numpy as np

pg1 = [5.000e-1,5.000e-1,5.000e-1,5.000e-1,5.000e-1,5.000e-1,5.000e-1,5.000e-1,5.000e-1,5.000e-1]
pg2 = [5.000e-1,5.000e-1,5.000e-1,5.000e-1,5.000e-1,5.000e-1,5.000e-1,5.000e-1,5.000e-1,5.000e-1]

for i in range(100000):
    for j in range(10):
		a = choice([0,1],1)
		if a==1:
			pg1[j] = 0.001 + 0.999 * pg1[j]
			pg2[j] = 0.999 * pg2[j]
		else:
			pg1[j] = 0.999 * pg1[j]
			pg2[j] = 0.001 + 0.999 * pg2[j]
print pg1

left = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
plt.bar(left, pg1)

plt.show()
