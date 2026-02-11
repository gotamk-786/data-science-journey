import pandas as pd

data = {
    "Name": ['ram','arsaln','gotam','jagdesh','rohit','rave','kalesh','umash'],
    "Age": [10,20,30,40,50,60,48,30],
    "salary": [50000,60000,45000,49000,70000,48000,5000,55000], 
    "Performance Score": [85,90,78,92,88,95,80,89]              
}
df=pd.DataFrame(data)

print("Sample dataframe")
print(df)

print("Names (single column return series)")
name=df['Name']  # filter single colums in series
print(name)


# selecting multiple colums
subset=df[["Name","salary"]]
print('\n subset with Name and salary')
print(subset)