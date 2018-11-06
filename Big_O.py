import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer


# O(1), constant time
n = 100

def constTime(n):
    # This operation is taking the same time, no matter how big n is
    start = timer()
    n -= 1
    end = timer()
    return (end - start)

# mc is the number of Monte Carlo like simulations of the algorithm
mc = 100
r = n*mc
x = np.zeros(r)
y = np.zeros(r)
cnt = 0
for j in range(0,mc):
    for i in range(0,n):
        x[cnt] = i
        y[cnt] = constTime(i+1)*10000000
        cnt += 1
        
plt.scatter(x, y, alpha=0.5)
print(np.mean(y), np.std(y))
plt.ylim([min(y)*0.9, np.mean(y)+np.std(y)])
plt.title("O(1)")
plt.show()


# O(log n) - logarithmic time
n = 100000

def logTime(n):
    start = timer()
    while n > 1:
        n /= 2
    end = timer()
    return (end - start)

# mc is the number of Monte Carlo like simulations of the algorithm
mc = 5
r = n*mc
x = np.zeros(r)
y = np.zeros(r)
cnt = 0
for j in range(0,mc):
    for i in range(0,n):
        x[cnt] = i
        y[cnt] = logTime(i+1)*10000000
        cnt += 1
        
plt.scatter(x, y, alpha=0.5)
print(np.mean(y), np.std(y))
# learning from a data visualization perspective: need to find a proper
# range for the y-values, so the logarithmic characteristic can be seen
# tweaking n, mc and ylim by hand
plt.ylim([min(y)*0.9, 35])
plt.title("O(log n)")
plt.show()
