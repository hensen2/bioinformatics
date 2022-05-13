def find_clumps(dna, k, t, L):
    s = dna[0: L]
    counts = count_frequencies(s, k)
    frequent_set = set()
    for pattern, count in iter(counts.items()):
        if count >= t:
            frequent_set.add(pattern)
    
    for index in range(1, len(dna)-L+1):
        begin = dna[index - 1: index - 1 + k]
        counts[begin] -= 1
        end = dna[index + L - k: index + L]
        increase_count(counts, end)
        for pattern, count in iter(counts.items()):
            if count >= t:
                frequent_set.add(pattern)
    
    clumps = sorted(list(frequent_set))
    return clumps

def count_frequencies(dna, k):
    dict = {}
    for index in range(len(dna)-k+1):
        pattern = dna[index: index + k]
        increase_count(dict, pattern)
    return dict


def increase_count(dict, pattern):
    if dict.__contains__(pattern):
        dict[pattern] += 1
    else:
        dict[pattern] = 1

