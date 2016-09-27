# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 11:20:10 2016

@author: maquiles
"""
import os
import pandas as pd

path = os.path.dirname(os.path.abspath(__file__))
files = os.listdir(path)
files_xls = [f for f in files if f[-4:] == 'xlsx']

all_data = pd.DataFrame()
for f in files_xls:
    data = pd.read_excel(f, 'Sheet1')
    all_data = all_data.append(data)
    
all_data.to_excel("all.xls")