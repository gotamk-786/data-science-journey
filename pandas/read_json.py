import pandas as pd
df = pd.read_json(
    "D:/6th semester/DS/DS_LAB/pandas/sample_data.json"
)

print(df)
print("head")
print(df.head())


# ---------------------------------
# • Dataset ki full info
# ---------------------------------
print(df.info())
