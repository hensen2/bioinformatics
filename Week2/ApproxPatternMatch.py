def approximate_pattern_matching(pattern, dna, mismatches):
    pattern_len = len(pattern)
    matches = []
    for index in range(len(dna) - pattern_len + 1):
        sub_dna = dna[index:index + pattern_len]
        hamming_distance = 0
        is_match = True
        for i in range(pattern_len):
            if pattern[i] != sub_dna[i]:
                hamming_distance += 1
                if hamming_distance > mismatches:
                    is_match = False
                    break
        if is_match:
            matches.append(index)
    return matches

def approximate_pattern_matching_count(pattern, dna, mismatches):
    return len(approximate_pattern_matching(pattern, dna, mismatches))

print(approximate_pattern_matching_count("GAGG", "TTTAGAGCCTTCAGAGG", 2))
