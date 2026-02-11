import pandas as pd
# df = pd.read_csv(
#     "D:/6th semester/DS/DS_LAB/pandas/sales_data_sample.csv",
#     encoding="latin1"
# )

# ---------------------------------
# • Excel (.xlsx) file read kar rahe hain
# • openpyxl engine explicitly specify kiya
# • xlrd error permanently fix
# ---------------------------------
df = pd.read_excel(
    "D:/6th semester/DS/DS_LAB/pandas/SampleSuperstore.xlsx",
    engine="openpyxl"
)

# ---------------------------------
# • First 5 rows print (data check)
# ---------------------------------
print(df.head())

# ---------------------------------
# • Dataset ki full info
# ---------------------------------
print(df.info())
