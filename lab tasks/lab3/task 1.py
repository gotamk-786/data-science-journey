import pandas as pd

df = pd.read_csv(r"D:\6th semester\DS\data_science_pratical\lab tasks\lab3\archive\zomato.csv")
print("Shape:", df.shape)
print("\nFirst 5 rows:\n", df.head())
print("\nColumns list:\n", df.columns)


# part 1: deleting Redundant Columns
df = df.drop(["url", "phone", "reviews_list", "dish_liked", "menu_item"], axis=1)
print("\nAfter dropping redundant columns:")
print("Shape:", df.shape)
print("Columns now:\n", df.columns)

# part 2: renaming Column
df = df.rename(columns={"approx_cost(for two people)": "cost_for_two"})
print("\nAfter renaming column:")
print(df.columns)


# part 3: drop Duplicates
print("\nNumber of duplicate rows:", df.duplicated().sum())
df = df.drop_duplicates()
print("\nAfter removing duplicates:")
print("Shape:", df.shape)


#part 4:cleaning
print("\nUnique values in rate column:")
print(df["rate"].unique()[:10])

df = df[df["rate"] != "NEW"]
df = df[df["rate"] != "-"]
df["rate"] = df["rate"].str.replace("/5", "")
df["rate"] = df["rate"].astype(float)
print("\nRate column cleaned successfully")
print(df["rate"].head())
print("Shape after rate cleaning:", df.shape)

#part 5:remove NaN
print("\nMissing values in each column:")
print(df.isnull().sum())
df = df.dropna()

print("\nAfter removing NaN values:")
print("Shape:", df.shape)

#part 6:Some more transformations (cost column clean)
print("\nMissing values in each column:")
print(df.isnull().sum())
df = df.dropna()

print("\nAfter removing NaN values:")
print("Shape:", df.shape)

df.to_csv("zomato_cleaned.csv", index=False)

print("\n Saved file as zomato_cleaned.csv ")
print("\nFinal Cleaned Data Shape:", df.shape)
print("\nFinal Cleaned Data (First 10 rows):\n")
print(df.head(10))