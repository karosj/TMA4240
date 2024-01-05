import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from random import sample

x = [0.189,0.743,0.605,0.044,0.091,0.045,0.532,0.642,
     0.397,0.583,0.355,0.054,0.155,0.066,0.099]
data = pd.DataFrame({'verdi': x, 'medisin': 
                     ['Trad', 'Trad', 'Trad', 'Trad', 'Trad', 'Trad', 'Trad', 'Trad', 
                      'Ny', 'Ny', 'Ny', 'Ny', 'Ny', 'Ny', 'Ny']})

sns.boxplot(x='medisin',y='verdi',data=data)
plt.show()

trad_medicine = [0.189, 0.743, 0.605, 0.044, 0.091, 0.045, 0.532, 0.642]
new_medicine = [0.397, 0.583, 0.355, 0.054, 0.155, 0.066, 0.099]

def testStatistic(x,nTrad):  
    #x inneholder alle observerte verdier, de nTrad 
    #første av disse er for pasienter som som fikk tradisjonell medisin    
    
    #gjennomsnitt av observerte verdier for pasienter som fikk tradisjonell medisin:
    meanTrad = np.mean(x[0:(nTrad+1)])
    #gjennomsnitt av observerte verdier for pasienter som fikk by medisin
    meanNew = np.mean(x[(nTrad+1):]) 
    
    return meanNew - meanTrad  #returnerer differansen

# observerte verdier for tradisjonell og ny medisin
x = trad_medicine + new_medicine

# regner ut observert verdi av testobservatoren
statistic_observed = testStatistic(x = x, nTrad = 8)
print(f"Observert verdi av testobservatoren: {statistic_observed}")

# genererer tilfeldig permutasjon av alle elementene i x
x_permuted = sample(x, len(x))

# regner ut simulert verdi av testobservatoren
statistic_simulated = testStatistic(x = x_permuted, nTrad = 8)
print(f"Simulert verdi av testobservatoren: {statistic_simulated}")

# permtasjonstest
m = 10000
count = 0
for _ in range(m):
    x_permuted = sample(x, len(x))
    statistic_simulated = testStatistic(x = x_permuted, nTrad = 8)
    # sammenligner med observert verdi av testobservatoren
    if statistic_simulated > statistic_observed:
        count += 1

# estimerer p-verdi
p_value = count/m
print(f"p-verdi: {p_value}")