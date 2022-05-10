# 경영정보학과 1851782 이소정
import matplotlib.pyplot as plt
import numpy as np

heights=np.array([1.83,1.76,1.69,1.86,1.77,1.73])
weights=np.array([86,74,59,95,80,68])

bmi=heights/weights**2
print(bmi)
plt.boxplot(bmi)
plt.show()


