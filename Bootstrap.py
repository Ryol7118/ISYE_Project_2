import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# Set parameters for reproducibility
np.random.seed(38)

# Parameters
n = 25          # Sample size
N = 2000        # Number of samples
population_mean = 0
population_std = 1

# Generate N samples each of size n from N(0,1)
samples = np.random.normal(loc=population_mean, scale=population_std, size=(N, n))

# Compute sample means for each N samples
sample_means = np.mean(samples, axis=1)

# Q7: Plot normalized histogram of sample means
plt.figure(figsize=(10, 6))
plt.hist(sample_means, bins=30, density=True, alpha=0.6, color='green', label='Sample Means')

# Overlay CLT
theoretical_std = population_std / np.sqrt(n)
x = np.linspace(np.min(sample_means), np.max(sample_means), 100)
plt.plot(x, norm.pdf(x, population_mean, theoretical_std), 
         'r-', linewidth=2, label='Theoretical Distribution')

plt.xlabel('Sample Mean')
plt.ylabel('Density')
plt.title('Sampling Distribution of the Sample Mean')
plt.legend()
plt.savefig("Q7.png")

# Q8: Compare theoretical and simulated mean/SE
simulated_mean = np.mean(sample_means)
simulated_std_error = np.std(sample_means, ddof=1)  

print(f"Theoretical Mean: {population_mean:.4f}")
print(f"Simulated Mean: {simulated_mean:.4f}\n")
print(f"Theoretical Standard Error: {theoretical_std:.4f}")
print(f"Simulated Standard Error: {simulated_std_error:.4f}")

# Q9: Compute and plot confidence intervals using percentiles

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


# Generate one random sample of size n = 25
original_sample = np.random.normal(loc=population_mean, scale=population_std, size=n)

# Q10: Bootstrap to compute 95% CI for the mean
bootstrap_means = []
for i in range(N):
    
    bootstrap_sample = np.random.choice(original_sample, size=n, replace=True)
    bootstrap_means.append(np.mean(bootstrap_sample))

# Compute bootstrap confidence interval
confidence_level = 95
alpha = (100 - confidence_level) / 2
ci_low_boot, ci_high_boot = np.percentile(bootstrap_means, [alpha, 100 - alpha])

# Theoretical CI (using population std)
sample_mean = np.mean(original_sample)
theoretical_std_error = population_std / np.sqrt(n)
z_score = 1.96
ci_low_theory = sample_mean - z_score * theoretical_std_error
ci_high_theory = sample_mean + z_score * theoretical_std_error

std_error_bootstrap = np.std(bootstrap_means, ddof=1) 

# Print results
print(f"Original Sample Mean: {sample_mean:.4f}")
print(f"Bootstrap 95% CI: [{ci_low_boot:.4f}, {ci_high_boot:.4f}]")
print(f"Bootstrap STD Error:  {std_error_bootstrap:.4f}")
print(f"Theoretical 95% CI: [{ci_low_theory:.4f}, {ci_high_theory:.4f}]")

# Q11: Compare bootstrap and sampling distributions
plt.figure(figsize=(10, 6))

# Plot bootstrap distribution
plt.hist(bootstrap_means, bins=30, density=True, alpha=0.6, color='blue', 
         label='Bootstrap Means')

# Overlay sampling distribution from Question 7 (reuse earlier data)
plt.hist(sample_means, bins=30, density=True, histtype='step', 
         linewidth=2, color='green', label='Sampling Distribution (Q7)')

# Theoretical distribution (CLT)
x = np.linspace(min(bootstrap_means)-0.5, max(bootstrap_means)+0.5, 100)
plt.plot(x, norm.pdf(x, population_mean, theoretical_std_error), 
         'r--', label='Theoretical N(0, 0.2)')

plt.xlabel('Sample Mean')
plt.ylabel('Density')
plt.title('Bootstrap vs. Sampling Distribution')
plt.legend()
plt.savefig("Q11.png")
