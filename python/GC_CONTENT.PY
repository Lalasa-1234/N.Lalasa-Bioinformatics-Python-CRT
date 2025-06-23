sequence = input("Enter the DNA sequence: ")
gc_count = 0
for base in sequence:
    if base == 'G' or base == 'C':
        gc_count += 1
gc_percent = (gc_count / len(sequence)) * 100
print("GC Content: ", gc_percent, "%")
if gc_percent > 60:
    print("Classification: High GC")
elif gc_percent >= 40:
    print("Classification: Moderate GC")
else:
    print("Classification: Low GC")