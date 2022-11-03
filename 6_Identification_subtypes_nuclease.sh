#!/bin/bash

read -p 'Type the format of fasta files (with the dot) in the folder "5_Hmmsearch_result" : ' format_fa
cat 5_Hmmsearch_result/*$format_fa > Multifasta.fa


read -p 'Type the folder name with other Cas nuclease profiles:' foldername_hmm
read -p 'Type the format of Cas nuclease profiles (with the dot, for example .fna or .fa or .fasta) : ' format_hmm

echo Now Hmmbuild program will work. It can take a lot of time. Do not shut down the code!
for f in $foldername_hmm/*$format_hmm*; do  hmmbuild "${f%.*}.hmm" "$f"  ; done > hmmbuild_metadata.txt.out
echo Hmmbuild program successfully created the file with extension ".hmm" that will be used in Hmmsearch program - following step

for g in $foldername_hmm/*.hmm ; do  hmmsearch  --tblout  "${g}.txt" "$g"  Multifasta.fa ; done > metadata.txt.out
echo Hmmsearch Step successfully done! program created ".txt" files.

python3 6_Identification_subtypes_nuclease.py "$foldername_hmm"