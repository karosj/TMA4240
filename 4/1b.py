import numpy as np
import matplotlib.pyplot as plt

# definerer variabler
n = 10000
mu_s = 241.3
mu_t = 7.02
sigma_s = 2
sigma_t = 1

# simulerer S og T og G
simS = np.random.normal(mu_s, sigma_s, n)
simT = np.random.normal(mu_t, sigma_t, n)
simG = (2*simS)/(simT**2)

# finner E(G) og SD_G
mu_G = np.mean(simG)
SD_G = np.std(simG)

# plotter histogram
plt.hist(simG, bins=100, density=True, alpha=0.6, color='g', label="10000 simulasjoner av G")
xmin, xmax = plt.xlim()
x = np.linspace(xmin,xmax,100)
p = (1/(SD_G * np.sqrt(2 * np.pi))) * np.exp(-(x-mu_G)**2/(2 * SD_G**2))
plt.plot(x,p,'k', linewidth = 2)
plt.legend()
plt.show()