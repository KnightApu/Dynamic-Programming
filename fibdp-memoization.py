
# coding: utf-8

# In[33]:


nil = -1
lookup = [];

def init():
    for i in range(10):
        lookup.append(nil)
        
init()

def fib(n):
    if(lookup[n] == nil):
        if n<= 1 : 
            lookup[n]=n;
        else:
            lookup[n] = fib(n-1)+fib(n-2)
            
    return lookup[n]

for i in range(10):
    print(fib(i))


