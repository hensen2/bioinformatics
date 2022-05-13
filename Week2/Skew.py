def skew(dna):
    values = [0]
    for nucleotide in dna:
        value = values[-1]
        if nucleotide == "G":
            value += 1
        elif nucleotide == "C":
            value -= 1
        values.append(value)
    return values

print(skew("CATGGGCATCGGCCATACGCC"))