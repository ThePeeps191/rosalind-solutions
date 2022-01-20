# Problem link: https://rosalind.info/problems/revc/
# Complementing a Strand of DNA

def reverse_complement_dna(dna):
    complement = ""
    complement_table = {"A": "T", "T": "A", "C": "G", "G": "C"}
    for nuc in dna:
        complement += complement_table[nuc]
    return complement[::-1]

data = "AGTGACTTTCATCAAGAATCGTCGGAATCATCCAGCCTGAAATCAGCCAGGCTGGTCCTCGCTGAACCTCACATCCCCGCGGGCGACCTCCGACGACTGACGAACGTATTGTGACAGTTTGGTCGAGCCAAGGAACCCTCCCCACTGGCCGGATTTACGACGATGTCTGGTCTGCCGCCATCTGTCCAAGTTGTCTGCAGGCTTCCACTCGCCGTCGCTGCAATAGAGCGTAGTCCTCGGATAGGATCTTCAGCGAGAGCACGTGTTTTCATCACAGCATCGGTTGGTGCCCCTTAGTTCGGTTTTTCACACTTTGCTGCTCTAGGGTCGTGCGGTCTCCTACGGGGCGAACGACAGTGTGATGGGTAAGGACGAGGGGACAGCTGCTATAGGGTGGCGCTTGTTAGTCGCAAGCACTGCGTTCCATTCTACTGCTAAAGTGAACCTTGCGCGCGAGTGGGGGAAGAGCCTGGTTAAAACGATTTCGAGACTCTGGGTGTGTCCGGGTGCCATGTCTCAGTCTGTTCCTCCCATGAACCCTAGCAGCCAGCTCAAAAACCTGGTTTGTAGCATCTTTGTCATCCAATACGCAATCCTCTAATTTACGGATTATCCCAGTCGATGCTCGGATTCGGAAATATCTATTACATTAAGTGCGGGCATTAGGTTCCTCTAGTGGAGGGTATGCACCAACTGTGTGGTTTTCTCGTCGATACCCTGCGATTAAGCCCTACCTGACGCTCGCCAACGAGACACCTGGGTTTAGGACGTACTCGTGGCAGCGTACGACACCAAATATCTAATACTTCCCTGAAGTGGTTAAGGTCGTGGTCTGTGCACTGCGCTACAAAGTTTAGTTGTAAATGAGGAGTCCTATCGTACAGGAGCCCAAAACTTAGAATAGGAAGTCCCCACCGGAT"
print(reverse_complement_dna(data))