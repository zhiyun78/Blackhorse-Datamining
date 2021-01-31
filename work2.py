import pandas as pd
import numpy as np

# 2..100间隔2 求和
print(np.arange(2,100,2).sum())

# 作业第2题 成绩求和排序
data = {'Chinese': [66, 95, 93, 90,80], 'Math': [30, 98, 96, 77, 90], 'English': [65, 85, 92, 88, 90]}

df2 = pd.DataFrame(data, index=['ZhangFei', 'GuanYu', 'LiuBei', 'DianWei', 'XuChu'], columns= ['Chinese', 'Math', 'English'])
print(df2.describe())

df2['sum']=df2.sum(axis=1)

print(df2.sort_values('sum',ascending=False))

