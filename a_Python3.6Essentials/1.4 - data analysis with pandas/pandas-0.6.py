import pandas as pd
import numpy as np
data_series = pd.Series(np.random.randn(1000))
head = data_series.head(5)
tail = data_series.tail(5)
print(data_series.describe())
print(data_series.std()**2 == data_series.var())

df = pd.DataFrame(
    {
        'one':[1,2,3],
        'two':[4,5,6],
        'three':[7,8,9]
    },
    index=['a','c','a']
)
print(df)
df2 = df.sort_index()
df3 = df.sort_index(axis=1, ascending=False)
df4 = df.sort_index(by='two', ascending=False)
print(df.apply(np.mean))
df.apply(np.median, axis=1)
