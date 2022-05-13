import itertools


def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value

def hamming_distance(dna1, dna2):
    if len(dna1) != len(dna2):
        raise Exception("The two DNA strings must have equal length.")
    
    hamming_distance = 0
    for index in range(len(dna1)):
        if dna1[index] != dna2[index]:
            hamming_distance += 1
    
    return hamming_distance




def get_min_hamming_dist(pattern, dna):
    k = len(pattern)
    min_distance = k

    for index in range(len(dna) - k +1):
        sub_dna = dna[index: index + k]
        distance = hamming_distance(pattern, sub_dna)
        if distance < min_distance:
            min_distance = distance
    
    return min_distance



def median_string(dnas, k):
    median_strings = []
    min_d = len(dnas) * k

    for l in itertools.product('ACGT', repeat=k):
        k_mer = ''.join(l)
        d = reduce(lambda a, b: a + b, map(lambda dna: get_min_hamming_dist(k_mer, dna), dnas))
        if d < min_d:
            min_d = d
            median_strings = [k_mer]
        elif d == min_d:
            median_strings.append(k_mer)
    return median_strings


print(median_string(["CTCGATGAGTAGGAAAGTAGTTTCACTGGGCGAACCACCCCGGCGCTAATCCTAGTGCCC", "GCAATCCTACCCGAGGCCACATATCAGTAGGAACTAGAACCACCACGGGTGGCTAGTTTC", "GGTGTTGAACCACGGGGTTAGTTTCATCTATTGTAGGAATCGGCTTCAAATCCTACACAG"], 7))

# dnas = [

# ]

# count = 0
# for i in dnas:
#     if (get_min_hamming_dist("CAGTG", i)) > 0:
#         count += get_min_hamming_dist("CAGTG", i)
# print(count)