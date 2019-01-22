import pandas as pd

people = pd.read_excel('C:/Temp/People.xlsx',header=None)

people.columns = ['ID','Type','Title','FirstName','MiddleName','LastName']
people.set_index("ID",inplace=True)
print(people.columns)

people.to_excel('c:/temp/output.xlsx')
print('----Ok!-----')