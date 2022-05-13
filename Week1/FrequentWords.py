def FrequentWords(dna, k):
    frequency_map = {}
    length = len(dna)
    for i in range(len(dna) - k + 1):
        pattern = dna[i: k + i]
        if pattern in frequency_map:
            frequency_map[pattern] += 1
        else:
            frequency_map[pattern] = 1

    max_count = 0
    frequent_patterns = []
    for k_mer, count in frequency_map.items():
        if count > max_count:
            frequent_patterns = [k_mer]
            max_count = count
        elif count == max_count:
            frequent_patterns.append(k_mer)

    return frequent_patterns

print(FrequentWords("ACGTTGCATGTCGCATGATGCATGAGAGCT", 4))