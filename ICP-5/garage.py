import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

plt.style.use(style='ggplot')
plt.rcParams['figure.figsize'] = (10, 6)

train = pd.read_csv('train.csv')


# plot GarageArea field and SalePrice in scatter plot
plt.scatter(x=train['GarageArea'], y=np.log(train.SalePrice))
plt.ylabel('Sale Price')
plt.xlabel('GarageArea')
plt.show()

# outliers removed.
train = train[train['GarageArea'] < 1200].where(train['GarageArea'] > 0)

plt.scatter(x=train['GarageArea'], y=np.log(train.SalePrice))
plt.xlim(-200, 1600)
plt.ylabel('Sale Price')
plt.xlabel('Garage Area')
plt.show()