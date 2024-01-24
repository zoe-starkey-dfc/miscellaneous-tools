# Miscellaneous Tools

Contains a collection of tools/functions that can be used to make a variety of manual tasks easier or can be incorporated into larger codes to avoid recreating the same syntax. You will at minimum have to update
file paths and variable names to use these tools.
## The below tools are complete and functional:
1. csv_row_splitter - splits large .csv files into smaller files. Main purpose is to split .csv files that are too big to be opened in Excel into an openable size.
2. state_row_splitter - this tool splits data provided by state and outputs a separate, formatted file for each state. Intended to create outreach files for targeted data transfer. Code can be easily modified to 
                     split based on parent organization or issuer as well. 
3. SplitColumnDateDelimiterExcel - splits chunks of data in an excel box based on a given delimiter (for example, a long list of plan ids stored in a single cell).
4. Comparison1-1 - compares two files against each other to find differences. Main purpose is to be copied into a larger code that incorporates any necessary data cleaning. Uses the datacompy package.

## The below tools are still in development and should be used with caution:

