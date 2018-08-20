import pandas as pd
csvData = pd.read_csv('./../0.0 - data/data.csv')
# header = X
# header = None, names = ['time', 'space', 'range']
# index_col = X
# index_col = False
series_data = pd.DataFrame() # or something like that

series_data.to_csv('export_file.csv')

series_data.to_csv('exported_file.csv', header=False, index=False)

# mode=a for appending an existing file