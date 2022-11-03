# Step-by-step pipline explanation

## Step 1. (Optional) Divide multifasta file to many single ".fasta" files
If you have multifasta files that you are going to work with - then you must start with this step - divide multifasta files to many single '.fasta' files.
[Here is the link to file](1_divide_multifasta_files.sh) To run ".sh" file type in terminal: `bash nameofthefile.sh`

## Step 2. Detection of CRISPR elements in fasta files
In this step you can use any suitable program such as CRISPRCasFinder, PILER-CR, CRISPRDetect,  CRISPRidentify. [In this file](2_CRT-detection_crispr.sh) we are using CRT program - CRISPR Recognition Tool.

Before launching the [file](2_CRT-detection_crispr.sh):

You need to download the CRT program  http://www.room220.com/crt/CRT1.2-CLI.jar.zip , then unzip file.<br/>Note that [file](2_CRT-detection_crispr.sh) will work only if java file of the CRT program is in the same folder.<br/>Note that we specified the option `-minNR 2` which is responsible for minimum number of repeats is 2.<br/>You also can add option `-Xmx4096m` if you do not have enough cores/memory on your computer.<br/>After running CRT program file will launch [next python file](move_fasta_files_that_has_crispr_light.py) that will find and save in specified folder only fasta files that contain CRISPR elements.

## Step 3. Cut specific location of CRISPR-element from the fasta file
Sometimes fasta file can be too long. We do not want to proceed the whole file. Instead we will save only that nucleotide location where CRISPR was found.<br/>You will need to specify the number of nucleotides that should be saved from the left and right side of the CRISPR-element. In case of searching for Cas 9 nuclease we recommend to put 30 000.<br/>Launch [this python file](3_cut_crispr_region.py) by typing in terminal `python3 3_cut_crispr_region.py` 

## Step 4.Identifying open reading frames
[The python file](4_Identify_ORF_biopython.py) requires from user to specify `min_pro_len` parameter (minimum protein length). In case of Cas9 nuclease we recommend to put number in range  800 - 900.
[Run this python file](4_Identify_ORF_biopython.py) on fasta files that passed step 3!

## Step 5. Find fasta files that look similar to chosen Cas nuclease 
This step will be performed with usage of HMMsearch and HMMbuild programs. So, before launching the files, please download hmmsearch in your terminal. Detailed information about HMMER program can be found [here](http://eddylab.org/software/hmmer/Userguide.pdf). 
To run step 5 launch [this bash file](5_Hmmsearch.sh) that will launch [following python file](move_fasta_files_similar_to_Cas_nuclease.py).

## Step 6. Classification of Cas nuclease subtype.
For this step you will need to have profiles of Cas nuclease subtypes. [Run this bash file](6_Identification_subtypes_nuclease.sh) that will launch [python file](6_Identification_subtypes_nuclease.py)
