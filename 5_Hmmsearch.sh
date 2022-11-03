#!/bin/bash

read -p 'Type the folder name that contain profile of Cas nuclease : ' nuclease_folder
read -p 'Type the full filename (with extension) of profile of Cas nuclease : ' nuclease_name
echo Now Hmmbuild program will work. It can take a lot of time. Do not shut down the code!

hmmbuild $nuclease_name.hmm $nuclease_folder/$nuclease_name > metadata_hmmbuild.out 
echo Hmmbuild program successfully created the file with extension ".hmm" that will be used in Hmmsearch program - following step

read -p 'Type the folder name that contain your fasta file (with ORF) after step 4: ' foldername_file
read -p 'Type the format of your fasta file (with the dot, for example .fna or .fa or .fasta) : ' format 

for f in $foldername_file/*$format ; do hmmsearch $nuclease_name.hmm  "$f" > "${f%.*}.out" ; done 
 
echo Hmmsearch Step successfully done! program created ".out" files.In the same directory with fasta files 
echo Now files that are similar to chosen Cas profile will be filtered and saved in specified folder!

#read -p 'Type the destination folder name (must already exist) where this fasta files will be located: ' 
mkdir foldername_Cas-nuclease_file_save
find $foldername_file/ -type f -exec grep -qiF 'Alignments for each domain' {} \; -exec mv {} foldername_Cas-nuclease_file_save/ \;
if    ls -A1q foldername_Cas-nuclease_file_save/ | grep -q .
then  ls foldername_Cas-nuclease_file_save/ > Similar_to_nuclease_files.txt | python3 move_fasta_files_similar_to_Cas_nuclease.py "$foldername_file" "$format" 
else  echo No files were similar to Cas nuclease
fi



