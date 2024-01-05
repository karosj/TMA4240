import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

# Data
x = np.array([24.7,24.8,27.3,28.4,28.4,29.0,30.3,32.7,35.6,38.5,38.8,39.3,39.4,39.9,40.3,40.6,40.7,40.7,
              42.9,45.8,46.9,48.2,51.5,51.5,53.4,56.0,56.5,57.3,57.6,59.2,59.8,66.0,67.4,68.8,69.1,69.1])
y = np.array([484,427,413,517,549,648,587,704,979,914,1070,1020,1210,989,1160,1010,1100,1130,1270,1180,
              1400,1760,1710,2010,1880,1980,1820,2020,1980,2310,1940,3260,2700,2890,2740,3140])

# Estimerer parametere for lineær regresjonsmodell
beta_hat = np.sum((x - np.mean(x)) * y) / np.sum((x - np.mean(x))**2)
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

# genererer nye x-verdier for prediksjon
x0 = np.linspace(np.min(x), np.max(x), 100)

# t-verdi for 90% konfidensintervall
t = stats.t.ppf(1 - (1 - 0.90) / 2, df=n - p - 1)

# Beregner prediksjonsintervaller
lower_bounds = []
upper_bounds = []

for x_val in x0:
    y0 = alpha_hat + beta_hat * x_val
    pred_error_var = sigma_hat * (1 + 1/n + (x_val - x_bar)**2 / np.sum((x - x_bar)**2))
    prediction_interval = t * np.sqrt(pred_error_var)
    lower_bounds.append(y0 - prediction_interval)
    upper_bounds.append(y0 + prediction_interval)

# Plotter
plt.figure(figsize=(14, 7))
plt.scatter(x, y, color='blue', label="Observert data")
plt.plot(x0, alpha_hat + beta_hat * x0, color='red', label="Estimert regresjonslinje")
plt.plot(x0, lower_bounds, color='green', label="Nedre 90% prediksjonsintervall")
plt.plot(x0, upper_bounds, color='green', label="Øvre 90% prediksjonsintervall")
plt.fill_between(x0, lower_bounds, upper_bounds, color='yellow', alpha=0.2, label="90% prediksjonsintervall")

plt.title("Spredningsplott med Prediksjonsintervall")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
