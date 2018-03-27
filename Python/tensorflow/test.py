import numpy as np
import matplotlib.pyplot as plt

num_points = 200
vectors_set = []
for i in range(num_points):
  x = np.random.normal(5,5)+15
  y =  x*1000+ (np.random.normal(0,3))*1000
  vectors_set.append([x,y])


x_data = [v[0] for v in vectors_set ]
y_data = [v[1] for v in vectors_set ]

plt.plot(x_data, y_data , 'ro')
plt.ylim([0,40000])
plt.xlim([0,35])
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()