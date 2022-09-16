import pandas as pd
import os
from IPython.core.display import display, HTML
pd.set_option('display.max_columns', None)  # or 1000
pd.set_option('display.max_rows', None)  # or 1000
pd.set_option('display.max_colwidth', None)  # or 199
display(HTML("<style>.container { width:100% !important; }</style>"))
pd.set_option('display.max_colwidth', None)
os.chdir(r'C:\Users\chris\Documents\Transgola\Clients\PROJECTS\2022\459250222_TM_HS (Fatinha)\Translation\REV TM')

"""
A program that compares acronyms between source and target documents

"""

# read acronyms
acros = pd.read_excel('acroy.xlsx')

# define source acronyms
sc_acs = acros['source_acs'].tolist()

# define target acronyms
tar_acs = acros['target_acs'].tolist()

# read source and target text
df = pd.read_excel('splits.xlsx', names= ["source", "target"])

# define DataFrame to hold results
results = pd.DataFrame(columns = ["source", "target"])

# iterate over source and target acronyms 
for x,y in zip(sc_acs, tar_acs):
    # filter source and target columns for source and target acronyms
    results = results.append(df[(df['source'].str.contains(fr'[^a-zA-Z]{x}[^a-zA-Z]', na=False)) &  ~(df['target'].str.contains(fr'[^a-zA-Z]{y}[^a-zA-Z]', na=False))])

# drop nulls    
results.dropna(inplace = True)  

# write results to Excel
results.to_excel('results1.xlsx', index = False)
