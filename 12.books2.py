import pandas as pd

books2 = pd.read_excel('c:/temp/books2.xlsx',index_col="ID")
# books2['Price'] = books2['ListPrice'] * books2['Discount']

# for i in books2.index:
#     books2['Price'].at[i] = books2['ListPrice'].at[i] * books2['Discount'].at[i]



books2['ListPrice'] = books2['ListPrice'].apply(lambda x:x+2)

for i in range(5,16):
    books2['Price'].at[i] = books2['ListPrice'].at[i] * books2['Discount'].at[i]


print(books2)