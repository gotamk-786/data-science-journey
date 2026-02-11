import pandas as pd

data = {
    "Name": ['ram','arsaln','gotam','jagdesh','rohit','rave','kalesh','umash'],
    "Age": [10,20,30,40,50,60,48,30],
    "salary": [50000,60000,45000,49000,70000,48000,5000,55000], 
    "Performance Score": [85,90,78,92,88,95,80,89]              
}

df = pd.DataFrame(data)
print("sample dataframe")
print(df)
print("Descriptive statistics")
print(df.describe())
