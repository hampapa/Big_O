import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer

# O(1)
n = 100

def constTime(n):
    # This operation is taking the same time, no matter how big n is
    n -= 1
    return n

x = np.zeros(n)
y = np.zeros(n)
for i in range(0,n):
    start = timer()
    constTime(i+1)
    end = timer()
    x[i] = i
    y[i] = (end - start)*10000000

plt.scatter(x, y, alpha=0.5)
plt.ylim([min(y)*0.9, max(y[5:])*1.1])
plt.title("O(1)")
plt.show()
