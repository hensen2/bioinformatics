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

                


print(profile_most_probable("CACAATGGTGATGCGTTGTCCCACTGGCAATGTTTCGCCGCCCTCTTTACGTACACCCTTACGAGCATATTCCCATACCGATCTAGGCCTAAAAACTTAGGTGATTTAGCCGTTGCAGTAAGCCGGGACAACGTTTCGTGAATCGTGGCATAGGTAACACGTATATCGCATGGCCATTTAGTGACTATTCAATTCTGGCCCGCGCGTGGGGCTGGGCGGTCAACAGGTGACGACTAGACTACGGGAAAACTCGGTAGACTGGCTGTCTGGTTACAAGTGAGGTGTCAAGTCAGTCTCTGGTCAACTGCGTGCTATAAGCGGCCATCAGAGCCCATAGTTCATGGTCTCAGCACTCGTGCTACGAAGAAACATTTGCTTTACCAAGCACGGGCCAATAGGCGCAGCATTTGCGGGGTTAGACTGTCAGGAAAGTATTAGAATCCCCTGCGCTTGTTAAGCGAATTAAGTTTACCGCAAACCTAGGCAACAATCCGCAGCTTCCTTGTACCATGCATTAGTCTTGACTGCAACGGTACTTACGTTGATTCCCAGATGGTGAGTCTCGACTGCCACAAGACACGGCCCTTGTTATAACCCATTGTGATGTGCTTATGGTAGGCTCCTTGCGCCTTGCTGGGTGCCAGTCCTTCCCTGGACTCTTTTTTGAAGTTCCCTTAGATACCGTTCAGAAAATACAAGGTGCTCAGAGCACTAACCGTTATACCACCAGAGTAAGAGTCCGACGACTATCGCAAAGCCGGGCGACGAAAGGACAGAAACTGTTGTACGGTAAAGGGCGAAAGGCTTAGTGGATGTCAAATACCGTGCTCATGTTATGTACGGTGGGCTCGTATCCCAGTGCGCACTAATCACGATGTCTGTCTGATTTAGGATATCACGGCGTTTAACGGGTCTGTTAACGGCGAGGCTTTGCTGGGAGGAGGCCTTTCCGACTTCACCGTAGAGCAGCCCCTCAAGGGCGAGCAGTCCACCGACTCGA", 14, profile = {
    0: [0.296, 0.239, 0.31, 0.31, 0.296, 0.225, 0.268, 0.296, 0.239, 0.282, 0.155, 0.225, 0.211, 0.296],
    1: [0.225, 0.197, 0.254, 0.225, 0.183, 0.31, 0.31, 0.225, 0.282, 0.239, 0.254, 0.296, 0.225, 0.239],
    2: [0.254, 0.31, 0.183, 0.254, 0.324, 0.141, 0.254, 0.254, 0.239, 0.197, 0.31, 0.169, 0.282, 0.239],
    3: [0.225, 0.254, 0.254, 0.211, 0.197, 0.324, 0.169, 0.225, 0.239, 0.282, 0.282, 0.31, 0.282, 0.225]
}))