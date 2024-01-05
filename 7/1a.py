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
estimate = estimerELR(x,y)
alpha_hat, beta_hat, s2 = estimate

residuals = y - (alpha_hat + beta_hat*x)  # beregner residualene
plt.scatter(x, residuals)  # plotter residualene mot x
plt.xlabel('x')
plt.ylabel('Residualer')
plt.show()

paramHat = estimerELR(x,y)
print('alphaHat: ',paramHat[0])
print('betaHat: ',paramHat[1])
print('s2: ',paramHat[2])  