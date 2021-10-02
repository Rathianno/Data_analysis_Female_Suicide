import pandas as pd
import matplotlib.pyplot as plt
plt.close("all")

# reads the file
df = pd.read_csv("FemaleS.csv")

# groups the cause, takes the mean
causes = df.groupby(['CAUSE']).mean()

#causestotal = causes[['CAUSE', 'total_female']]

# prints the median of the professional occupation of female victims.
print(causes[["total_female"]])
causes.plot(kind="bar")
plt.show()

tf = pd.read_csv("yrtotal.csv")
display(tf)
