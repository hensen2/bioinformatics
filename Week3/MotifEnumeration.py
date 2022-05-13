bases = ["A", "G", "C", "T"]

def reduce(function, iterable, initializer=None):
    it = iter(iterable)
    if initializer is None:
        value = next(it)
    else:
        value = initializer
    for element in it:
        value = function(value, element)
    return value

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



def find_motifs(dna, k, d):
    motifs = set()
    
    for index in range(len(dna) - k + 1):
        motif = dna[index: index + k]
        neighbors = get_neighbors(motif, d)
        motifs.add(motif)
        for neighbor in neighbors:
            motifs.add(neighbor)
        
    return motifs



def motif_enumeration(dnas, k, d):
    motifs = []
    for dna in dnas:
        motifs.append(find_motifs(dna, k, d))
    from operator import and_

    return reduce(and_, motifs)



## Testing ##
print(" ".join(motif_enumeration(["ATTCGACCACGAGATACACCACCTT", "TCACTACGACGACCTTGGAGCCAGC", "CGCCCACGACACTCTCAAACAATGC", "TTCGGGGATTGCAAGACGACCTCTT", "GTGTAACAACAGCAGACGCGCGGGG", "ATTTGCGCGTTATTAACTTTACGAC"], 5, 1)))