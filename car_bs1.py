import pandas as pd
import numpy as np

data = pd.read_csv('car_complain.csv')
data['brand']=data['brand'].str.replace('-','')
data2 = data.loc[:, ['id', 'brand']]
data3 = data.loc[:, ['id', 'problem']]
# df1 每条投诉的问题列表
df1 = pd.DataFrame({'id': [], 'prob': []})
for i in range(len(data)):
   ltt = data3.iloc[i]['problem'].split(',')
   ltt.pop() #去掉最后的空记录
   df1=df1.append(pd.DataFrame({'id': np.full(len(ltt),data3.iloc[i]['id']), 'prob': ltt}))

# df3为品牌子问题清单
df3=pd.merge(data2,df1)
df3=df3.drop(columns='id')

data6=data.groupby('brand').size().sort_values(ascending=False)
print('品牌问题数')
print(data6)
print('车型问题数')
print(data.groupby('car_model').size().sort_values(ascending=False))

#求品牌的平均车型投诉最多，首先统计品牌车型数
data8=data.loc[:,['brand','car_model']].drop_duplicates().groupby('brand').size()
data9=pd.DataFrame({'n_problem':data6,'n_model':data8,'aver':0})
data9['aver']=data9['n_problem']/data9['n_model']

print(data9.sort_values('aver',ascending=False))











