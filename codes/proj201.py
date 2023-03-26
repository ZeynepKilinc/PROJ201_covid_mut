
#This function gets rid of the new line characters at the end of lines that contain sequence data of FASTA files
#Descriptive lines stay the same
#Takes the file name as a parameter and opens a new file to write into
#Writes the single line format of the given FASTA file into the new file
def fasta_to_single_line(filename):
    with open(filename) as input_file, open('updated_covid_nucleotide_sequences.fasta', 'w') as new_file: #open the given file and create new in the same statement
        sequence=''  # the string that will be updated and writen into the new file
        for line in input_file:
            if line.startswith('>'):
                if sequence!='':   #if sequence variable is updated previously, it is writen first as a whole
                    new_file.write(sequence + '\n')  #\n character is added because descriptive line (which will be written after this) needs to be seprated from the data                  
                    sequence='' #sequence is emptied after writing operation
                new_file.write(line) #desciriptive line is written into the file 
            else:   
                sequence+=(line.replace('\n', ''))   #sequence variable is is updated to hold the lines of data without \n character in each loop until the descriptive line

        if sequence!='': #this statement is for the final data block which does not have a descriptive line after it
            new_file.write(sequence + '\n')

fasta_to_single_line('test.txt')



