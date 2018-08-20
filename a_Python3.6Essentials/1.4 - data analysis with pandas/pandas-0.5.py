import pandas as pd
#reading excel
data_frame1 = pd.read_excel('filename.xsl',sheetname='sheet1')
excel_data = pd.ExcelFile('filename.xsl')
# writng excel
df = pd.DataFrame()
df.to_excel('outfile.xslx',sheet='Sheet1')