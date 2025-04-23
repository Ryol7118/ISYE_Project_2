import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Set parameters for reproducibility
np.random.seed(42)

# Parameters
n = 25          # Sample size
N = 2000        # Number of samples
population_mean = 0
population_std = 1

# Generate N samples each of size n from N(0,1)
samples = np.random.normal(loc=population_mean, scale=population_std, size=(N, n))

# Compute sample means for each of the N samples
sample_means = np.mean(samples, axis=1)

# Question 7: Plot normalized histogram of sample means
plt.figure(figsize=(10, 6))
plt.hist(sample_means, bins=30, density=True, alpha=0.6, color='green', label='Sample Means')

# Overlay theoretical normal distribution (CLT)
theoretical_std = population_std / np.sqrt(n)
x = np.linspace(np.min(sample_means), np.max(sample_means), 100)
plt.plot(x, norm.pdf(x, population_mean, theoretical_std), 
         'r-', linewidth=2, label='Theoretical Distribution')

plt.xlabel('Sample Mean')
plt.ylabel('Density')
plt.title('Sampling Distribution of the Sample Mean')
plt.legend()
plt.savefig("Q7.png")

# Question 8: Compare theoretical and simulated mean/SE
simulated_mean = np.mean(sample_means)
simulated_std_error = np.std(sample_means, ddof=1)  # Sample standard deviation

print(f"Theoretical Mean: {population_mean:.4f}")
print(f"Simulated Mean: {simulated_mean:.4f}\n")
print(f"Theoretical Standard Error: {theoretical_std:.4f}")
print(f"Simulated Standard Error: {simulated_std_error:.4f}")

# Question 9: Compute and plot confidence intervals using percentiles

plt.figure(figsize=(10, 6))
plt.hist(sample_means, bins=30, density=True, alpha=0.6, color='green', label='Sample Means')

# Overlay theoretical normal distribution (CLT)
theoretical_std = population_std / np.sqrt(n)
x = np.linspace(np.min(sample_means), np.max(sample_means), 100)
plt.plot(x, norm.pdf(x, population_mean, theoretical_std), 
         'r-', linewidth=2, label='Theoretical Distribution')

confidence_level = 95
alpha = (100 - confidence_level) / 2
ci_low, ci_high = np.percentile(sample_means, [alpha, 100 - alpha])

# Theoretical confidence interval (z-score for 95% CI)
z_score = 1.96
theoretical_ci_low = population_mean - z_score * theoretical_std
theoretical_ci_high = population_mean + z_score * theoretical_std

# Plot mean and confidence intervals
plt.axvline(simulated_mean, color='black', linestyle='--', 
            label=f'Simulated Mean: {simulated_mean:.4f}')
plt.axvline(ci_low, color='blue', linestyle='--', 
            label=f'Simulated {confidence_level}% CI')
plt.axvline(ci_high, color='blue', linestyle='--')
plt.axvline(theoretical_ci_low, color='red', linestyle=':', 
            label=f'Theoretical {confidence_level}% CI', linewidth=2)
plt.axvline(theoretical_ci_high, color='red', linestyle=':', linewidth=2)


plt.xlabel('Sample Mean')
plt.ylabel('Density')
plt.title('Sampling Distribution of the Sample Mean')
plt.legend()
plt.savefig("Q9.png")