
#input 2 sample datasets
s = input("Enter first sample dataset: ")
t = input("Enter second sample dataset: ")

#length of string cannot exceed 1000 bp length
if (len(s) or len(t)) >1000:
    print("DNA strings exceed 1000bp length")

#lengths of strings must match
elif len(s) != len(t):
    print("length of strings do not match in length")

#compare characters at index for both strings / the Hamming distance dH(s,t)
else:
    count = 0
    for i in range(len(s)):
        if t[i] != s[i]:
            count +=1
    print(count)

#sample DNA example
#GAGCCTACTAACGGGAT
#CATCGTAATGACGGCCT
#7
