import numpy as np
import matplotlib.pyplot as plt

# sett x-verdier og beregn tilhørende F(x)
x = [-1,0]
f_x = np.array([0.05,0.10,0.25,0.40,0.15,0.05])
F_x = [0,0]

for i in np.arange(5+1):    # for-løkke over verdiene 0,1,2,3,4,5
    x = x + [i,i+1]
    FF = np.sum(f_x[np.arange(i+1)])   # verdien til F(i)
    F_x = F_x + [FF,FF]

# lag plott av F(x)
plt.plot(x, F_x, color="red") 
plt.xlabel("x")
plt.ylabel("F(x)")
plt.show()

#stolpediagram for f(x), legger det bare inn her, kan kommenteres ut hvis du vil 
'''
#utfallsrom
x=np.arange(6)

#punktsannsynlighet
f_x = np.array([0.05,0.10,0.25,0.40,0.15,0.05])

#stolpediagram
plt.bar(x, f_x)
plt.xlabel("x")
plt.ylabel("f(x)")  
plt.title("Stolpediagram for f(x)") 
plt.show()'''