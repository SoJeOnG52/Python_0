import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv("./data/titanic.csv")
df.drop(['PassengerId', 'Name', 'Ticket'],axis=1, inplace=True)
#print(df.info())
table = df.pivot_table(df, ['Sex', 'Pclass'], aggfunc={'Survived' : np.sum})
table.plot(kind='bar', color='red')
plt.show()
print(table)