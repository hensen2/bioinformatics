import numpy as np

def calc_score(dnas):
    # define constants
    dna_length = len(dnas[0])
    profile = np.zeros((4, dna_length)) # create empty profile array
    nuc_row = {'A': 0, 'C': 1, 'G': 2, 'T': 3}
    score = 0

    nuc_counter = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    highest_prob = 0    
    col_range = range(dna_length)   
    for i in col_range: # for each position in the string
        for dna in dnas: # go through each string
            print(dna)
            for n in dna:
                print(i)
                nuc_counter[n[i]] += 1 # count appearances of a nucleotide in i position of a string
                
                
#            print "s[i]: "+s[i]
#        print "nuc_counter.items(): ",nuc_counter.items()
        for row in nuc_counter.items():
            prob = float(row[1]) / len(dnas) # calculate probability 
            profile[nuc_row[row[0]], i] = prob # set profile accordingly
#            print "prob: "+str(prob)
#            print "profile: "
#            print profile

            if prob > highest_prob:
                highest_prob = prob # picks out most likely nucleotide in each column
#                print "prob > highest_prob"

        score += (1.0 - highest_prob)*10  # converts probability to score
        highest_prob = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
        nuc_counter = 0 # reset counter to calculate next column
        i += 1 # move on to next column
#        print "score: "+str(score)
        
    return (profile, score)


def greedy_motif_search(dnas, k, t):
    pass
    # best_motifs = [dna[:k] for dna in dnas]
    # best_prof, best_score = calc_score(best_motifs)


print(calc_score(["AGGCGGCACATCATTATCGATAACGATTCGCCGCATTGCC",
"ATCCGTCATCGAATAACTGACACCTGCTCTGGCACCGCTC",
"AAGCGTCGGCGGTATAGCCAGATAGTGCCAATAATTTCCT",
"AGTCGGTGGTGAAGTGTGGGTTATGGGGAAAGGCAGACTG",
"AACCGGACGGCAACTACGGTTACAACGCAGCAAGAATATT",
"AGGCGTCTGTTGTTGCTAACACCGTTAAGCGACGGCAACT",
"AAGCGGCCAACGTAGGCGCGGCTTGGCATCTCGGTGTGTG",
"AATTGAAAGGCGCATCTTACTCTTTTCGCTTTCAAAAAAA"]))