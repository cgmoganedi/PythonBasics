#Series : Iterate over each element
#DataFrame : Iterate over the columns
#Panel : Iterate over the item labels
import pandas as pd
df = pd.DataFrame(
    {
        'one':[1,2,3],
        'two':[4,5,6],
        'three':[7,8,9]
    },
    index=['a','c','a']
)
for col in df:
    print(df[col].mean())

for row_index, row in df.iterrows():
    print(row_index)
    print(row)