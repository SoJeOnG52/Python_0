import numpy as np
import matplotlib.pyplot as plt
ftemp=[63,73,80,86,78,54,66]
f = np.array(ftemp)
c= (f-32)*0.55
print(c)

## plot 작성
plt.plot(c)
plt.show()
