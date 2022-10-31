# If you have multifasta files that you are going to work with 
#Then you must start with this step - divide multifasta files to many single '.fasta' files

#!/bin/bash

read -p 'Type the folder name that contain your multifasta file: ' foldername_file
read -p 'Type the format of the multifasta file. Type with the dot, for example .fna or .fa or .fasta : ' format


for f in $foldername_file/*$format ; do awk -v var="$format" '{if(substr($0, 1, 1)==">"){filename=(substr($0,2)var)} print $0 > filename}' "$f" ; done

echo Step successfully done! Go to the next step!

