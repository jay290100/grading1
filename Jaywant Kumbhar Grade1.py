#!/usr/bin/env python
# coding: utf-8
Que 11  ans-4)python is only interpreted2  ans-3)it indicates privet variable of class3  ans-2)4  ans-1)5  ans-2)
# In[69]:


#1
a =input("enter a string   ")

b=a[1::2]
print("even index car", b)


# In[65]:


#2
n=[12,75,150,180,145,525,50]
for i in n:
    if i>=500:
         break
    if (i%5==0) and (i<=150) :
        print(i)


# In[70]:


#3
n=[1,2,3,4,5,6,7]
for i in n:
    i=i*i
    print (i)


# In[81]:


#4
days=['sun','mon','tue','wen','thu','fri','sat']
temp=[30.5,32.6,31.8,33.4,29.8,30.2,29.9]
week_tempc={day:temp for day,temp in zip(days,temp)}
print(week_tempc)


# In[ ]:


#5
from 52 cards pick 2
dependom probability
prob of picking 1 card is king is 4/52
prob of picking 2nd card is king is 3/51
then probability of picking 2 king is   4/52*3/51= 1/221


# In[104]:


#6
#Method overriding : Both has same method ( class method gets called)
a=int(input('enter first no  '))
b=int(input('enter secound no  '))
class Shape:
    def area(self,radius,b=0):
        return 3.14 * radius * radius
     
    def area(self,l,b):
        return l * b 
c=Shape()
c.area(a,b)


# In[85]:


#7
a=int(input('enter  no  '))
if a%5==0 & a%7 :
    print(a)
else:
    print('its not divisible by 5 and 7')


# In[ ]:


#8
types of distribution
1)normal distribution
2)binomial distribution
3)poission distribution
4)exponential destribution


# In[ ]:


#9
the central limit theorem  states that the distribution of a sample variable approximates a normal 

distribution (bell) as the sample size becomes larger, assuming that all samples are
identical in size, and regardless of the population's ctual distribution.
  

It needs to be sampled at random.
One sample should not impact the others.
When taking samples without replacement  sample size should not exceed 10% of the population


# In[86]:


#10
a=int(input('enter first no  '))
b=int(input('enter secound no  '))
def multi():
    c=a*b
    print(c)
def substraction():
    d=a-b
    print(d)
    
multi()
substraction()

Que 3
# In[91]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as mlt
import seaborn as sns


# In[108]:


a=pd.read_csv(r'C:\Users\Jay\Downloads\supermarket_sales - Sheet1.csv')
a


# In[109]:


#1 
a= a.drop(['Invoice ID','Date','Time',], axis = 1)


# In[110]:


a

#2
sns.boxplot(x='Gender',y='Payment',data=a)
mlt.showa.pivot_table(index=['Gender','Payment'],values=['Gender'], aggfunc='mean')
# In[103]:


a.describe()


# In[99]:


#3
highst_sell=a['Product line'].value_counts().head(20)
highst_sell


#Fashion accessories       178    have highst sell category


# In[97]:


#4
f, ax = mlt.subplots(1,3, figsize=(30,5))
sns.boxplot(x='Unit price', data=a, ax=ax[1])
sns.boxplot(x='gross income', data=a, ax=ax[1])
sns.boxplot(x='Rating', data=a, ax=ax[2])
mlt.show


# In[18]:


#5
mlt.figure(figsize=(11, 6))
sns.heatmap(a.corr(),annot = True, vmin = -1, vmax = 1)
mlt.show()


# In[ ]:




