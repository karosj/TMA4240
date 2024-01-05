import numpy as np
import matplotlib.pyplot as plt

# Sett hvilke x-verdier du vil plotte for
x = np.linspace(0,5,100)

# Sett verdien for parameteren alpha
alpha = 1

# Beregn så sannsynlighetstettheten og plott opp funksjonen
f_x = lambda x : 2*x*np.exp(-alpha*x**2)
f_z = lambda z : 4*x*np.exp(-alpha*x**2) - 4*x*(np.exp(-alpha*x**2))**2

plt.plot(x, f_x(x), color="blue")
plt.plot(x, f_z(x), color="red")    
plt.xlabel("x vs y")
plt.ylabel("f(x) vs f(y)")
plt.show()