
bases = input("Please copy and paste your base sequence: ")

#AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC

print(bases)

#count the A, C, G, T, U bases
A_count = bases.count('A')
print("A:", A_count)
C_count = bases.count('C')
print("C:", C_count)
G_count = bases.count('G')
print("G:", G_count)
T_count = bases.count('T')
print("T:", T_count)

print("Total:", A_count+C_count+G_count+T_count)
