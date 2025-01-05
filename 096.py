import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 50)
y1 = np.sin(x)
y2 = np.sin(x) + 1

plt.fill_between(x, y1, alpha=0.6, label='Data 1')
plt.fill_between(x, y2, alpha=0.6, label='Data 2')

plt.title('Cumulative Trend Over Time (Area Chart)')
plt.legend()
plt.show()