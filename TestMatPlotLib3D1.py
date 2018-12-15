import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

import random

fig = plt.figure()
objectMirsad = fig.add_subplot(111, projection='3d')


objectMirsad.scatter(0, 0, 0)

for i in range (0,1000):
    x = random.randint(-100,100)
    y = random.randint(-100, 100)
    z = random.randint(-100, 100)
    objectMirsad.scatter(x, y, z)



plt.show()



