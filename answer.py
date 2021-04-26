#!/usr/bin/env python
# coding: utf-8

# In[27]:


import allennlp
from allennlp_models import pretrained
from allennlp.predictors.predictor import Predictor
import wikipedia
import sys

filename = "set4/a2.txt"
file = open(filename, "r")
passage = file.read()


query = "Is ash the protagonist?"
predictor = pretrained.load_predictor('rc-bidaf')
answer = predictor.predict(query, passage)
print(answer['best_span_str'])


# In[ ]:





# In[ ]:




