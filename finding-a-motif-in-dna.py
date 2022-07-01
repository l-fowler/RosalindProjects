"""
Given two strings s and t, t is a substring of s if t is contained as a contiguous collection of symbols in s (as a result, t must be no longer than s).

The position of a symbol in a string is the total number of symbols found to its left, including itself (e.g., the positions of all occurrences of 'U' in "AUGCUUCAGAAAGGUCUUACG" are 2, 5, 6, 15, 17, and 18). The symbol at position i of s is denoted by s[i].

A substring of s can be represented as s[j:k], where j and k represent the starting and ending positions of the substring in s; for example, if s = "AUGCUUCAGAAAGGUCUUACG", then s[2:5] = "UGCU".

The location of a substring s[j:k] is its beginning position j; note that t will have multiple locations in s if it occurs more than once as a substring of s (see the Sample below).

Given: Two DNA strings s and t (each of length at most 1 kbp).

Return: All locations of t as a substring of s.

Sample Dataset
GATATATGCATATACTT
ATAT

Sample Output
2 4 10
"""

s = input("Enter DNA sequence: ")
t = input("Enter DNA sequence of interest: ")

# substring (t) must be shorter than DNA string (s)
if len(t) > len(s):
    print("DNA sequence must be longer than the DNA sequence of interest")
    quit()
if len(s) > 1000 or len(t) > 1000:
    print("DNA sequences cannot exceed 1 kbp in length")
    quit()

# all locations of t as a substring of s
loc = []
i = 0
for char in s:
    pos = s[i:]
    if pos.startswith(t):
        loc.append(i+1)
        i += 1
    else:
        i +=1

print(*loc)
