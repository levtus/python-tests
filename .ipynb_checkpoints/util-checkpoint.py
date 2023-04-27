import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 8, 1, 10])

plt.xlabel('xaxis')
plt.ylabel('yaxis')

plt.plot(ypoints, linestyle = 'dashed', marker = '.', color = 'r')

plt.grid()

plt.show() 

