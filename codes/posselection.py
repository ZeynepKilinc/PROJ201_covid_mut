import matplotlib.pyplot as plt

def findaminoacid(ntlist, maincodon):
    for aa in ntlist:
        for c in aa:
            if maincodon == c:
                return aa
            
            

def makelist(line, list):
    start = 0
    stop = 3

    cleanline = line.replace("-","").replace("N", "").replace("T","A").replace("A", "U").replace("G","C").replace("C","G")

    for x in cleanline:
        while stop < len(cleanline):
            addcodon = cleanline[start:stop]
            list.append(addcodon)
            start += 3
            stop += 3
    return list


file = open("aligned.fasta")
sequences = file.readlines()

#starts with A
Ile = ["AUA", "AUC", "AUU"]
Met = ["AUG"]
Thr =["ACG", "ACA", "ACC", "ACU"]
Asn =["AAC", "AAU"]
Lys = ["AAG", "AAA"]
Ser = ["AGC", "AGU", "UCU", "UCC", "UCA", "UCG"]
Arg = ["AGG", "AGA", "CGU", "CGC", "CGA", "CGG"]  
listA = [Ile, Met, Thr, Asn, Lys, Ser, Arg] 

#starts with G
Val = ["GUU", "GUC", "GUA", "GUG"]
Ala = ["GCU", "GCC", "GCA", "GCG"]
Asp = ["GAU", "GAC"]
Glu = ["GAA", "GAG"]
Gly = ["GGU", "GGC", "GGA", "GGG"]
listG = [Val, Ala, Asp, Glu, Gly]

#starts with U 
Phe = ["UUU", "UUC"]
Leu = ["UUA", "UUG", "CUU", "CUC", "CUA", "CUG"]
Ser = ["UCU", "UCC", "UCA", "UCG", "AGC", "AGU"]
Tyr = ["UAU", "UAC"]
Cys = ["UGU", "UGC"]
Trp = ["UGG"]
Stop = ["UAA", "UAG", "UGA"]
listU = [Phe, Leu, Ser, Tyr, Cys, Trp, Stop]

#starts with C
Leu = ["CUU", "CUC", "CUA", "CUG", "UUA", "UUG"]
Pro = ["CCU", "CCC", "CCA", "CCG"]
His = ["CAU", "CAC"]
Gln = ["CAA", "CAG"]
Arg = ["CGU", "CGC", "CGA", "CGG", "AGG", "AGA"]
listC = [Leu, Pro, His, Gln, Arg]


linenumber = 0
highest = 0
maincodons =[]
linecodons =[]
ratios = []

for line in sequences:

    line = line.replace("-","").replace("N", "").replace("T","A").replace("A", "U").replace("G","C").replace("C","G")
    linenumber += 1
    syncount = 0
    nonsyncount = 0

    if linenumber == 2:

        maincodons = makelist(line, maincodons)


    elif (linenumber % 2 == 0) and (linenumber != 2):
        linecodons =[]
        linecodons = makelist(line, linecodons)

        i = 0
        for x in maincodons:

            if i < len(linecodons) and x != linecodons[i]:

                letter = x[0]
                found = False

                if letter == "A":

                    mainaa = findaminoacid(listA, x)

                    for c in mainaa:
                        if linecodons[i] == c:
                            syncount += 1
                            found = True
                    if found == False:
                        nonsyncount += 1

                elif letter == "G":

                    mainaa = findaminoacid(listG, x)
                    for c in mainaa:
                        if linecodons[i] == c:
                            syncount += 1
                            found = True
                    if found == False:
                        nonsyncount += 1

                elif letter == "C":

                    mainaa = findaminoacid(listC, x)
                    for c in mainaa:
                        if linecodons[i] == c:
                            syncount += 1
                            found = True
                    if found == False:
                        nonsyncount += 1

                elif letter == "U":

                    mainaa = findaminoacid(listU, x)
                    for c in mainaa:
                        if linecodons[i] == c:
                            syncount += 1
                            found = True
                    if found == False:
                        nonsyncount += 1
            
            i += 1

    if syncount != 0 and nonsyncount != 0 and (linenumber % 2 == 0):
        ratio = nonsyncount/syncount
        ratio = round(ratio, 3)
        ratios.append(ratio)
        if ratio > highest:
            highest = int(ratio)
    elif (linenumber % 2 == 0):
        ratios.append(0)


            
file.close()

range = (0, highest)
intervals = 20

plt.hist(ratios, intervals, range, color = 'orange', histtype = 'bar', rwidth = 0.8)
plt.xlabel('dN/dS')
plt.ylabel('number of sequences')

plt.title('dN/dS ratios of sequences')
plt.show()
plt.close()