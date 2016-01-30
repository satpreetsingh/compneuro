import pickle
import matplotlib.pyplot as plt
import numpy as np

def next_w(delta_t, n, alpha, w, u):
    v = np.dot(u, w)
    #return delta_t*n*( v*u - alpha*v*v*w )
    return delta_t*n*( v*u )

with open('c10p1.pickle', 'rb') as f:
    data = pickle.load(f)['c10p1']
xmean = sum([elem[0] for elem in data])/len(data)
ymean = sum([elem[1] for elem in data])/len(data)
xmean = np.random.rand()*5

ymean = np.random.rand()*5
data = np.array([ [elem[0] - xmean, elem[1] - ymean] for elem in data ])
w = np.random.random_sample((2,)) #w0

'''plt.scatter(data[:, 0], data[:, 1])
plt.plot(w[0], w[1], 'ro')
plt.show()
'''

for i in range(1000):
    w = w + next_w(0.01, 1, 1, w, data[i%len(data)])

print w
#plt.scatter(data[:, 0], data[:, 1])

'''plt.plot(w[0], w[1], 'ro')
plt.show()'''
