#code to find and move fasta files that are similar to chosen Cas nuclease (based on ".out" files output of Hmmsearch program)
import os
import shutil
import glob
import sys

filename_txt="Similar_to_nuclease_files.txt"  
source_folder=sys.argv[1] 
source_folder=source_folder+"/"
format_files=sys.argv[2] 
destination_folder="5_Hmmsearch_result/"
files_to_move=[]
#read "Similar_to_nuclease_files.txt"  file where written all names of fasta files that contain CRISPR
with open(filename_txt) as file:
    newline_breaks=file.readlines() 
    for line in newline_breaks: 
        newline_breaks1=line.replace(".out",format_files).replace("\n","") 
        files_to_move.append(newline_breaks1)
           
# iterate files
for file in files_to_move:
    pattern = source_folder + file
    # construct full file path
    for fileq in glob.iglob(pattern, recursive=True):
    # extract file name form file path
        res_file_name = os.path.basename(fileq)
        shutil.move(fileq, destination_folder + res_file_name)
        print('Moved:', file)

#delete temporary files
 
os.remove("Similar_to_nuclease_files.txt")
print('All temporary files were removed' )    