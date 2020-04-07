#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from numpy import *
import numpy as np
from sklearn import preprocessing
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn import neighbors
from sklearn.model_selection import cross_val_score


# In[3]:


data =pd.read_csv(r'trainedustage.csv')
array = data.values

for i in range(len(array)):
	if array[i][0]=="Male":
		array[i][0]=1
	else:
		array[i][0]=0
       
df=pd.DataFrame(array)

maindf =df[[0,1,2,3,4,5,6]]
mainarray=maindf.values
print (mainarray)

temp=df[7]
train_y =temp.values
# print(train_y)
# print(mainarray)
train_y=temp.values        

for i in range(len(train_y)):
	train_y[i] =str(train_y[i])
    
mul_lr = linear_model.LogisticRegression(multi_class='multinomial', solver='newton-cg',max_iter =1000)
mul_lr.fit(mainarray, train_y)

testdata =pd.read_csv(r'testedustage.csv')    
test = testdata.values

for i in range(len(test)):
	if test[i][0]=="Male":
		test[i][0]=1
	else:
		test[i][0]=0

df1=pd.DataFrame(test)

testdf =df1[[0,1,2,3,4,5,6]]
maintestarray=testdf.values
print(maintestarray)  

y_pred = mul_lr.predict(maintestarray)      
for i in range(len(y_pred)) :
	y_pred[i]=str((y_pred[i]))

DF = pd.DataFrame(y_pred,columns=['Weak Spot (Class Label)'])
DF.index=DF.index+1
DF.index.names = ['Person No']
DF.to_csv("output7.csv")  

cv_score=cross_val_score(mul_lr,mainarray,train_y,cv=10)
print(cv_score.mean())


# In[7]:


from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix


# In[11]:





# In[ ]:




