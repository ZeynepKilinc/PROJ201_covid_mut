def ntseqcomp():

    file = open('covid_nucleotide_sequences.fasta')
    content = file.readlines()

    sequencenumber = 0
    index = 0
    totalcount = 0
    processed = 0
    sequences = {}

    for x in content:
        seqcount = 0
        Acount = 0 
        Gcount = 0 
        Ccount = 0 
        Tcount = 0 
        seqlist = {}
        string = str(x)

        if string[0] != '>':
            sequencenumber += 1
            totalcount += 1

            for x in string:
                seqcount += 1

                if x == 'A':
                    Acount += 1
                if x == 'G':
                    Gcount += 1
                if x == 'C':
                    Ccount += 1
                if x == 'T':
                    Tcount += 1

            if totalcount == 100000:
                totalcount = 0
                processed += 100000
                print(processed,  "sequences have been processed.")

            seqlist["A"] = int((Acount/seqcount) * 100)
            seqlist["T"] = int((Tcount/seqcount) * 100)
            seqlist["G"] = int((Gcount/seqcount) * 100)
            seqlist["C"] = int((Ccount/seqcount) * 100)

            sequences['seq' + str(sequencenumber)] = seqlist

    file.close()

    out = open("ntseqcomp.txt", "w")
    out.write("    \tA\tT\tG\tC\n")

    iS = -1

    names = list(sequences.keys())
    values = []
    compdic = list(sequences.values())
    for x in compdic:
        values.append(list(x.values()))

    for x in sequences:
        iV = -1
        iS += 1
        out.write(names[iS] + "\t")
        for x in values[iS]:
            iV +=1
            out.write(str(values[iS][iV]) + "\t")
        out.write("\n")

    out.close()
