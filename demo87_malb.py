import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import numpy as np

mu = 100
sigma = 8
X = mu+sigma*np.random.randn(10000)
print len(X)
num_bins = 50
plt.hist(X, num_bins, density=1, facecolor='blue')
plt.show()