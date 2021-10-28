# 3D hisogram built following the example code found at:
# https://matplotlib.org/stable/gallery/mplot3d/hist3d.html

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.stats import pearsonr as correlation

# WARNING: Computation time and memory load varies drastically
# from bins_number[2] to bins_number[3]!
bins_number = [10, 50, 100, 300]

# Starting variables: X normally distributed, Y = 10 + X + Y_R, 
# Y_R being a normally distributed variable ~N(0,36)
x = np.random.normal(0, 15, 100000)
y_R = np.random.normal(0, 36, 100000)
y = 10 + x + y_R
corr_coeff = correlation(x,y)

# Definition of a 2D array to evaluate covariance for variables X and Y
XY = np.vstack((x, y))
covariance = np.cov(XY)

# Initialization of a np.2dhistogram and its grid for 3d representation
histo3d, xedges, yedges = np.histogram2d(x, y, 
			bins=bins_number[1], 
			range=[[-60, 60], [-120, 120]])
xpos, ypos = np.meshgrid(xedges[:-1] + 0.25, 
			 yedges[:-1] + 0.25, 
			 indexing="ij")
xpos = xpos.ravel()
ypos = ypos.ravel()
zpos = 0

# Definition of arrays for the dimensions of the bars constituting 
# the 3d histogram
dx = dy = 0.5 * np.ones_like(zpos)
dz = histo3d.ravel()

fig1, ax = plt.subplots(1, 3)
plt.get_current_fig_manager().set_window_title('Marginal densities')
secax = ax[0].twinx()
ax[0].hist(y, bins=50, color='red', label='Y', density=True)
secax.hist(x, bins=50, label='X', density=True)
ax[0].legend(loc='upper left')
secax.legend(loc='upper right')
ax[0].set_title('Comparison between X and Y probability distributions')
ax[1].set_title('Marginal density of variable X')
ax[1].hist(x, bins=50, density=True)
ax[2].set_title('Marginal density of variable Y')
ax[2].hist(y, bins=50, color='red', density=True)
fig1.tight_layout()

fig2 = plt.figure("3D histogram of conjunct density of variables (X, Y)")
ax_1 = fig2.add_subplot(122)
ax_1.hist2d(x, y, bins=50, density=True)
ax_1.set_title('2D scatter plot of conjunct density (X,Y)', fontsize='x-large')
ax_1.set_xlabel('X', fontsize='large')
ax_1.set_ylabel('Y', fontsize='large')
ax_2 = fig2.add_subplot(121, projection='3d')
ax_2.bar3d(xpos, ypos, zpos, dx, dy, dz, zsort='average')
ax_2.set_title('3D histogram of conjunct density (X,Y)', fontsize='x-large')
ax_2.set_xlabel('X', fontsize='large')
ax_2.set_ylabel('Y', fontsize='large')
ax_2.set_zlabel('(X,Y)', fontsize='large')
fig2.tight_layout()

print("The covariance matrix for variables X and Y is: \n", 
      covariance,
      "\n\u03C3_xy: ",
      covariance[0][1],
      "\n\u03C1: ",
      corr_coeff[0])

plt.show()
