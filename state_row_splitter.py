# -*- coding: utf-8 -*-
"""
Created on Mon Jan 23 15:35:16 2023

@author: ZoeStarkey
"""

#Import packages
import pandas as pd

#Set file path - update to current file
big_file = r"C:/Users/ZoeStarkey/OneDrive - Duty First Consulting/Python Data Mod/cleanedUpApps11-17.xlsx"

#Name of column with categories
state_column_name = 'State' #this is the original column name for the state - update as needed (if this value changes you will need to update some of the variables below)
app_column_name = 'appID' #this is the original column name for the application ID - update as needed
date = '_11.30.2023' #update to two days after the request is receied from CCIIO

#read big_file into pandas
data = pd.read_excel(big_file)

#Reorder column names
data = data[[state_column_name, app_column_name]]
data.rename(columns={app_column_name: 'Application ID'}, inplace = True)

#Split big_file into smaller files by state - files will output wherever this python file is saved
data_category_range = data[state_column_name].unique()
data_category_range = data_category_range.tolist()
for i,state in enumerate(data_category_range):
    data[data[state_column_name] == state].to_excel(r'App ID Request_'+str(state)+str(date)+r'.xlsx',index = False, na_rep = 'N/A', sheet_name = r'App ID Request - '+str(state))

#Set column widths for Application ID to 15 characters        
for state in data_category_range:
    df = pd.read_excel(r'App ID Request_'+str(state)+str(date)+r'.xlsx')
    writer = pd.ExcelWriter(r'App ID Request_'+str(state)+str(date)+r'.xlsx', engine = 'xlsxwriter')
    df.to_excel(writer, sheet_name=r'App ID Request - '+str(state), index = False, startrow=1, header=False)
    col_idx = df.columns.get_loc('Application ID')

    #Sets parameters for header (alignment, text wrapping, color, etc)
    workbook = writer.book
    worksheet = writer.sheets[r'App ID Request - '+str(state)]
    header_format = workbook.add_format({
        'bold': True, 
        'text_wrap': True, 
        'valign': 'top', 
        'fg_color': '#FF00FF',
        'border': 1})
    
    #Sets formatting for the sheet header
    for col_num, value in enumerate(df.columns.values):
        worksheet.write(0, col_num, value, header_format)
        
    worksheet.set_column(col_idx, col_idx, 15)

    writer.close()
    
# #Chunksize indicates the number of rows per file
# for i, size in enumerate(pd.read_csv(big_file, chunksize = 1000000, dtype = object)):
#     size.to_csv(r'C:/Users/ZoeStarkey/OneDrive - Duty First Consulting/PM/Data Team/PUF/PY24/October PY24/LMI PUF/rate_split{}.csv'.format(i), index = False)
    

