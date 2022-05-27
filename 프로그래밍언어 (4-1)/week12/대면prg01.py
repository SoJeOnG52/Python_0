import pandas as pd
import matplotlib.pyplot as plt
busan = pd.read_csv("./data/busanIndex-1.csv")
#print(busan['index'])
print(busan[['economic','heath','index']].corr()) #인덱스와 경제의 관계가 가깝다고
plt.scatter(busan['economic'],busan['index'], color="blue") #라인 그래프는 추세를 볼 때, 박스는 분포를 볼 때
plt.show()