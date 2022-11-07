#!/bin/bash

read -p 'Type the folder name that contain your fasta file: ' foldername_file
read -p 'Type the format of your fasta file (with the dot, for example .fna or .fa or .fasta) : ' format

echo Now CRT program will work. It can take a lot of time. Do not shut down the code!

for f in $foldername_file/*$format ; do java -cp CRT1.2-CLI.jar crt -minNR 2  "$f" "${f%.*}.out" ;done > metadata.out 

echo Step successfully done! CRT program created ".out" files.In the same directory with fasta files 
echo Now files that have CRISPR will be filtered and saved in folder "2_CRT_result"!
echo Filtration in progress! It can take a lot of time. Do not shut down the code!

mkdir 2_CRT_result
find $foldername_file/ -type f -exec grep -qiF 'REPEAT' {} \; -exec mv {} 2_CRT_result/ \;
ls 2_CRT_result/ > CRISPR_found_in_this_files.txt

python3 move_fasta_files_that_has_crispr_light.py "$foldername_file" "$format" 

