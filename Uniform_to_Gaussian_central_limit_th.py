from scipy.stats import uniform
from scipy.stats import norm
import matplotlib.pyplot as plt
import numpy as np
import math


n_bins = 20

def sum_of_uniform_variables(xi, xf, n_unif, min_vis, max_vis, n_points):
  uniform_variables = []
  x = np.linspace(min_vis, max_vis, n_points)
  for i in range(n_unif):
    uniform_variables.append(np.random.uniform(xi, xf, n_points))
  sum_of_uniforms = (1/math.sqrt(n_unif))*sum(uniform_variables)
  return x, sum_of_uniforms

fig, axs = plt.subplots(3, 3, sharey=True, tight_layout=True)
for i in range(3):
  for j in range(3):
    x, prob_distribution = sum_of_uniform_variables(-1.73, 
                                      1.73,
                                      1+j+50*i,
                                      -4,
                                      4,
                                      1000)
    axs[i][j].hist(prob_distribution, bins=n_bins, density=True)
    axs[i][j].plot(np.linspace(-1.73, 1.73, 1000), norm.pdf(x))

x, prova_func = sum_of_uniform_variables(-1.73, 
                                      1.73,
                                      4,
                                      -4,
                                      4,
                                      1000)

plt.show()
