 # -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 17:20:04 2019

@author: JLI
"""

'''
# summaize all .bib files
import os
path = os.getcwd()
one = open('1.bib', 'w+', encoding='utf-8')
for item in os.listdir(path):
    portion = os.path.splitext(item)
    if len(portion[0]) > 12 and portion[1] == '.bib':
        file = open(os.path.join(path,item), encoding='utf-8').read()
        one.write(file)
one.close()
'''      

import bibtexparser
import pandas as pd
file = open('1.bib',encoding='utf-8')
n = file.read().count('issn')
print(n)
df = pd.DataFrame(columns=['issn', 'doi', 'abstract', 'pages', 'url', 'volume', 'year', 'journal', 'title', 'author'])
with open('1.bib',encoding='utf-8') as bib_file:
    bib_database = bibtexparser.load(bib_file)

for i in range(0,n):
    try:
        df.loc[i,'issn'] = bib_database.entries[i]['issn'].replace('{','').replace('}','')
    except:
        df.loc[i,'issn'] ='Null'
    try:
        df.loc[i,'doi'] = bib_database.entries[i]['doi'].replace('{','').replace('}','')
    except:
        df.loc[i,'doi'] ='Null'
    try:
        df.loc[i,'abstract'] = bib_database.entries[i]['abstract'].replace('{','').replace('}','')
    except:
        df.loc[i,'abstract'] ='Null'
    try:
        df.loc[i,'pages'] = bib_database.entries[i]['pages'].replace('{','').replace('}','')
    except:
        df.loc[i,'pages'] = 'Null'
    try:
        df.loc[i,'url'] = bib_database.entries[i]['url'].replace('{','').replace('}','')
    except:
        df.loc[i,'url'] = 'Null'
    try:
        df.loc[i,'volume'] = bib_database.entries[i]['volume'].replace('{','').replace('}','')
    except:
        df.loc[i,'volume'] = 'Null'
    try:
        df.loc[i,'year'] = bib_database.entries[i]['year'].replace('{','').replace('}','')
    except:
        df.loc[i,'year'] = 'Null'
    try:
        df.loc[i,'journal'] = bib_database.entries[i]['journal'].replace('{','').replace('}','')
    except:
        df.loc[i,'journal'] = 'Null'
    try:
        df.loc[i,'title'] = bib_database.entries[i]['title'].replace('\n',' ').replace('{','').replace('}','')
    except:
        df.loc[i,'title'] = 'Null'
    try:
        df.loc[i,'author'] = bib_database.entries[i]['author'].replace('{','').replace('}','')
    except:
        df.loc[i,'author'] = 'Null'
df.to_csv('1.csv')

'''
file = open('2.bib',encoding='utf-8')
n = file.read().count('Unique-ID')
print(n)
df = pd.DataFrame(columns=['issn', 'doi', 'abstract', 'pages', 'url', 'volume', 'year', 'journal', 'title', 'author'])
with open('2.bib',encoding='utf-8') as bib_file:
    bib_database = bibtexparser.load(bib_file)

for i in range(0,n):
    try:
        df.loc[i,'issn'] = bib_database.entries[i]['issn'].replace('{','').replace('}','')
    except:
        df.loc[i,'issn'] ='Null'
    try:
        df.loc[i,'doi'] = bib_database.entries[i]['doi'].replace('{','').replace('}','')
    except:
        df.loc[i,'doi'] ='Null'
    try:
        df.loc[i,'abstract'] = bib_database.entries[i]['abstract'].replace('{','').replace('}','')
    except:
        df.loc[i,'abstract'] ='Null'
    try:
        df.loc[i,'pages'] = bib_database.entries[i]['pages'].replace('{','').replace('}','')
    except:
        df.loc[i,'pages'] = 'Null'
    try:
        df.loc[i,'url'] = bib_database.entries[i]['url'].replace('{','').replace('}','')
    except:
        df.loc[i,'url'] = 'Null'
    try:
        df.loc[i,'volume'] = bib_database.entries[i]['volume'].replace('{','').replace('}','')
    except:
        df.loc[i,'volume'] = 'Null'
    try:
        df.loc[i,'year'] = bib_database.entries[i]['year'].replace('{','').replace('}','')
    except:
        df.loc[i,'year'] = 'Null'
    try:
        df.loc[i,'journal'] = bib_database.entries[i]['journal'].replace('{','').replace('}','')
    except:
        df.loc[i,'journal'] = 'Null'
    try:
        df.loc[i,'title'] = bib_database.entries[i]['title'].replace('\n',' ').replace('{','').replace('}','')
    except:
        df.loc[i,'title'] = 'Null'
    try:
        df.loc[i,'author'] = bib_database.entries[i]['author'].replace('{','').replace('}','')
    except:
        df.loc[i,'author'] = 'Null'
df.to_csv('2.csv')

df0 = pd.read_csv('2.csv')
df1 = pd.read_csv('1.csv')
df2 = df0[~df0['ID'].isin(df1['ID'])]
df2.to_csv('left.csv')'''