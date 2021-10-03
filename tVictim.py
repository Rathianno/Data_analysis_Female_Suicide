import pandas as pd
import matplotlib.pyplot as plt
plt.close("all")

# Reads the file
df = pd.read_csv("FemaleS.csv")

# Groups the data by year, takes the mean
causes = df.groupby(['Year']).mean()

# Prints out the raw stats
print(causes[["total_female"]])

# Makes the bar plot and displays it
causes[["total_female"]].plot(kind="bar")
plt.show()
