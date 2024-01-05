import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

x = np.array([24.7,24.8,27.3,28.4,28.4,29.0,30.3,32.7,35.6,38.5,38.8,39.3,39.4,39.9,40.3,40.6,40.7,40.7,
              42.9,45.8,46.9,48.2,51.5,51.5,53.4,56.0,56.5,57.3,57.6,59.2,59.8,66.0,67.4,68.8,69.1,69.1])
y = np.array([484,427,413,517,549,648,587,704,979,914,1070,1020,1210,989,1160,1010,1100,1130,1270,1180,
              1400,1760,1710,2010,1880,1980,1820,2020,1980,2310,1940,3260,2700,2890,2740,3140])

# estimerer parametrene ved lineær regresjonsmodell
beta_hat = np.sum((x-np.mean(x))*y)/np.sum((x-np.mean(x))**2)
alpha_hat = np.mean(y) - beta_hat * np.mean(x)

# beregner residualene
y_hat = alpha_hat + beta_hat*x
residuals = y - y_hat

# regner varians
sigma_hat = np.sum(residuals**2)/(len(y))

# hypotesetest
n = len(x) # antall observasjoner
p = 1 # antall prediktorer
x_bar = np.mean(x) 

# regner ut standardfeilen til beta_hat
s_x = np.sqrt(np.sum((x-x_bar)**2)/(n-1)) # standardavviket til x
se_beta_hat = np.sqrt(sigma_hat)/ (s_x * np.sqrt(n))# standardfeilen til beta_hat

#regner ut standardfeilen til alpha_hat
se_alpha_hat = np.sqrt(sigma_hat) * np.sqrt(1/n + x_bar**2)/np.sum((x-x_bar)**2)

#regne ut t-verdien
t_alpha = alpha_hat/se_alpha_hat

#regne ut p-verdien
p_value = 2* (1-stats.t.cdf(np.abs(t_alpha),df=n-p-1))

# avgjøre om vi forkaster H0
alpha = 0.10
reject_H0 = p_value < alpha

print(p_value)
print(reject_H0)