import numpy as np

#utfallsrom
x = np.arange(6)
#punktsannsynlighet
f_x = np.array([0.05,0.10,0.25,0.40,0.15,0.05]) 
#kumulativ fordelingsfunksjon
F_x = [np.sum(f_x[:i]) for i in range(1,7)]

def simX(n):
    x_sim = np.zeros(n) # for lagring av de simulerte x-ene 
    for i in range(n): #vi simulerer hver og en x for seg
        u = np.random.uniform() # en realisasjon fra uniformfordelingen U(0,1) 
        if(u < F_x[0]): #hvis u er mindre enn den laveste verdien i F_x vil
                          #vi at realisasjonen skal være 0
            x_sim[i] = x[0]
        elif(u <= F_x[1]): # hvis u er mindre enn den nest laveste verdien
            x_sim[i] = x[1] 
        elif(u <= F_x[2]):
            x_sim[i] = x[2] 
        elif(u <= F_x[3]):
            x_sim[i] = x[3] 
        elif(u <= F_x[4]):
            x_sim[i] = x[4] 
        elif(u > F_x[4]):
            x_sim[i] = x[5] 
    return x_sim

# antall realisasjoner 
n = 1000

# simuler x
x = simX(n)

# approksimert forventningsverdi
E_x = np.mean(x)

# approksimert sannsynlighet
P_X_le_2 = np.sum(x <= 2) / n

print("E(X) = ", E_x)
print("P(X <= 2) = ", P_X_le_2)