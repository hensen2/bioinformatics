def PatternMatch(pattern, dna):
    locations = []
    for i in range(len(dna) - len(pattern) + 1):
        substring = dna[i: len(pattern) + i]
        if substring == pattern:
            locations.append(str(i))
    return " ".join(locations)

print(PatternMatch("ATAT", "GATATATGCATATACTT"))