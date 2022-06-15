#!/usr/bin/env python
# coding: utf-8

# # Max-Net

# In[1]:


import numpy as np
import copy


# ### Needed Functions

# In[2]:


def relu(x):
    if x >= 0:
        return x
    else:
        return 0
    
def finished(v):
    count = 0
    for i in range(len(v)):
        if v[i] == 0:
            count += 1
    if count >= len(v)-1:
        return True
    else:
        return False


# ### Inputs

# In[3]:


input_array = np.array([1.2, 1.1, 1, 0.9, 0.95, 1.15])
epsilon = 0.15


# ### Training Max-Net

# In[4]:


w = np.eye(len(input_array))*(1+epsilon) - epsilon
my_list = []
answer = []
temp_input = copy.deepcopy(input_array)

while not finished(temp_input):
    print(temp_input)
    temp_input = np.matmul(w, temp_input.T)
    for i in range(len(temp_input)):
        temp_input[i] = relu(temp_input[i])
        if temp_input[i] == 0 and i not in my_list:
            my_list.append(i)            
print(temp_input)

for i in range(len(temp_input)):
    if temp_input[i] != 0 :
        my_list.append(i)

my_list = my_list[::-1]
answer = np.array(my_list)


# ### Max-Net output

# In[5]:


print('Descending max index:', answer)
print('\nSorted Descending:')
for i in range(len(input_array)):
    print(input_array[answer[i]])


# In[6]:


ascending_answer = answer[::-1]
print('Ascending max index:', ascending_answer)
print('\nSorted Ascending:')
for i in range(len(input_array)):
    print(input_array[ascending_answer[i]])


# In[ ]:





# In[ ]:




