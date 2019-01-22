import pandas as pd

People = pd.read_excel('c:/temp/People.xlsx', header=None)

print(People.shape)

People.columns = ['李新', '袁红秋', '张剑楠', '李坤', '郎曼', '李小爱']
#People = People.set_index('李新')
People.set_index("李新", inplace=True)
print(People.columns)

People.to_excel('c:/temp/output.xlsx')

print(People.head())
print('===========================\n ok!')
print(People.tail())
print(People.columns)
print('===========================\n ok!')
