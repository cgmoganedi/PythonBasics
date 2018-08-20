import numpy as np
import pandas as pd

# working with 3D data

randItems1 = np.random.randn(4, 3)
randItems2 = np.random.randn(4, 2)
dataDict = {
    'item1': pd.DataFrame(randItems1),
    'item2': pd.DataFrame(randItems1)
}

dataPanel = pd.Panel(dataDict)

print(dataPanel)

print(dataPanel['item2'])