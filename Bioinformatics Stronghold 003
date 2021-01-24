
#reverse complement

DNA_strand = input("Enter your DNA stand: ")
DNA_reverse = DNA_strand[::-1]

if len(DNA_strand) >1000:
    print("DNA strand exceeds limit")
else:
    print("Reverse of DNA strand: " + DNA_reverse)

    def complement(seq):
        """
        complement of base where A and T are complements,
        and where C and G are complements
        """
        basecomplement = {"A": "T", "T": "A", "C": "G", "G": "C"}
        letters = list(seq)
        letters = [basecomplement[base] for base in letters]
        return "".join(letters)
    print("Complement reverse of DNA strand: " + complement(DNA_reverse))
