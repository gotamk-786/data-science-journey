import pandas as pd 
import numpy as np
df1=pd.read_csv(r"D:\6th semester\DS\DS_LAB\lab tasks\lab 2\data1.csv", index_col=0)
df2=pd.read_csv(r"D:\6th semester\DS\DS_LAB\lab tasks\lab 2\data2.csv", index_col=1)
print(df1)

print("\n")
print(df2)

df3=pd.concat([df1,df2])

print("\n")
print("df3 is:")
print(df3)
print("\n")
#C
df4 = pd.read_csv(r"D:\6th semester\DS\DS_LAB\lab tasks\lab 2\data3.csv", index_col=0)
print("df4:")
print(df4)
df5=pd.concat([df3,df4],axis=1)
print(df5)
print("\n")
#D

df6=pd.read_json(r"D:\6th semester\DS\DS_LAB\lab tasks\lab 2\data.json")
df7=pd.concat([df5,df6])
#E
df7 = df7.applymap(lambda x: np.nan if isinstance(x, str) else x)
#F
df7 = df7.fillna(df7.mean())
print("Final DataFrame:")
print(df7)

df7.to_csv("newdata.csv", index=False)
