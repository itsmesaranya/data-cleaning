# -*- coding: utf-8 -*-
"""
Created on Sun May 08 12:39:02 2016

@author: Saranya
"""

import re
import pandas as pd

df = pd.read_csv('data_source_test.csv')

count = 0
for row_index, row in df.iterrows():
    if re.search(r"\\r\\n", str(row)):
        print type(row)
        #re.sub(r'\\r','',str(row))
        row.replace({r'\\r\\n': ''} , regex=True)        
        print row
        count += 1
        
print count
    
