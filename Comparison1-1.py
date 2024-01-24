# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 11:51:23 2022

@author: ZoeStarkey
"""

import pandas as pd
import datacompy

lmi_original_df1 = pd.read_excel("C:/Users/ZoeStarkey/Downloads/Medical_Files_01_11_2023_R5V1/Individual_Market_Medical_01_11_2023_R5V1.xlsx", dtype = object, skiprows = 1)
lmi_new_df2 = pd.read_excel("C:/Users/ZoeStarkey/Downloads/Medical_Files_01_11_2023_R5V3/Individual_Market_Medical_01_11_2023_R5V3.xlsx", dtype = object, skiprows = 1)

# lmi_original_df1['emergency room - 73 percent'].replace('$', '', inplace=True, regex=True)
# LBCS['EHBVarReason'].replace('\/', ' ', inplace=True, regex=True)
#Runs comparison
compare = datacompy.Compare(
        lmi_original_df1, #Pass in dataframe, MIDAS
        lmi_new_df2, #Pass in dataframe, LMI
        join_columns=['Plan ID (Standard Component)', 'FIPS County Code', 'Metal Level'],
        abs_tol=0, #optional, defaults to 0
        rel_tol=0, #optional, defaults to 0
        ignore_case = True,
        ignore_spaces = True,
        cast_column_names_lower = True,
        df1_name='lmi_original_df1', #optional, defaults to 'df1'
        df2_name='lmi_new_df2') #optional, defaults to 'df2'
compare.matches()

# Creates report and prints to Console
ComRepPA = compare.report(sample_count=0)
print(ComRepPA)


# Compares all variables to identify mismatches for printing
# dependentmaximumagerule = compare.sample_mismatch('dependentmaximumagrule', sample_count=1000000, for_display=False)
# emergroomstandard = compare.sample_mismatch('emergency room - standard', sample_count=1000000, for_display=False)
# emergroom73 = compare.sample_mismatch('emergency room - 73 percent', sample_count=1000000, for_display=False)
# emergroom87 = compare.sample_mismatch('emergency room - 87 percent', sample_count=1000000, for_display=False)
# emergroom94 = compare.sample_mismatch('emergency room - 94 percent', sample_count=1000000, for_display=False)
# genericdrugsstandard = compare.sample_mismatch('generic drugs - standard', sample_count=1000000, for_display=False)
# genericdrugs73 = compare.sample_mismatch('generic drugs - 73 percent', sample_count=1000000, for_display=False)
# genericdrugs87 = compare.sample_mismatch('generic drugs - 87 percent', sample_count=1000000, for_display=False)
# genericdrugs94 = compare.sample_mismatch('generic drugs - 94 percent', sample_count=1000000, for_display=False)
# perprefbranddrugsstandard = compare.sample_mismatch('preferred brand drugs - standard', sample_count=1000000, for_display=False)
# perprefbranddrugs73 = compare.sample_mismatch('preferred brand drugs - 73 percent', sample_count=1000000, for_display=False)
# perprefbranddrugs87 = compare.sample_mismatch('preferred brand drugs - 87 percent', sample_count=1000000, for_display=False)
# perprefbranddrugs94 = compare.sample_mismatch('preferred brand drugs - 94 percent', sample_count=1000000, for_display=False)
# drugformurl = compare.sample_mismatch('drug formulary url', sample_count=1000000, for_display=False)
# tehbinntier1familyperpersonmoop = compare.sample_mismatch('tehbinntier1familyperpersonmoop', sample_count=1000000, for_display=False)

# Generates CSV files of all variables, SHOULD REVISE TO ONLY CREATE FOR VARIABLES WITH MISMATCHES
# planbrochure.to_csv(r'C:\Users\ZoeStarkey\OneDrive - Duty First Consulting\PM\Data Team\PUF\PY23\January PY23\Results\planbrochure.csv', index = None, header = True)

BCSRow1 = compare.df1_unq_rows
BCSRow2 = compare.df2_unq_rows

# # Generates CSV of extra rows in MIDAS and LMI files
# ExtraBCSrow1 = BCSRow1.to_csv(r'C:\Users\ZoeStarkey\OneDrive - Duty First Consulting\PM\Data Team\PUF\PY23\November 2.0 PY23\Results\PlanAttributes\LMI_original_extraBCSRow.csv', index = None, header = True)
# ExtraBCSrow2 = BCSRow2.to_csv(r'C:\Users\ZoeStarkey\OneDrive - Duty First Consulting\PM\Data Team\PUF\PY23\January PY23\Results\PlanAttributes\LMI_new_extraBCSRow.csv', index = None, header = True)
