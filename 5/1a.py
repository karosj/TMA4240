import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# leser inn datasettet
data = pd.read_csv("blanding.csv")
x = np.array(data)[:,0]
y = np.array(data)[:,1]

# plotter spredningsplott
plt.scatter(x, y)
plt.xlabel("Andel av A")
plt.ylabel("Avvik fra ideell blanding")
plt.title("Spredningsplott av andel A vs. avvik fra ideell blanding")
plt.grid(True)
plt.show()
