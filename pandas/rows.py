# head() tail()
# head(n)--> display first n rows if not pass n it keep blank then by default it show first 5 rows
# head() 5
# tail(n)
import pandas as pd
df = pd.read_json("D:/6th semester/DS/DS_LAB/pandas/sample_data.json")

print("display first 10 rows")
print(df.head(10))

print("display last 10 rows")
print(df.tail(10))
