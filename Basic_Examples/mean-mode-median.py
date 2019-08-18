import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as sp


### Creates a random array with incomes.
incomes = np.random.normal(100.0, 20.0, 10000)

### Creates a hist char of incomes with 50 buckets
plt.hist(incomes, 50)
plt.show()

### Prints the mean and median of incomes
print("{}{}".format("mean: ", np.mean(incomes)))
print("{}{}".format("median: ", np.median(incomes)))


### Prints the mean and median of incomes adding a huge income into the data.
incomes = np.append(incomes,[1000000000])

print("{}{}".format("mean with bill: ", np.mean(incomes)))
print("{}{}".format("median with bill: ", np.median(incomes)))

## Creates a random input data with an ages from 10 to 90 years with 1000 data points.
## Prints its mode.
ages = np.random.randint(10, high=90, size=1000)
print(sp.mode(ages))
