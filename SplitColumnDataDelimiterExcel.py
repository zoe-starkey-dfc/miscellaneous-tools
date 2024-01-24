# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 02:33:58 2022

@author: ZoeStarkey
"""

import pandas as pd

PlanIDs = pd.read_csv(r'C:\Users\ZoeStarkey\OneDrive - Duty First Consulting\PDEPlanIds.csv')

unique_planids = [val.strip() for sublist in PlanIDs.PlanIds.dropna().str.split(",").tolist() for val in sublist]

unique_planids = pd.DataFrame(unique_planids, columns=['PlanIds'])

uniqueids = unique_planids.to_csv(r'C:\Users\ZoeStarkey\OneDrive - Duty First Consulting\PDEPlanIdsIsolated.csv', index=None, header=True)
