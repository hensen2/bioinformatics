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

def minimum_skew(dna):
    skew_values = skew(dna)
    min_value_indices = []
    min_value = skew_values[0]
    for index in range(len(dna) + 1):
        value = skew_values[index]
        if value < min_value:
            min_value_indices = [index]
            min_value = value
        elif value == min_value:
            min_value_indices.append(index)
    return min_value_indices

print(minimum_skew("TAAAGACTGCCGAGAGGCCAACACGAGTGCTAGAACGAGGGGCGTAAACGCGGGTCCGAT"))