import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 4*np.pi, 100)

y1 = np.sin(x)
y2 = np.cos(x)

plt.subplot(2,1,1)
plt.plot(x, y1)
plt.title("sin(x)")
plt.grid()

plt.subplot(2,1,2)
plt.plot(x, y2)
plt.title("cos(x)")
plt.grid()

plt.show()