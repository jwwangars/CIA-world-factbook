# Test if CIA world factbook has a colored glass
# gather data, fit one model, and test residuals
# 
# Step 1: gather data
#
# only save useful stems for words

import requests
import bs4
import nltk
import numpy as np
import pandas as pd

excludes = ['oth','away','from','bord','hav','been','also',\
            'becaus','with','econom','most','year','which','peso',\
            'than','real','that','century',\
            'about','into','through','between','among',\
            'their','and','the','for','but','upon','whil',\
            'janu','febr','april','may','jun','jul','august','septemb','octub','novemb','decemb']


r = requests.get('https://www.cia.gov/the-world-factbook/field/economic-overview')
r.encoding = 'utf-8'
soup = bs4.BeautifulSoup(r.text,"html.parser")
ttag =  soup.find('h3',text='Afghanistan').parent # whole paragraph
entity = []
text1 = []
text_stemmer = list()
while(True):
    entity.append(ttag.h3.text) # name
    temp = ttag.p.text.lower() # content
    
    temp = temp.replace('.', ' ') # ignore punctuation
    temp = temp.replace('-', ' ')
    temp = temp.replace(';', ' ')
    temp = temp.replace(',', ' ')
    
    text1.append(temp)
    
    all_text = nltk.word_tokenize(temp) # split
    temp3 = []
    for word in all_text:
        temp2 = nltk.LancasterStemmer().stem(word) # transfer to stems
        if not (len(temp2)<3 or temp2 in excludes or temp2.isnumeric()): # ignore simple ones
            temp3.append(temp2)
    text_stemmer.append(temp3)
    
    
    ttag = ttag.next_sibling
    if (ttag == None):
        break




#with open('cia.csv', 'wt') as f:
#    f.write(freq.to_csv())
