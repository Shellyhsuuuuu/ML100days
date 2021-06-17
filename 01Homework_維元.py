#!/usr/bin/env python
# coding: utf-8

# # [作業目標]
# 
# 1. [簡答題] 請問下列兩種將 Array 轉換成 List 的方式有何不同？
# 
# ```
# print('list(a): ', list(a))
# print('tolist(): ', a.tolist())
# ```
# 
# 2. 請試著在程式中印出以下三個 NdArray 的屬性？（屬性：ndim、shape、size、dtype、itemsize、length、type）
# 
# ```
# a = np.random.randint(10, size=6) 
# b = np.random.randint(10, size=(3,4)) 
# c = np.random.randint(10, size=(2,3,2)) 
# ```
# 
# 3. 如何利用 list(...) 實現 a.tolist() 的效果？試著用程式實作。
# 

# # 作業 

# ### 1. [簡答題] 請問下列兩種將 Array 轉換成 List 的方式有何不同？
# 
# ```
# print('list(a): ', list(a))
# print('tolist(): ', a.tolist())
# ```
# 

# In[9]:


import numpy as np 

a = np.random.randint(10, size=10)

print('list(a):', list(a))
print('a.tolist():', a.tolist())

b = np.random.randint(10, size=6).reshape(3,2)  

print('list(b):', list(b))
print('b.tolist():', b.tolist())


# ### 2. 請試著在程式中印出以下三個 NdArray 的屬性並且解釋結果？（屬性：ndim、shape、size、dtype、itemsize、length、type）
# 
# ```
# a = np.random.randint(10, size=6) 
# b = np.random.randint(10, size=(3,4)) 
# c = np.random.randint(10, size=(2,3,2)) 
# ```

# In[10]:


# 記得先 Import 正確的套件
import numpy as np

a = np.random.randint(10, size=6)

print(a)
print(a.ndim)
print(a.shape)
print(a.size)    ##
print(a.dtype)  #位元
print(a.itemsize) 
print(len(a))  ##不屬於arrary屬性
print(type(a)) #不屬於arrary屬性


# In[11]:


b = np.random.randint(10, size=(3,4)) 

print (b)
print (b.ndim)
print (b.shape)
print (b.size)
print (b.dtype)
print (b.itemsize)
print (len(b))
print (type(b))


# In[13]:


c = np.random.randint(10, size=(2,3,4)) 

print (c)
print (c.ndim)
print (c.shape)
print (c.size)
print (c.dtype)
print (c.itemsize)
print (len(c))
print (type(c))


# ### 3. 如何利用 list(...) 實現 a.tolist() 的效果？試著用程式實作。
# 

# In[14]:


a = np.random.randint(10, size=6) 

print(a.tolist())
print(list(a))


# In[15]:


b = np.random.randint(10, size=(3,4)) 

print(b.tolist())
print(list(b))


# In[17]:


c = np.random.randint(10, size=(2,3,4)) 

print(c.tolist())
print(list(c))


# In[39]:


##課程版1
def tolist(iterable):
    if type(iterable) != np.ndarray:
        return iterable
    newlist = []
    for obj in iterable:
        newlist.append(tolist(obj))
    return tolist (newlist)

print(tolist(a))
print(tolist(b))
print(tolist(c))


# In[38]:


def list(iterable):
    return iterable.tolist()

print('list(a) -> a.tolist:', list(a))
print('list(b) -> b.tolist:', list(b))
print('list(c) -> c.tolist:', list(c))


# In[41]:


##課程版2
def tolist(iterable):
    if type(iterable) != np.ndarray:
        return iterable
    return [tolist (obj) for obj in iterable]

print(tolist(a))
print(tolist(b))
print(tolist(c))


# 延伸題
# 題目: 1.生成一個等差數列，首數為0，尾數為20，公差為1的數列。 2.呈上題，將以上數列取出偶數。 3.呈1題，將數列取出3的倍數。
# 

# In[44]:


a = np.arange (21)

print (a)

b = a[0:21:2]

print (b)

c = a[0:21:3]

print (c)


# In[ ]:




