import pandas as pd

df = pd.DataFrame({"姓名":['李新','袁红秋','郎曼'],'性别'
:['男','女','女']})

df.set_index("姓名")

df.to_excel('c:/temp/output2.xlsm')
print(df)
print("=======================\nok!")

