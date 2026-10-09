#!/usr/bin/python3


dna = input()
count_g = dna.count('G')
count_c = dna.count('C')
count_gc = count_g + count_c
length = len(dna)
gc = (count_gc / length) * 100
print(f"{gc:.2f}%")
