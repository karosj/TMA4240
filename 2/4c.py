import keyword
import numpy as np
import matplotlib.pyplot as plt

def simulate_round(target):
    dice = np.random.randint(1, 7, 5)
    count_target = np.sum(dice == target)

    #2. kast
    if count_target < 5:
        dice = np.random.randint(1, 7, 5 - count_target)  
        count_target += np.sum(dice == target)

    #3. kast
    if count_target < 5:
        dice = np.random.randint(1, 7, 5 - count_target)  
        count_target += np.sum(dice == target)
    
    return count_target

def generate_Z(n):
    z = []
    for i in range(n):
        Z = sum([i* simulate_round(i) for i in range(1,7)])
        z.append(Z)
    return z

n = 10000
z = generate_Z(n)

#Plotter histogram
plt.hist(z, bins=range(0,61),edgecolor="k", alpha = 0.7)
plt.title("Histogram av simulerte Z-verdier")
plt.xlabel("Z")
plt.ylabel("Frekvens")
plt.axvline(x=44.24, color="r", linestyle="--", label="E[Z] = 44.24")
plt.axvline(x=44.24+10.5, color="b", linestyle="--", label="SD[Z] + 10.5 (øvre grense)")
plt.axvline(x=44.24-10.5, color="b", linestyle="--", label="SD[Z] - 10.5 (nedre grense)")
plt.legend
plt.show()

#Beregner tilnærmet verdi for P(Z større eller lik 42)
p = np.sum(np.array(z) >= 42)/n
print("Tilnærmet verdi for P(Z større eller lik 42):", p)
