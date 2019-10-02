# -*- coding: utf-8 -*-
"""
Bitmex TAQ file Combiner
created by Randall Campbell 
Bitmex .gzip files can be found at 
https://public.bitmex.com
"""

import os
import pandas as pd 
import gzip 


##Path of the directory or folder where Bitmex .gzips are saved
directory = 'N://Bitmex'  


bitmex_complete = []
for filename in os.listdir(directory):
    if filename.endswith('.gz'):
        bitmexRaw = gzip.GzipFile(directory +'/'+filename,'rb')
        bitmexDF =pd.read_csv(bitmexRaw)
        ## Change groupby to timestamp,side,size,symbol,price,tickDirection
        ## trdMacthID,grossValue,homeNotional,foreignNotional
        ## Filter and sort as you wish. 
        bitmexGrouped = bitmexDF.groupby('symbol').get_group('XBTUSD') 
        bitmex_complete.append(bitmexGrouped)
        bitmex_TradeRecord = pd.concat(bitmex_complete) 
        bitmex_TradeRecord.to_csv('N://Bitmex/TradeRecord.csv') 
 