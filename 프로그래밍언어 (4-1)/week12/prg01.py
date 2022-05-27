import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import pyplot as plt

df = pd.read_csv("./data/countries.csv")
#print(df.info())   #데이터 타입이 나온다
df["density"]=df['population']/df['area']
#df.drop(['capital'], axis=1,inplace=True) #열 삭제
df.plot(kind='bar',x='code',y='density',color="red")
plt.show()
print(df) #index->행



