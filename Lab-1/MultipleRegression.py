import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn import linear_model
from sklearn.metrics import mean_squared_error

plt.style.use(style='ggplot')
plt.rcParams['figure.figsize'] = (10, 6)

train = pd.read_csv('./data/50_Startups.csv')

#Next, we'll check for skewness
print ("Skew is:", train.Profit.skew())
plt.hist(train.Profit, color='blue')
plt.show()

target = np.log(train.Profit)
print ("Skew is:", target.skew())
plt.hist(target, color='blue')
plt.show()


numeric_features = train.select_dtypes(include=[np.number])
print(numeric_features.describe())

corr = numeric_features.corr()

print(corr['Profit'].sort_values(ascending=False)[:5])

quality_pivot = train.pivot_table(index='Profit',
                                  values='R&D Spend', aggfunc=np.median)
print(quality_pivot)

#Notice that the median sales price strictly increases as Overall Quality increases.
quality_pivot.plot(kind='bar', color='blue')
plt.xlabel('Overall Profit')
plt.ylabel('Median Profit')
plt.xticks(rotation=0)
plt.show()

# deal with the null values
nulls = pd.DataFrame(train.isnull().sum().sort_values(ascending=False)[:25])
nulls.columns = ['Null Count']
nulls.index.name = 'Feature'
print(nulls)

# build a linear regression model
dataset = train.select_dtypes(include=[np.number])

y = np.log(train.Profit)

x = dataset.drop(['Profit'], axis=1)
X_train, X_test, y_train, y_test = train_test_split(x, y, random_state=42, test_size=.33)
lr1 = linear_model.LinearRegression()
model = lr1.fit(X_train, y_train)

# RMSE: Interpreting this value is somewhat more intuitive that the
# r-squared value. The RMSE measures the distance between our predicted
# values and actual values
print('r2 is: ', model.score(X_test, y_test))
prediction = model.predict(X_test)

print('rmse: ', mean_squared_error(y_test, prediction))

actual_values = y_test
plt.scatter(prediction, actual_values, alpha=.75,
            color='b')  # alpha helps to show overlapping data
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Multiple Regression Model')
plt.show()