import numpy as np
import matplotlib.pyplot as plt
import math

x = np.arange(1,4, 0.1)
plt.plot (x, [math.exp(y) - y**2+4*y-5 for y in x], 'y')
plt.grid(True)
plt.show()