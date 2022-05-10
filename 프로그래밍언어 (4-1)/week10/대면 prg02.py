#경영정보학과 1851782 이소정
#3.
import matplotlib.pyplot as plt
import numpy as np
h=np.random.normal(175,10,1000)
plt.hist(h)
plt.show()
print(h.mean())
print(h.std())


