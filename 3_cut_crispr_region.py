import glob, os
foldername=str(input("Type the folder name where fasta and '.out' files are located (from 2 step): "))
foldername=foldername+'/'
length_ORF=int(input("Type the length of ORF that will be cutted from right and left sides of CRISPR-element:")) 
format_file=str(input('Type  the format of the fasta file (.fa , .fasta, .fna etc) Type with the dot: '))
len_format_file=-len(format_file)
format_file_1='*'+format_file 
os.chdir(foldername)
#for each fasta file open .out file
for file in glob.glob(format_file_1): 
    new_filename=str(file)
    new_filename1=new_filename[0:len_format_file:1]
    len_filename=len(new_filename1)+1         
    search=str(new_filename1)+'.out'
    #work with .out files
    with open(search) as k:
        #uu=str(k.readlines())
        bingo=[]
        lines = k.readlines() #run through each file
        for line in lines: 
            position_coordinate=line.find('POSITION')
            newstring=line.find('Range: ')
            newstring1=line[newstring:position_coordinate]
            bingo.append(newstring1) #it`s a list that has crispr without digits (of the location crispr-cas)
            bingo = [x for x in bingo if x != ''] #delete '' from the list bingo (==save everything except '') #НАДО ДОБАВИТЬ ИЗБАВЛЕНИЕ ОТ WARNING!
            bingo=[y.replace('Range: ', '') for y in bingo]#delete 'Range: ' from the list bingo 
            bingo=[k.replace('-','') for k in bingo]#delete '-' from the list bingo
        print(bingo)
        bingo_new=[]
        for coordinate in bingo:
            bingo_new.append(coordinate.split())  
        print(bingo_new)    
    with open(file) as file1:
        newline_breaks=""
        for line in file1: 
            stripped_line = line.strip()
            newline_breaks += stripped_line
        dna_len=len(newline_breaks)
    #print(dna_len)  
    if dna_len>length_ORF*2:
        for coordinate in bingo_new:    
            after= int(coordinate[1])
            before=int(coordinate[0])
            before_cut=before-length_ORF+len_filename #т.к. когда код будет читать файл, он начнет с > и чтобы это невелировать добавляю len_filename
            after_cut=after+length_ORF+len_filename #т.к. когда код будет читать файл, он начнет с > и чтобы это невелировать добавляю len_filename
        #print(after_)
        #print(before_)
            
            if before<=length_ORF and after_cut>=dna_len:   
                result=newline_breaks[len_filename:] #чтобы избежать записи > снова!
            elif before>=length_ORF and after_cut<=dna_len:
                result=newline_breaks[before_cut:after_cut]
            elif before<=length_ORF and after_cut<=dna_len:
               result=newline_breaks[len_filename:after_cut]
            elif before>=length_ORF and after_cut>=dna_len:
                result=newline_breaks[before_cut:]    
            #print(result)
            name=str(file)[:len_format_file]+'_'+'nucl-coordin-of-crispr-'+str(before)+'-'+str(after)+'.fa' #добавляет 
            with open(name, 'w') as f: 
                f.write('>'+name[:-3]+' \n'+result)
    else:
       print('file is less than 60k-you can use it without changes')      

