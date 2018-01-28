
# coding: utf-8

# ### Problem Statement
# 
# Create the below pattern using nested for loop in Python.
# 

# In[23]:


n=5
for x in [1,n-1]:
    for y in range (0,n):
        if x !=n-1 :
            print ("*"*(x+y))
        else:
            print(("*"*(x-y)))
    
    

