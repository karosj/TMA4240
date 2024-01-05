import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

x = [0.189,0.743,0.605,0.044,0.091,0.045,0.532,0.642,
     0.397,0.583,0.355,0.054,0.155,0.066,0.099]
data = pd.DataFrame({'verdi': x, 'medisin': 
                     ['Trad', 'Trad', 'Trad', 'Trad', 'Trad', 'Trad', 'Trad', 'Trad', 
                      'Ny', 'Ny', 'Ny', 'Ny', 'Ny', 'Ny', 'Ny']})

sns.boxplot(x='medisin',y='verdi',data=data)
plt.show()