import numpy as np
import matplotlib.pyplot as plt
from  scipy.stats import pearsonr as correlation

points = np.linspace(-100, 100, 100)

T = np.random.uniform(0, 1, 100)
U = np.random.uniform(0, 1, 100)
V = np.random.uniform(0, 1, 100)

variables = [T, U, T+V, -T+V] # (X, Y, W, Z )

corr_coeff = [correlation(variables[0], variables[i]) for i in range(1, len(variables))]

print("Pearson's correlation coefficient between variables (X, Y), is: ", corr_coeff[0])
print("Pearson's correlation coefficient between variables (X, W), is: ", corr_coeff[1])
print("Pearson's correlation coefficient between variables (X, Z), is: ", corr_coeff[2])

plt.plot(points, T)
plt.plot(points, U)
plt.plot(points, V)
plt.ylim(-2, 2)
#plt.show()
