import pandas as pd
# Two dimensional data

d1 = {'one':[1,2,3,4], 'two':[7,6,5,4]}
df1 = pd.DataFrame(d1)

# accessing
col1 = df1['one'] #column

a = df1['one'][2] #specific elment is a row

# accessing
row2 = df1.loc[1] # second row

b = df1.loc[1][1] # the second element of the second row

#print(b)
