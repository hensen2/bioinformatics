bases = ["A", "G", "C", "T"]


def find_all_neighbors(pattern, prefix, d, neighbors):
    if not pattern:
        return
    sub_pattern = pattern[1:]
    for base in bases:
        if base == pattern[0]:
            delta_d = 0 
        else:
            delta_d = 1
        new_d = d - delta_d
        if new_d < 0:
            continue
        new_prefix = prefix + base
        neighbors.add(new_prefix + sub_pattern)
        if sub_pattern:
            find_all_neighbors(sub_pattern, new_prefix, d - delta_d, neighbors)



def get_neighbors(pattern, d):
    neighbors = set()
    find_all_neighbors(pattern, "", d, neighbors)
    return neighbors


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


def freq_words_with_mismatch(dna, k, d):
    patterns = []
    frequencey_map = {}
    dna_length = len(dna)
    max_count = 0
    for index in range(dna_length - k + 1):
        pattern = dna[index: k + index]
        neighborhood = get_neighbors(pattern, d)
        neighborhood = list(neighborhood)
        for i in range(len(neighborhood)):
            neighbor = neighborhood[i]
            if neighbor not in frequencey_map:
                frequencey_map[neighbor] = 1
            else:
                frequencey_map[neighbor] += 1
    
    for pattern in frequencey_map:
        if frequencey_map[pattern] > max_count:
            max_count = frequencey_map[pattern]
    
    for pattern in frequencey_map:
        if frequencey_map[pattern] == max_count:
            patterns.append(pattern)
    
    return patterns


def freq_words_with_mismatch_plus_rc(dna, k, d):

    frequency_map = {}

    for index in range(len(dna) - k + 1):
        pattern = dna[index: k + index]
        neighborhood = get_neighbors(pattern, d)
        neighborhood = list(neighborhood)
        for i in range(len(neighborhood)):
            neighbor = neighborhood[i]
            if neighbor not in frequency_map:
                frequency_map[neighbor] = 1
            else:
                frequency_map[neighbor] += 1
    
    
    rc_dna = ReverseComplement(dna)
    rc_frequency_map = {}

    for index in range(len(rc_dna) - k + 1):
        pattern = rc_dna[index: k + index]
        neighborhood = get_neighbors(pattern, d)
        neighborhood = list(neighborhood)
        for i in range(len(neighborhood)):
            neighbor = neighborhood[i]
            if neighbor not in rc_frequency_map:
                rc_frequency_map[neighbor] = 1
            else:
                rc_frequency_map[neighbor] += 1

    max_sum = 0
    patterns = []
    final_pattern = ""
    final_rc = ""
    for pattern, value in frequency_map.items():
        for rc_pattern, rc_value in rc_frequency_map.items():
            if (value + rc_value) > max_sum:
                if pattern == ReverseComplement(rc_pattern):
                    max_sum = value + rc_value
                    final_pattern = pattern
                    final_rc = rc_pattern
    patterns.append(final_pattern)
    patterns.append(final_rc)
    
    for pattern, value in frequency_map.items():
        for rc_pattern, rc_value in rc_frequency_map.items():
            if pattern == ReverseComplement(rc_pattern) and (value + rc_value) == max_sum:
                if pattern not in patterns and rc_pattern not in patterns:
                    patterns.append(final_pattern)
                    patterns.append(final_rc)
            
    
    return patterns



# print(FrequentWords("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4))
# print(" ".join(freq_words_with_mismatch("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4, 1)))
print(" ".join(freq_words_with_mismatch_plus_rc("AGTTTGGATTTACAGTTTTTTAGGGAGAAACAGACGGAGGAAGGAAACTTTTTTAGACGGAACACACACACTTTACTTTAGGAAAGGGAGGATTTGAAAGGAAGGAAGACACAGGAATTTGGATTTGAATTTAGGGAAGACGAAACGGATTTAGGAAGGAGAAGAAACAGGAAGGAGAAAGGAAAGAGTTTTTTGAAACAGGAAGGAGGAAGTTTGGAAGGAAACGGAGAAGAAAGAGGAAGAAGAA", 5, 2)))