import pandas as pd

df = pd.read_excel('c:/temp/output.xlsx',index_col="ID")
df.to_excel('c:/temp/output2.xlsx')
print("OK!")