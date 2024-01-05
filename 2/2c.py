import numpy as np
import matplotlib.pyplot as plt

def simX(alpha):
    u = np.random.uniform() # array med n elementer.
    x = np.sqrt(-alpha * np.log(1 - u)) # formelen du fant for x
    return x

def simY():
    alphas = [1,1, 1.2, 1.2, 1.2]
    lifetimes = [simX(alpha)for alpha in alphas]
    lifetimes.sort()
    return lifetimes[2] # returnerer tredje lengste levetid

def generate_simY(n):
    return [simY() for i in range(n)]

n = 10000
Y = generate_simY(n)

plt.hist(Y, density=True, bins=100, label='histogram for simulerte x-er', color= "green", edgecolor="black") #tetthet=True gjør at vi får et sannsynlighetshistogram
plt.xlabel('Y')
plt.ylabel('f(Y)')
plt.title("Histogram for simulerte Y-er")
plt.legend()
plt.show()  
