seq1 = input("Enter the first Sequence: ")
seq2 = input("Enter the second Sequence: ")

mutation_points = []

for i in range(len(seq1)):
    if seq1[i] != seq2[i]:
        mutation_points.append(i)

print("OUTPUT:", mutation_points)