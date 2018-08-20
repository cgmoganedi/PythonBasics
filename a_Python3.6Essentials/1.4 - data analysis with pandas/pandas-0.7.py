import pandas as pd
df = pd.DataFrame(
    {
        'one':[1,2,3],
        'two':[4,5,6],
        'three':[7,8,9]
    },
    index=['a','c','a']
)
#lambda expressions

df.apply(lambda x: 2*x, axis=1)
df.applymap(lambda x: x*x)
print(df['two'].map(lambda x: 2*x))