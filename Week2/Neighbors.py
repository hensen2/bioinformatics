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

print(' '.join(get_neighbors("CGGATTTGC", 3)))