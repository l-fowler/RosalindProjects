"""
The 20 commonly occurring amino acids are abbreviated by using 20 letters from the English
alphabet (all letters except for B, J, O, U, X, and Z). Protein strings are constructed from
these 20 symbols. Henceforth, the term genetic string will incorporate protein strings along
with DNA strings and RNA strings.

The RNA codon table dictates the details regarding the encoding of specific codons into the
amino acid alphabet.

Given: An RNA string s corresponding to a strand of mRNA (of length at most 10 kbp).

Return: The protein string encoded by s.
"""

s = input("Enter RNA string: ").upper()

count = 0
for characters in s:
    if characters == 'A' or characters == 'G' or characters == 'C' or characters == 'U':
        count += 1
    else:
        print("RNA string includes input other than AGCU")
        quit()

if len(s) > 10000:
    print("RNA string is larger than 10 kbp")
    quit()

# ignore end bases if input isn't divisible by 3
if len(s)%3 != 0:
    print("As RNA string is not divisible by 3, the last base(s) will be ignored")


a = []
j = 0
i = 3
# while loop
# if i (multiple of 3) <= len(s), should continue
while i <= len(s):
    pos = s[j:i]
    a.append(pos)
    j += 3
    i += 3

# print(a)

aa = []
index = 0
for rna in a:
    if a[index] == 'UUU' or a[index] == 'UUC':
        aa.append("F")
        index += 1
    elif a[index] == 'UUA' or a[index] == 'UUG' or a[index] == 'CUU' or a[index] == 'CUC' or a[index] == 'CUA' or a[index] == 'CUG':
        aa.append("L")
        index += 1
    elif a[index] == 'UCU' or a[index] == 'UCC' or a[index] == 'UCA' or a[index] == 'UCG' or a[index] == 'AGU' or a[index] == 'AGC':
        aa.append("S")
        index += 1
    elif a[index] == 'CCU' or a[index] == 'CCA' or a[index] == 'CCG' or a[index] == 'CCC':
        aa.append("P")
        index += 1
    elif a[index] == 'AUU' or a[index] == 'AUC' or a[index] == 'AUA':
        aa.append("I")
        index += 1
    elif a[index] == 'AUG':
        aa.append("M")
        index += 1
    elif a[index] == 'ACU' or a[index] == 'ACC' or a[index] == 'ACA' or a[index] == 'ACG':
        aa.append("T")
        index += 1
    elif a[index] == 'GUU' or a[index] == 'GUC' or a[index] == 'GUA' or a[index] == 'GUG':
        aa.append("V")
        index += 1
    elif a[index] == 'GCU' or a[index] == 'GCC' or a[index] == 'GCA' or a[index] == 'GCG':
        aa.append("A")
        index += 1
    elif a[index] == 'UGU' or a[index] == 'UGC':
        aa.append("C")
        index += 1
    elif a[index] == 'UGG':
        aa.append("W")
        index += 1
    elif a[index] == 'UAU' or a[index] == 'UAC':
        aa.append("Y")
        index += 1
    elif a[index] == 'CGU' or a[index] == 'CGC' or a[index] == 'CGA' or a[index] == 'CGG' or a[index] == 'AGG' or a[index] == 'AGA':
        aa.append("R")
        index += 1
    elif a[index] == 'CAU' or a[index] == 'CAC':
        aa.append("H")
        index += 1
    elif a[index] == 'CAA' or a[index] == 'CAG':
        aa.append("Q")
        index += 1
    elif a[index] == 'AAU' or a[index] == 'AAC':
        aa.append("N")
        index += 1
    elif a[index] == 'AAA' or a[index] == 'AAG':
        aa.append("K")
        index += 1
    elif a[index] == 'GGU' or a[index] == 'GGC' or a[index] == 'GGA' or a[index] == 'GGG':
        aa.append("G")
        index += 1
    elif a[index] == 'GAU' or a[index] == 'GAC':
        aa.append("D")
        index += 1
    elif a[index] == 'GAA' or a[index] == 'GAG':
        aa.append("E")
        index += 1
    # without stop codon the string will stop printing
    # elif a[index] == 'UAA' or a[index] == 'UAG' or a[index] == 'UGA':
    #     aa.append("Stop")
    #     index += 1

print(''.join(aa))

