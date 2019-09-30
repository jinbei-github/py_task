
# coding: utf-8

# In[4]:


#方法一：pandas类库读取文件
import pandas as pd
data=pd.read_csv('xjdb1.csv',encoding = 'utf-8')
print(data)


# In[15]:


#方法二：numpy类库读取文件
import numpy as np
data2=np.loadtxt('xjdb1.csv',dtype=np.str,encoding='UTF-8')
print(data2)


# In[37]:


#方法三：csv类库读取文件
import csv
data3 = []
with open('xjdb1.csv','r',encoding = 'utf-8') as csvfile:
    csv_reader = csv.reader(csvfile)  # 使用csv.reader读取csvfile中的内容
    data3_header = next(csv_reader)  # 读取第一行每一列的标题
    for row in csv_reader:  # 将csv 文件中的数据保存到data3中
        data3.append(row)
print(data3)
#for row in data3:
#    print(row)

