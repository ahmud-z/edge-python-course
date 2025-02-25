import pandas as pd

df = pd.DataFrame({"category": ["A", "B", "C", "D"], "amount": [10, 20, 30, 40]})

print(df.aggregate("sum"))
