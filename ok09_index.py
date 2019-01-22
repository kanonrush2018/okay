import pandas as pd

output = pd.read_excel('c:/temp/output.xlsx')
df = pd.read_excel('c:/temp/output.xlsx', index_col="李新")
df.to_excel('c:/temp/output2.xlsx')
print(output.head())

print('==================\n ok!')

output2 = pd.read_excel('c:/temp/output2.xlsx')
print(output2.head())
