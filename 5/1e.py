import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.stats import norm

data = pd.read_csv("blanding.csv")
sigma2 = 0.025**2
x = np.array(data)[:,0]
y = np.array(data)[:,1]

# beregner estimat for beta
beta_hat = np.sum(x*(1-x)*y) / np.sum((x*(1-x))**2)

# beregner konfidensintervall for ulike verdier av x0
x0 = np.linspace(0, 1, 100)
lower_bounds = []
upper_bounds = []

for i in x0:
    mu0_hat = beta_hat * x0 * (1 - x0)
    var_mu0_hat = sigma2 * (x0 * (1 - x0))**2 / np.sum((x * (1 - x))**2)
    std_mu0_hat = np.sqrt(var_mu0_hat)
    
    lower = mu0_hat - norm.ppf(0.975) * std_mu0_hat
    upper = mu0_hat + norm.ppf(0.975) * std_mu0_hat
    
    lower_bounds.append(lower)
    upper_bounds.append(upper)

# plott
plt.scatter(x, y, label='blanding.csv')
plt.plot(x0, lower_bounds, 'r--', label='Nedre konfidensintervall')
plt.plot(x0, upper_bounds, 'g--', label='Øvre konfidensintervall')
plt.xlabel("Andel av A")
plt.ylabel("Avvik fra ideell blanding")
plt.title("Spredningsplott av andel A vs. avvik fra ideell blanding")
plt.grid(True)
plt.legend()
plt.show()