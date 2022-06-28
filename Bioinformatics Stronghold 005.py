"""
The GC-content of a DNA string is given by the percentage of symbols in the string that are
'C' or 'G'. For example, the GC-content of "AGCTATAG" is 37.5%. Note that the reverse
complement of any DNA string has the same GC-content.

DNA strings must be labeled when they are consolidated into a database. A commonly used
method of string labeling is called FASTA format. In this format, the string is introduced
by a line that begins with '>', followed by some labeling information. Subsequent lines
contain the string itself; the first line to begin with '>' indicates the label of the
next string.

In Rosalind's implementation, a string in FASTA format will be labeled by the ID
"Rosalind_xxxx", where "xxxx" denotes a four-digit code between 0000 and 9999.

Given: At most 10 DNA strings in FASTA format (of length at most 1 kbp each).

Return: The ID of the string having the highest GC-content, followed by the GC-content
of that string. Rosalind allows for a default error of 0.001 in all decimal answers
unless otherwise stated; please see the note on absolute error below.

>Rosalind_6404 CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCC TCCCACTAATAATTCTGAGG
>Rosalind_5959 CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCT ATATCCATTTGTCAGCAGACACGC
>Rosalind_0808 CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGAC TGGGAACCTGCGGGCAGTAGGTGGAAT
"""

print("Enter each input separately, and then type 'done' to continue")
contents = []
count = 0
while count < 10:
    x = input("Enter input: ")
    if x == "done":
        if count == 0:
             print("There must be an input")
             continue
        else:
            count = 10
            continue
    else:
        x = ''.join(x.split())
        # check if x starts with >
        if x.startswith('>Rosalind_'):
            contents.append(x)
            count += 1
        else:
            print("Ignored input '" + x + "' as it does not have to proper input structure: >Rosalind_XXXX")

# print(contents)

sum_ = []
count = 0
while count < len(contents):
    cg = 0
    total = 0
    string = contents[count]
    string = string[14:]
    # print(string)
    if len(string) > 1000:
        print("Sequences must be less than 1 kbp each")
        quit()
    else:
        for char in string:
            if char == 'C' or char == 'G':
                cg += 1
                total += 1
            elif char == 'A' or char == 'T':
                total += 1
            else:
                print("Sequence(s) include input other than ATCG")
                quit()
        # cg/total *100 for cg percentage
        sum = (cg/total)*100
        sum_.append(sum)
        count += 1

# find highest cg value
highest = max(sum_)
# find index of highest cg value
max_index = sum_.index(highest)

# fasta of same index
fasta_max = contents[max_index]
fasta_max = fasta_max[1:14]
print(fasta_max, highest)