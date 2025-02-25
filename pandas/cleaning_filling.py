import pandas as pd
import numpy as np

df = pd.DataFrame(
    {
        "name": ["nuzaifa", np.nan, "nabhan", "niloy", "bob"],
        "age": [5, 3, np.nan, 20, np.nan],
    }
)


print(df.isnull().sum())

df["name"] = df["name"].fillna("Mr")
df["age"] = df["age"].fillna(100)
print(df)