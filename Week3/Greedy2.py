def score(motifs):
    ## '''Returns the score of the given list of motifs.'''
    columns = [''.join(seq) for seq in zip(*motifs)]
    max_count = sum([max([c.count(nucleotide) for nucleotide in 'ACGT']) for c in columns])
    return len(motifs[0])*len(motifs) - max_count



def profile(motifs):
    ## '''Returns the profile of the dna list motifs.'''
    columns = [''.join(seq) for seq in zip(*motifs)]
    return [[float(col.count(nuc)) / float(len(col)) for nuc in 'ACGT'] for col in columns]



def profile_most_probable(dna, k, profile):
    nuc_row = {'A': 0, 'C': 1, 'G': 2, 'T':3}
    prob_tracker = {}
    most_prob = []
    for i, nuc in enumerate(dna):
        nuc
        end_index = i + k - 1
        if end_index < len(dna):
            k_mer = dna[i: i + k]
            if k_mer not in prob_tracker: 
                k_mer_score = 0   
                for i2, nuc2 in enumerate(k_mer):
                    k_mer_score += (1.0 - profile[nuc_row[nuc2]][i2]) * 10

                prob_tracker[k_mer] = k_mer_score

    # sort the new list of probable k-mers           
    sorted_probs = sorted(
        prob_tracker.items(),
        key=lambda x: x[1],
        reverse=False
    )

    # filters for k_mers with max probability
    filter_value = sorted_probs[0][1]
    filtered_probs = filter(
        lambda x: x[1] == filter_value,
        sorted_probs
    )
    
    # takes filtered sequences and puts them in a list
    for item in filtered_probs:
        most_prob.append(item[0])
    
    return most_prob



def profile_most_probable_kmer(dna, k, profile):
    '''Returns the profile most probable k-mer for the given input data.'''
    # A dictionary relating nucleotides to their position within the profile.
    nuc_loc = {nucleotide:index for index,nucleotide in enumerate('ACGT')}

    # Initialize the maximum probabily.
    max_probability = -1

    # Compute the probability of the each k-mer, store it if it's currently a maximum.
    for i in range(len(dna)-k+1):
        # Get the current probability.
        current_probability = 1
        for j, nucleotide in enumerate(dna[i:i+k]):
            current_probability *= profile[j][nuc_loc[nucleotide]]

        # Check for a maximum.
        if current_probability > max_probability:
            max_probability = current_probability
            most_probable = dna[i:i+k]

    return most_probable



def greedy_motif_search(dna_list, k):
    # '''Runs the Greedy Motif Search algorithm and returns the best motif.'''
    # Initialize the best score as a score higher than the highest possible score.
    t = len(dna_list)
    best_score = t * k
    best_motifs = None

    # Run the greedy motif search.
    for i in range(len(dna_list[0])-k+1):
        # Initialize the motifs as each k-mer from the first dna sequence.
        motifs = [dna_list[0][i:i+k]]

        # Find the most probable k-mer in the next string.
        for j in range(1, t):
            current_profile = profile(motifs)
            motifs.append(profile_most_probable_kmer(dna_list[j], k, current_profile))

        # Check to see if we have a new best scoring list of motifs.
        current_score = score(motifs)
        if current_score < best_score:
            best_score = current_score
            best_motifs = motifs

    return best_motifs

def profile_laplace(motifs):
    '''Returns the profile of the dna list motifs.'''
    columns = [''.join(seq) for seq in zip(*motifs)]
    return [[float(col.count(nuc) + 1) / float(len(col) + 4) for nuc in 'ACGT'] for col in columns]


def greedy_motif_search_laplace(dna_list, k):
    """
    Runs the Greedy Motif Search algorithm and returns the best motif,
    with applications of Laplace's Rule of Succession
    """
    # Initialize the best score as a score higher than the highest possible score.
    t = len(dna_list)
    best_score = t*k
    best_motifs = None

    # Run the greedy motif search.
    for i in range(len(dna_list[0])-k+1):
        # Initialize the motifs as each k-mer from the first dna sequence.
        motifs = [dna_list[0][i:i+k]]
        current_profile = profile_laplace(motifs)

        # Find the most probable k-mer in the next string.
        for j in range(1, t):
            motifs.append(profile_most_probable_kmer(dna_list[j], k, current_profile))
            current_profile = profile_laplace(motifs)

        # Check to see if we have a new best scoring list of motifs.
        current_score = score(motifs)
        if current_score < best_score:
            best_score = current_score
            best_motifs = motifs

    return best_motifs




