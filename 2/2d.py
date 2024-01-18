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

E_Y = np.mean(Y)
SD_Y = np.std(Y)
P_Y_geq_2 = sum([1 for y in Y if y >= 2])/n
P_Y_geq_2_given_Y_geq_1 = sum([1 for y in Y if y >= 2])/sum([1 for y in Y if y >= 1])

print(f"E(Y) = {E_Y:.4f}")
print(f"SD(Y) = {SD_Y:.4f}")
print(f"P(Y ≥ 2) = {P_Y_geq_2:.4f}")
print(f"P(Y ≥ 2|Y ≥ 1) = {P_Y_geq_2_given_Y_geq_1:.4f}")