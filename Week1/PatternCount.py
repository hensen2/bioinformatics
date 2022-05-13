def PatternCount(dna, pattern):
    count = 0
    for i in range(len(dna) - len(pattern) + 1):
        if dna[i: (len(pattern) + i)] == pattern:
            count += 1
    return count

print(PatternCount("GCGCG", "GCG"))