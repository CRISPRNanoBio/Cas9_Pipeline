
import shutil
import glob,os
import warnings
import Bio
from Bio import SeqIO
from Bio.Seq import Seq
from Bio import BiopythonWarning

foldername=str(input("Type the folder name where fasta files are located (from 3 step): "))
foldername=foldername+'/'
length_folder_name=len(foldername)
min_pro_len=int(input("Specify the minimum protein length (min_pro_len): "))
format_file=str(input('Type  the format of the fasta file (.fa , .fasta, .fna etc) Type with the dot: '))
len_format_file=-len(format_file)
format_file_1='*'+format_file
directory="4_step_Biopython_result/"
path = os.path.join(os.getcwd(), directory) #create path for folder in current directory
os.mkdir(path)
files_to_move=[]
ready=[]

#in order to prevent BiopythonWarning: Partial codon, len(sequence) not a multiple of three.
def pad_seq(sequence):
            remainder = len(sequence) % 3
            return sequence if remainder == 0 else sequence + Seq('N' * (3 - remainder))

        
def find_orfs_with_trans(seq, trans_table, min_protein_length):
            answer = []
            seq_len = len(seq)
            for strand, nuc in [(+1, seq), (-1, seq.reverse_complement())]:
                for frame in range(3):
                    trans = nuc[frame:].translate(trans_table)
                    trans_len = len(trans)
                    aa_start = 0
                    aa_end = 0
                    while aa_start < trans_len:
                        aa_end = trans.find("*", aa_start)
                        if aa_end == -1:
                            aa_end = trans_len
                        if aa_end - aa_start >= min_protein_length:
                            if strand == 1:
                                start = frame + aa_start * 3
                                end = min(seq_len, frame + aa_end * 3 + 3)
                            else:
                                start = seq_len - frame - aa_end * 3 - 3
                                end = seq_len - frame - aa_start * 3
                            answer.append((start, end, strand, trans[aa_start:aa_end]))
                        aa_start = aa_end + 1
            answer.sort()
            return answer

# ignore biopython warnings
warnings.simplefilter('ignore', BiopythonWarning)

fasta_paths = glob.glob(os.path.join(foldername, format_file_1))
for file in fasta_paths:
        record = pad_seq(SeqIO.read(file, "fasta"))
        table = 11
        name=str(file)[:len_format_file]
        orf_list = find_orfs_with_trans(record.seq, table, min_pro_len)
        for start, end, strand, pro in orf_list:
            result="%s - length %i, strand %i, %i:%i"\
            % (pro[:], len(pro), strand, start, end)   #Here is the place to modify which characteristics about ORF will be written
            result=str(result)
            ready.append (name+'\n'+result)
                        
        for element in ready:
            name_correction=element.find('\n')
            new_name=element[length_folder_name:name_correction]
            add=element.find('- length')
            new_name=new_name+element[add:]+'.fa' #add to the filename information about ORF length, strand, coordinates
            with open(new_name, 'w') as f: 
                f.write('>'+element[length_folder_name:add])    #write to the file ORF starting with sign '>'
            files_to_move.append(new_name)
# iterate files        
for ready_file in files_to_move:
    pattern = ready_file
    # construct full file path
    for fileq in glob.iglob(pattern, recursive=True):
         # extract file name form file path
        res_file_name = os.path.basename(fileq)
        shutil.move(fileq, directory + res_file_name)       
print("All created files with ORF are moved to the folder '4_step_Biopython_result'. This step is completed! Go to the next step!")                       