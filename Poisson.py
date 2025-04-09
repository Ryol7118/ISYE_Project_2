import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = open('data.txt')
palins = []
distances = []
distances.append(0)
i = 0
in_count = 0


for line in data:
    num = int(line.strip())
    palins.append(num)
    if i > 0:
        distances.append(num - palins[i-1])
        in_count +=1
    i+=1

x_bar = np.mean(distances)
print('****************************************')
print('Palindromes\' Count  Observed Number O_i')
print('****************************************')

i = 0
in_count = 0
interval = 1

while palins[i] < max(palins):
    in_count += 1
    i+=1
    if palins[i] > interval*3000:
        print(f'      {interval - 1}                    {in_count}')
        in_count = 0
        interval+=1
    
print(f"Average Distance between palindrome: {np.mean(distances)}")

x = np.linspace(0, max(distances), 1000)
y = 1/x_bar*np.exp(-1/x_bar*x)
plt.hist(distances, bins = 30, color="skyblue", edgecolor='black', density = True)
plt.plot(x, y, 'r-')
plt.xlabel("Distance between Consecutive Palindromes")
plt.ylabel("Density")
plt.show()
