# import matplotlib.pyplot as plt

# x = [1,2,3,4]
# y = [1,2,3,4]
# z = [2,4,6,8]
# plt.plot(x,y)
# plt.plot(x,z)
# plt.ylabel('some numbers')
# plt.show()

import numpy as np
from scipy.stats import mstats
import matplotlib.pyplot as plt

# Create 10 columns with 100 rows of random data
rd = np.random.randn(100, 10)
# Calculate the quantiles column wise
quantiles = mstats.mquantiles(rd, axis=0)
# Plot it
labels = ['25%', '50%', '75%']
for i, q in enumerate(quantiles):
    plt.plot(q, label=labels[i])
plt.legend()
plt.show()