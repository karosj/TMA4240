import numpy as np
import matplotlib.pyplot as plt

#Initialisering av parameterverdier
n = 25
alpha = 0.5
beta = 0.25
sigma = 0.25

#Simulering av data etter modell
x = np.random.normal(loc=0,scale=2,size=n) # trekker x_1,x_2,...,x_n
y = alpha + beta * x + np.random.normal(loc=0,scale=sigma,size=n) # genererer tilhørende verdier for y_i

#Visualiserer resultatet i et plott
plt.plot(x,y,'bo')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

def estimerELR(x,y):
    #Beregner gjennomsnitt
    xStrek = np.mean(x)
    yStrek = np.mean(y)
    #Estimater for parametere
    betaHat = np.sum((x-xStrek)*y)/np.sum((x-xStrek)**2)
    alphaHat = yStrek - betaHat * xStrek
    S2 = np.sum((y-(alphaHat+betaHat*x))**2)/(len(x)-2)
    #Returnerer resultatet i en liste
    return [alphaHat,betaHat,S2]

# estimerer parametrene
paramHat = estimerELR(x,y)
alpha_hat, beta_hat, s2 = paramHat

residuals = y - (alpha_hat + beta_hat*x)  # beregner residualene
plt.scatter(x, residuals)  # plotter residualene mot x
plt.xlabel('x')
plt.ylabel('Residualer')
plt.show()

# genererer data etter ny modell
y_new = alpha + beta * x + 0.02 * x**2 + np.random.normal(loc=0,scale=0.10,size=n)

# estimerer parametrene med ny y
paramHat_new = estimerELR(x,y_new)  
alpha_hat_new, beta_hat_new, s2_new = paramHat_new

# beregner estimerte residualer for ny modell
residuals_new = y_new - (alpha_hat_new + beta_hat_new*x)

# plotter residualene for ny modell
plt.scatter(x, residuals_new)
plt.xlabel('x')
plt.ylabel('Residualer (ny modell)')
plt.show()
