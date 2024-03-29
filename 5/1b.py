import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# leser inn datasettet
data = pd.read_csv("blanding.csv")
x = np.array(data)[:,0]
y = np.array(data)[:,1]


teller = sum(x[i] * (1 - x[i]) * y[i] for i in range(len(x)))
nevner = sum(x[i] * (1 - x[i]) ** 2 for i in range(len(x)))
beta_hat = teller / nevner
print(f"Estimatet for beta er: {beta_hat}")