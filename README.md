# Step-by-step pipline explanation

## Step 1. (Optional) Divide multifasta file to many single ".fasta" files
If you have multifasta files that you are going to work with - then you must start with this step - divide multifasta files to many single '.fasta' files.
[Here is the link to file](1_divide_multifasta_files.sh) To run ".sh" file type in terminal: `bash nameofthefile.sh`

## Step 2. Detection of CRISPR elements in fasta files
In this step you can use any suitable program such as CRISPRCasFinder, PILER-CR, CRISPRDetect,  CRISPRidentify. [In this file] (2_CRT-detection_crispr.sh) we are using CRT program - CRISPR Recognition Tool.

Before launching the file:

You need to download the CRT program  http://www.room220.com/crt/CRT1.2-CLI.jar.zip , then unzip file.
Note that [file] (2_CRT-detection_crispr.sh) will work only if java file of the CRT program is in the same folder.
Note that we specified the option `-minNR 2` which is responsible for minimum number of repeats is 2.
You also can add option `-Xmx4096m` if you do not have enough cores/memory on your computer. 
After running CRT program file will launch [next python file] (move_fasta_files_that_has_crispr_light.py) that will find and save in specified folder only fasta files that contain CRISPR elements.
