import pandas as pd
from datetime import date,timedelta

def add_month(d,md):
    yd = md //12
    m = d.month + md % 12
    if m != 12:
        yd += m//12
        m = m%12
    return date(d.year +yd,m,d.day)


books = pd.read_excel('c:/temp/books.xlsx',skiprows=3,usecols='c:f',
                      dtype={'ID': str,'InStore':str,'Date':str})
#print(books)
# books['ID'].at[1]=100
# print(books["ID"])

start = date(2018,1,1)
for i in books.index:
    books["ID"].at[i] = i + 1
    books['InStore'].at[i] = 'Yes'if i % 2 == 0 else 'No'
    books['Date'].at[i] = add_month(start,i)

books.set_index('ID',inplace=True)
books.to_excel('c:/temp/output4.xlsx')
print('ok:)')


