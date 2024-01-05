import numpy as np
import matplotlib.pyplot as plt

def simX(n, alpha):
    u = np.random.uniform(size=n) # array med n elementer.
    x = np.sqrt(-alpha * np.log(1 - u)) # formelen du fant for x
    return x

def fx(x, alpha):
    return (2*x/alpha) * np.exp(-x**2/alpha)

# Sett antall realisasjoner og verdien til alpha
n = 10000000
alpha = 1

# simuler X
x = simX(n, alpha)

# lage histogram for de simulerte x-ene
plt.hist(x, density=True, bins=100, label='Histogram for simulerte x-er') #tetthet=True gjør at vi får et sannsynlighetshistogram

# angir navn på aksene
plt.xlabel('x')
plt.ylabel('f(x)')

# regner ut og plotter f(x) på samme plott
x = np.linspace(0, 5, 100)
plt.plot(x, fx(x, alpha), 'r-', color = "black", label='sannsynlighetsfordeling f(x)')
plt.legend
plt.show()