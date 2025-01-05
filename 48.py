import matplotlib.pyplot as plt
import numpy as np

data = [np.random.normal(0, std, 100) for std in range(1, 4)]

plt.violinplot(data)
plt.xlabel('Data')
plt.ylabel('Density')
plt.title('Violin Plot')
plt.show()