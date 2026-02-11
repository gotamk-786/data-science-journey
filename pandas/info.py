import pandas as pd 
data={
    "name":['ram','gotam','radhi'],
    "age":['10','20','30'],
    "city":['karachi','badin','hyd']
}

df=pd.DataFrame(data)

print("display the info method data set")
print(df.info())
