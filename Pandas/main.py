#Dictionary using Dataframe

import pandas as pd

data = {
    'cars': ["BMW", "Volvo", "Ford"],
    'passings': [3, 7, 2]
}

df = pd.DataFrame(data, index=["a", "b", "c"])

print(df)

# Refer to the row index
print(df.loc["a"])

# Use a list of indexes
print(df.loc[["a", "b"]])

# Get column names
a = df.keys()
print(a)

# Get values as a NumPy array
b = df.values
print(b)
