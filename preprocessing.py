# Step 2: data cleaning and preprocessing
# establish a dictionary to convert into real numbers

import numpy as np
import pandas as pd

dict_ts = dict()
word_index = 1
count_word = np.ones(10000)
wordlist = ['']
for rows in text_stemmer:
    for word in rows:
        if dict_ts.get(word,'0') == '0':
            dict_ts[word] = word_index
            word_index = word_index + 1
            wordlist.append(word)
        else:
            count_word[dict_ts.get(word,'0')] += 1
            
effective_count = sum(count_word > 1) #2265

for i in range(effective_count):
    if count_word[i] == 1:
        dict_ts[wordlist[i+1]] = 0
        
text_ts_input = np.zeros([len(text_stemmer),500])

count1 = 0
for rows in text_stemmer:
    count2 = 0
    for word in rows:
        text_ts_input[count1][count2] = dict_ts.get(word,0)
        count2 += 1
        if count2 > 499:
            break
    count1 += 1

gdp = pd.read_csv('gdpgr.csv') # responses from world bank lastest statistics
gdp.index = gdp.iloc[::,0]
response = np.zeros(len(entity))
error_count = np.zeros(len(entity))
for i in range(len(entity)):
    try:
        response[i] = gdp.loc[entity[i]][64]
    except:
        error_count[i] = 1
    if np.isnan(response[i]):
        error_count[i] = 2
        response[i] = 0
    
    
