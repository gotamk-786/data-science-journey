import pandas as pd 
data={
    "name":['ram','gotam','radhi'],
    "age":['10','20','30'],
    "city":['karachi','badin','hyd']
}

df=pd.DataFrame(data)
print(df)
df.to_csv("output.xlsx",index=False) # yhe index jaisa 0,1,2 arha ha yhe na ahy is liye index=False used kiya hai

#to_csv mein save karny k liye output
# to_excel se excel file mein sav karny k liye
# to_json se output json file mein save hoga 


#gcsfs for google cloud se data read karna 
#     name  ...     city
# 0    ram  ...  karachi
# 1  gotam  ...    badin
# 2  radhi  ...      hyd

