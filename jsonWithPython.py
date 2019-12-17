
# coding: utf-8

# In[35]:


import json
with open('E:\Spell and Grammar Checker\MS Word Add-in\csvtconvertson/miniDictionary.json', encoding="utf8") as f:
  data = json.load(f)
# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
for i in range (len(data)):
    print(data[i]['words'])

