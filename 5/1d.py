import numpy as np
import pandas as pd
from scipy.stats import norm

data = pd.read_csv("blanding.csv")
sigma2 = 0.025**2
x = np.array(data)[:,0]
y = np.array(data)[:,1]

# Beregne estimat for beta
beta_hat = np.sum(x*(1-x)*y) / np.sum((x*(1-x))**2)

# Beregne standardavvik for beta_hat
std_beta_hat = np.sqrt(sigma2 / np.sum((x*(1-x))**2))

# Kritisk verdi for alpha = 0.05
z = norm.ppf(0.975) # siden det er tosidig

# konfidensintervall 
konfidensintervall = [beta_hat - z*std_beta_hat, beta_hat + z*std_beta_hat]
print(f"Konfidensintervall: {konfidensintervall}")