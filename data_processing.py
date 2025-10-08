import pandas as pd

files = ["data/daily_sales_data_0.csv", "data/daily_sales_data_1.csv", "data/daily_sales_data_2.csv"]

processed = []
for f in files:
    df = pd.read_csv(f)
    df = df[df["product"] == "pink morsel"]
    df["price"] = df["price"].replace('[\$,]', '', regex=True).astype(float)
    df["sales"] = (df["quantity"] * df["price"]).map(lambda x: f"${x:.2f}")
    df = df.drop(columns=["product", "quantity", "price"])
    df = df[["sales", "date", "region"]]
    processed.append(df)

combined = pd.concat(processed, ignore_index=True)
combined.to_csv("data_formatted.csv", index=False)
