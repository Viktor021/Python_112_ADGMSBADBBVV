import numpy as np

def minkowski_distance(x, y, p):
    return np.sum(np.abs(x-y) ** p) ** (1 / p)


x = np.array([1,2,3])
y = np.array([4,5,6])

distance = minkowski_distance(x,y, p=3)
print("Minkowski Distance:", distance)