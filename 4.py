
"""
Created on Mon Nov 29 14:29:26 2021

@author: lenovo
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

import os
idx = pd.IndexSlice

plotconfig = {
    'style':'.',
    'ylim':(0,2000),
    'xlim':('2018-01-01','2021-01-01'),
    'grid':True,
    'markersize':5,
    'figsize':(20,6)
}

detections = pd.read_csv(r'C:\Users\lenovo\Documents\skola\python\csv\nika.csv',index_col=['location','direction','ts'],parse_dates=True).value.sort_index()
detdata = pd.DataFrame(detections)
print(detdata.iloc[0])
print(detdata.index)
print(detdata.unstack(['location','direction']).columns)
print(detdata.stack)
print(detdata.mean())
detcols = detdata.unstack(['location','direction']).median()
print(detcols.head())
def get_max_counter(row):
    recordman = row.idxmax()
    return pd.Series({'location':recordman[0],'direction':recordman[1],'value':row.max()})
print(detcols.apply(get_max_counter))