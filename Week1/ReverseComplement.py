def ReverseComplement(dna):
    complement = ""
    for base in dna:
        if base == "A":
            complement += "T"
        elif base == "G":
            complement += "C"
        elif base == "C":
            complement += "G"
        elif base == "T":
            complement += "A"
        else:
            raise Exception('Invalid DNA base.')
    return complement[::-1]

print(ReverseComplement("AAAACCCGGT"))