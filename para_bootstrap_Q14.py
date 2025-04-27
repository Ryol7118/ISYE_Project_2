import numpy as np
import matplotlib.pyplot as plot
from scipy.stats import norm


def para_bootstrap_poisson(lambda_p, B, n_bins=76):

    bootstrap_means = np.zeros(B)
    for i in range(B):
        bootstrap = np.random.poisson(lambda_p, n_bins)
        bootstrap_means[i] = np.mean(bootstrap)

    return bootstrap_means

def para_bootstrap_expon(lambda_e, B, n_pals = 296):
    bootstrap_means = np.zeros(B)

    for i in range(B):
        bootstrap = np.random.exponential(lambda_e, n_pals)
        bootstrap_means[i] = np.mean(bootstrap)

    return bootstrap_means


lambda_p = 3.844
lambda_e = 775

bootstrap_means_p = para_bootstrap_poisson(lambda_p, 1000)
bootstrap_means_e = para_bootstrap_expon(lambda_e, 1000)

theta_bar_p = np.mean(bootstrap_means_p)
theta_bar_e = np.mean(bootstrap_means_e)

Lp = np.percentile(bootstrap_means_p, 2.5)
Up = np.percentile(bootstrap_means_p, 97.5)

Le = np.percentile(bootstrap_means_e, 2.5)
Ue = np.percentile(bootstrap_means_e, 97.5)

print(f"original sample mean Poisson: {lambda_p}")
print(f"bootstrapped mean: {theta_bar_p}")
print(f"95% confidance interval for population mean: [{Lp:.4f}, {Up:.4f}]")

print(f"original sample mean Expon: {lambda_e}")
print(f"bootstrapped mean: {theta_bar_e}")
print(f"95% confidance interval for population mean: [{Le:.4f}, {Ue:.4f}]")

'''plot.hist(bootstrap_means_p, bins=30, color = "skyblue", edgecolor = "black", density=True)

plot.xlabel("Sample Poisson Means")
plot.ylabel("Density")
plot.title("Distribution of Poisson Bootstrap Sample Means ")

plot.axvline(3.844, color = "blue", linestyle="--", label="Initial lambda_p: 3.844")
plot.axvline(theta_bar_p, color="red",linestyle="--",label=f"Bootstraph lambda_p: {theta_bar_p:.4f}")
plot.axvline(Lp, color="red", linestyle="--", label=f"Lower Bound Poisson: {Lp:.4f}")
plot.axvline(Up, color="red", linestyle="--", label=f"Upper Bound Poisson: {Up:.4f}")
plot.legend()
plot.show()'''


plot.hist(bootstrap_means_e, bins=30, color = "skyblue", edgecolor = "black", density=True)

plot.xlabel("Sample Exponential Means")
plot.ylabel("Density")
plot.title("Distribution of Exponential Bootstrap Sample Means ")

plot.axvline(775, color = "blue", linestyle="--", label="Initial lambda_e: 775")
plot.axvline(theta_bar_e, color="red",linestyle="--",label=f"Bootstraph lambda_e: {theta_bar_e:.4f}")
plot.axvline(Le, color="red", linestyle="--", label=f"Lower Bound Expnential: {Le:.4f}")
plot.axvline(Ue, color="red", linestyle="--", label=f"Upper Bound Exponential: {Ue:.4f}")
plot.legend()
plot.show()
