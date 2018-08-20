import numpy as np
import pandas as pd

a = np.random.normal(25, 5, 20)
pdData = pd.Series(a)
pdData2 = pd.Series(a, dtype=np.float64)
# print(pdData)
# Operator overloading
pdData3 = 2* pdData

# accessing via indices
pdData3[3] = 42
print(pdData3[:]) # Just as you would by default in python
