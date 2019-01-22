# 创建Excel文件
import pandas as pd

df = pd.DataFrame({'id':[1,2,3],'name':['Nick','Box','Tom'],'coloar':['blue','yello','red'],
                   'gender':['male','female','middle'],'work':['有工作','没工作','找工作']},)
df = df.set_index('id')
df.to_excel('C:/Users/Administrator/Desktop/output.xlsx')
print(df)