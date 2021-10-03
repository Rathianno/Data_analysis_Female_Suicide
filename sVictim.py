import pandas as pd
import matplotlib.pyplot as plt
plt.close("all")

# Reads the file
df = pd.read_csv("FemaleS.csv")

# Groups the cause, takes the mean
causes = df.groupby(['CAUSE']).mean()

# Causestotal = causes[['CAUSE', 'total_female']]

# Prints the median of the professional occupation of female victims.
print(causes[["total_female"]])
causes.plot(kind="bar")
plt.show()
