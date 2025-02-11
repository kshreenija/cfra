# import pdfplumber
import csv
import pandas as pd
# keyword= "05 February 2025"
# with pdfplumber.open("/home/shreenija/cfra/selenium_tasks/myetf/US - Daily Fund Values 050225.pdf") as pdf:
#     # page = pdf.pages[0]  # 0-based index (page 2 is index 1)
#     # text = page.extract_text()
#     # print(text)    
#     # for page in pdf.pages:
#     #     tables = page.extract_tables()
#     #     for table in tables:
#     #         for row in table:
#     #             print(row)                                                                                                                                                                                                                                                                                                                                                                                                                        

#     for page in pdf.pages:
#         tables = page.extract_tables()
#         text = page.extract_text()
#         if keyword in text:
#             # print(f"Found '{keyword}' on page {page_num + 1}:")
#             # print(text)
#             print(keyword)
#         # Step 2: Process each table
#         data=[]
#         for table in tables:
#             # for row in table:
#             #     # Step 3: Extract and clean the data from the row
#             #     if 'NAV per Unit\n(USD)' in row:
#             #         print(row[3])
#             #     if "3 .0227" in row:
#             #         print(row[3]) 
#             #     if "Dow Jones Islamic Market US Titans 50 Index" in row:
#             #         print(row[0])
#             #     if "1 4,217.63"  in row:
#             #         print(row[0])
#              for row in table:
#                 if 'NAV per Unit\n(USD)' in row:
#                     data.append([row[3]])
#                 if "3 .0227" in row:
#                     data.append([row[3]])
#                 if "Dow Jones Islamic Market US Titans 50 Index" in row:
#                     data.append([row[0]])
#                 if "1 4,217.63" in row:
#                     data.append([row[0]])




# with pdfplumber.open("/home/shreenija/cfra/selenium_tasks/myetf/US - Daily Fund Values 050225.pdf") as pdf:
#     tables = []
#     for page in pdf.pages:
#         tables.extend(page.extract_tables())  # Extract tables from each page

# # Get the table you want (e.g., the second table)
# table_index = 1  # Adjust based on which table you need (0-based index)
# desired_table = tables[table_index]

# # Convert to DataFrame
# import pandas as pd
# df = pd.DataFrame(desired_table[1:], columns=desired_table[0])

# print(df)











import tabula as tb
import numpy as np
from tabula import read_pdf
from tabulate import tabulate

 
# #reads table from pdf file
# df = read_pdf("/home/shreenija/cfra/selenium_tasks/myetf/US - Daily Fund Values 050225.pdf",pages="all") #address of pdf file
# print(tabulate(df))
dfs=tb.read_pdf("/home/shreenija/cfra/selenium_tasks/myetf/US - Daily Fund Values 050225.pdf",pages="all")
# print(dfs[1].License[1])
# print(dfs[1].iloc[0])
print(dfs[1].to_csv("table1.csv",index=False))
# df=pd.DataFrame()
# for x in dfs:
#     df=pd.concat([df,x],ignore_index=0)
# # print(df)    
# df1=df.iloc[:,4:7]
# # print(df1)
# row_values=pd.DataFrame([df1.columns],columns=df1.columns)
# print(row_values)
# csv_file=dfs[1].to_csv("table1.csv",index=False)