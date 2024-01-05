import numpy as np
import matplotlib.pyplot as plt

# lager funksjon som simulerer n realisasjoner av Z
def simZ(n, mu, sigma, a, b):
    X = np.random.normal(mu, sigma, n) # simulerer X
    Z = a*X + b 
    return Z

n = 100000
mu = 1
sigma = 2
a = 2
b = 0.5

# simulerer Z
Z = simZ(n, mu, sigma, a, b)

# plotter histogram
plt.hist(Z, bins=100, density=True, alpha = 0.6, color='y')

# oppretter forventningsverdi, varians og standardavvik for Z + normalfordeling
E_Z = a * mu + b
Var_Z = a**2 * sigma**2
SD_Z = np.sqrt(Var_Z)

# genererer punkter for sannsynlighetstetthet for Z
x = np.linspace(E_Z - 4*SD_Z, E_Z + 4*SD_Z, 1000)
pdf = (1/ (SD_Z * np.sqrt(2*np.pi))) * np.exp(-0.5*((x-E_Z)/SD_Z)**2)

# plotting
plt.plot(x, pdf, 'k', linewidth=2)
title = "Histogram og sannsynlighetstetthet for Z"
plt.title(title)
plt.xlabel("Z")
plt.ylabel("Sannsynlighetstetthet for Z")
plt.show()
