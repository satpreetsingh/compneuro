import numpy as np
x = np.arange(5)
y = -np.arange(5)
x[y<2] = 0
import pdb; pdb.set_trace()
x *= 9
print(x)
