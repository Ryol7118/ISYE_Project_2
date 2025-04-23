import numpy as np
import matplotlib.pyplot as plt

positions = []

# Load data
data = open("data.txt")

for line in data:
    num = int(line.strip())
    positions.append(num)


# Create bins of 3000 nucleotides
max_pos = positions[-1]
bins = np.arange(0, max_pos + 3000, 3000)
print("Bins: " + str(bins.size))
counts_per_bin, _ = np.histogram(positions, bins=bins)

# Tally observed counts
observed_counts = np.bincount(counts_per_bin)
print("Palindromes’ count | Observed number (Oi)")
for k in range((bins.size - 1)):
    print(f"      {k}         |          {counts_per_bin[k]}")