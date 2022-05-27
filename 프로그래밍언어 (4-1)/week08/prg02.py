import numpy as np
h=[1.83,1.76,1.69,1.86,1.77,1.73]
w=[86,74,59,95,80,68]
bmi=[]
for i in range(len(h)):
    bmi.append(w[i]/h[i]**2)
print(bmi)
h1= np.array(h)  #array 자료형으로 변경
w1=np.array(w)
bmi1= w1/h1**2
print(bmi1)



