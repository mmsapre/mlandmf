import numpy as np

# initializing points in
# numpy arrays
point1 = np.array((2, 3))
point2 = np.array((5, 7))

# calculate Euclidean distance
# using linalg.norm() method
dist = np.linalg.norm(point1 - point2)

# printing Euclidean distance
print(dist)