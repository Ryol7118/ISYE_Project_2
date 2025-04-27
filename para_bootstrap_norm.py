import numpy as np
import matplotlib.pyplot as plot
from scipy.stats import norm

def draw_sample(n):
    return np.random.normal(0, 1, n)

def para_bootstrap(theta_hat, B, n):
    mu_hat = np.mean(theta_hat)
    sig_hat = np.std(theta_hat, ddof=1)

    bootstrap_means = np.zeros(B)
    for i in range(B):
        bootstrap = np.random.normal(mu_hat, sig_hat, n)
        bootstrap_means[i] = np.mean(bootstrap)

    return bootstrap_means


theta_hat = draw_sample(25)
bootstrap_means = para_bootstrap(theta_hat, 2000, 25)

theta_bar = np.mean(bootstrap_means)

L = np.percentile(bootstrap_means, 2.5)
U = np.percentile(bootstrap_means, 97.5)

print(f"original sample mean: {np.mean(theta_hat)}")
print(f"bootstrapped mean: {theta_bar}")
print(f"95% confidance interval for population mean: [{L:.4f}, {U:.4f}]")

plot.hist(bootstrap_means, color = "skyblue", edgecolor = "black", density=True)
plot.xlabel("Sample Mean")
plot.ylabel("Density")
plot.axvline(np.mean(theta_hat), color = "red", linestyle = "--", label=f"Theta_hat: {np.mean(theta_hat):.4f}")
plot.axvline(theta_bar, color = "blue", linestyle="--", label=f"Theta_bar: {theta_bar:.4f}")

plot.axvline(L, color="blue", linestyle="--", label=f"Lower Bound: {L:.4f}")
plot.axvline(U, color="blue", linestyle="--", label=f"Upper Bound: {U:.4f}")

'''x = np.linspace(-1, 1, 100)
plot.plot(x, norm.pdf(x, 0, 1), 
         'r-', linewidth=2, label='N(0,1)')'''

plot.title("Distribution of Parametric Bootstrap Sample Means")
plot.legend()
plot.show()
