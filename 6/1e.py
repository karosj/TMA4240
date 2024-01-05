import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

def simulate_n(n = 20, a = 5, r0 = 12.5, alpha = 0.10):
    alpha_gamma = a 
    beta_gamma = r0 / a

    observations = np.random.gamma(alpha_gamma, beta_gamma, n)

    r_hat = np.mean(observations)
    std_error = np.sqrt(r0**2/(a*n))
    test_observator = (r_hat - r0)/std_error

    return test_observator

m = 100000
critical_value = 1.645
type_I_error = sum(simulate_n() > critical_value for _ in range(m))/m

std_error_estimate = np.sqrt((type_I_error*(1-type_I_error))/m)
konfidensintervall = stats.norm.interval(0.95, loc=type_I_error, scale=std_error_estimate)  # 95% konfidensintervall
print(f"95% konfidensintervall: {konfidensintervall}")