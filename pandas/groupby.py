import pandas as pd

df = pd.DataFrame({"category": ["A", "A", "B", "B"], "amount": [10, 20, 30, 40]})

grouped = df.groupby("category").sum()

print(grouped)
