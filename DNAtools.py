# List of valid nucleotides
Nucleotides = ["A", "C", "G", "T"]

# Function to check if the sequence is a valid DNA string
def validate_seq(dna_seq):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return True

