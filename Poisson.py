import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = open('data.txt')
palins = []
distances = []
distances.append(0)
i = 0

for line in data:
    num = int(line.strip())
    palins.append(num)
    if i > 0:
        distances.append(num - palins[i-1])
    i+=1

print("Average Distance between palindrome: ")

plt.hist(distances, bins = 30, color="skyblue", edgecolor='black', density = True)
plt.xlabel("Distance between Consecutive Palindromes")
plt.ylabel("Density")
plt.show()
