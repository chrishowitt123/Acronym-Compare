import pandas as pd
import os
from IPython.core.display import display, HTML
pd.set_option('display.max_columns', None)  # or 1000
pd.set_option('display.max_rows', None)  # or 1000
pd.set_option('display.max_colwidth', None)  # or 199
display(HTML("<style>.container { width:100% !important; }</style>"))
pd.set_option('display.max_colwidth', None)
os.chdir(r'C:\Users\chris\Documents\Transgola\Clients\PROJECTS\2022\459250222_TM_HS (Fatinha)\Translation\REV TM')


acros = pd.read_excel('acroy.xlsx')
acros

or_acs = acros['orignal_acs'].tolist()
my_acs = acros['my_copy_acs'].tolist()

df = pd.read_excel('splits.xlsx', names= ["orignal", "my_copy"])

results = pd.DataFrame(columns = ["orignal", "my_copy"])

for x,y in zip(or_acs, my_acs):

    results = results.append(df[(df['orignal'].str.contains(fr'[^a-zA-Z]{x}[^a-zA-Z]', na=False)) &  ~(df['my_copy'].str.contains(fr'[^a-zA-Z]{y}[^a-zA-Z]', na=False))])
    
results.to_excel('results.xlsx', index = False)

results
