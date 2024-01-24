# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 15:35:16 2023

@author: ZoeStarkey
"""

import pandas as pd

#Set file path
big_file = r"C:/Users/ZoeStarkey/OneDrive - Duty First Consulting/PM/Data Team/PUF/PY23/January PY23/LMI PUF/Rate_PUF.csv"

#chunksize indicates the number of rows per file
for i, size in enumerate(pd.read_csv(big_file, chunksize = 1000000, dtype = object)):
    size.to_csv(r'C:/Users/ZoeStarkey/OneDrive - Duty First Consulting/PM/Data Team/PUF/PY23/January PY23/LMI PUF/rate_split{}.csv'.format(i), index = False)
    