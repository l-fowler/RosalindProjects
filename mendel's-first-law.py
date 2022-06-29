# Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms: k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
# Return: The probability that two randomly selected mating organisms will produce an individual possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two organisms can mate.

k = (input("Enter number of homozygous dominant individuals: "))
m = (input("Enter number of heterozygous individuals: "))
n = (input("Enter number of homozygous recessive individuals: "))
try:
    hom_dom = float(k)
    het = float(m)
    hom_rec = float(n)
# Except for words/letters
except:
    print("Input must be a number")
    quit()

population = hom_dom + het + hom_rec

# Find P(recessive phenotype)
# homologous recessive-homologous recessive
n_n = (hom_rec/population) * ((hom_rec-1)/(population-1)) * 1.0
# homologous recessive-heterozygous
m_n = (het/population) * ((hom_rec)/(population-1)) * 0.5
n_m = (het/population) * ((hom_rec)/(population-1)) * 0.5
# heterozygous-heterozygous
m_m = (het/population) * ((het-1)/(population-1)) * 0.25
rec_pheno = n_n + m_n + n_m + m_m
# 1-recessive phenotype = dominant phenotype
print(1-rec_pheno)

