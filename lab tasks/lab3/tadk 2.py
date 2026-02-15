import pandas as pd

data = {
    "item": ["cookies", "cake", "bagels", "bread"],
    "ingredient_cost_per_lb": [3.75, 4.00, 2.50, 3.00],
    "setup_cost": [1580, 2000, 680, 310],   # bread ka average setup cost
    "labor_cost_per_hr": [30, 30, 25, 40],
    "batch_output_units": [250, 5, 300, 1000],
    "batch_time_hr": [0.5, 1.5, 0.75, 2],    
    "ingredients_lb_per_batch": [15, 10, 20, None],
    "unit_price": [2.00, 34.00, 1.75, 3.00]
}

df = pd.DataFrame(data)
print("Dataset Created Successfully ")
print(df)
df.to_csv("bakery_menu_dataset.csv", index=False)
print("File saved as bakery_menu_dataset.csv ")

df["ingredient_cost_per_batch"] = df["ingredient_cost_per_lb"] * df["ingredients_lb_per_batch"]
df["labor_cost_per_batch"] = df["labor_cost_per_hr"] * df["batch_time_hr"]
df["total_cost_per_batch"] = df["ingredient_cost_per_batch"] + df["labor_cost_per_batch"]
df["revenue_per_batch"] = df["batch_output_units"] * df["unit_price"]
df["profit_per_batch"] = df["revenue_per_batch"] - df["total_cost_per_batch"]
df["profit_per_hour"] = df["profit_per_batch"] / df["batch_time_hr"]

print(df[["item", "profit_per_batch", "profit_per_hour"]])
df_clean = df.dropna()

print(df_clean[["item", "profit_per_batch", "profit_per_hour"]])
best_item = df_clean.loc[df_clean["profit_per_hour"].idxmax()]

print("\nBest Item:")
print(best_item["item"])
print("Profit per hour:", best_item["profit_per_hour"])
