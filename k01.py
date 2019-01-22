import pandas as pd

df = pd.DataFrame({"id":[1,2,3],
                   "name":['Nick','Box','Tom']},
                  index=['one','two','three'])

df.to_excel('C:/Users/Administrator/Desktop/out.xlsx')
print(df)