#1-1
import numpy as np
a=np.arange(1,46)

#2. 2차원 array로 바꿔라
n_arr= a.reshape(9,5)

#1-3
print("첫번째 원소=", n_arr[0,0])
print("마지막 원소=", n_arr[8,4])
print("마지막 원소=", n_arr[-1,-1])

#1-4
n_arr[7:,0:2]