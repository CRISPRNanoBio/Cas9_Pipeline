import pandas as pd
import glob, os
from glob import glob
import sys
foldername_txt=sys.argv[1]
foldername=foldername_txt+'/'
os.chdir(foldername) #change the path 
colspecs = [(0, 14), (14, 30), (30, 50), (50, 64), (64, 73), (73, 80), (80, 86), (86, -1)] #width of the columns
files=glob('*.txt') #read only txt files containing info about profiles and sequences
data = pd.concat((pd.read_fwf(file, skiprows=1, skipfooter=10,colspecs = colspecs) for file in files), ignore_index=True)
specific_columns = data[['# target name', 'query name', 'E-value',  'score',  'bias']] #show only specific columns
sorted_df=specific_columns.sort_values(by='# target name') #sort by name 
modified_df=sorted_df.drop(sorted_df[sorted_df.score.str.contains(r'[-]') |  #drop empty rows that have '-' sign
                 sorted_df.bias.str.contains(r'[-]')].index)
modified_df=modified_df.reset_index(drop=True) #drop index (= 1st column)         
print(modified_df)       #show the dataframe to the user
modified_df.to_csv('subtype_determination.csv',index=False) #save the dataframe to .csv file
print(''' RESULT: If you see II profiles and in previous step you searched against Cas9 profile 
then everything is fine ! and you can go to the next step!

 If you see V_ profiles and in previous step you searched against Cas12 profile 
 then everything is fine ! and you can go to the next step!

 In other cases open file subtype_determination.csv and check your data carefully!''')

#remove files from hmmsearch
test = os.listdir()
for item in test:
    if item.endswith(".hmm.txt") or item.endswith (".txt.out"):
        os.remove(item) 
print('All temporary files were removed' )

