import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC, LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


df = pd.read_csv('./data/cancer.csv')
y = df["diagnosis_result"]
df1 = df.drop("diagnosis_result",axis=1).copy()

#Working with Numeric Features
numeric_features = df1.select_dtypes(include=[np.number])

corr = numeric_features.corr()
print (corr['fractal_dimension'].sort_values(ascending=False)[:4], '\n')

nulls = pd.DataFrame(df1.isnull().sum().sort_values(ascending=False)[:10])
nulls.columns = ['Null Count']
nulls.index.name = 'Feature'
data = df1.select_dtypes(include=[np.number]).interpolate().dropna()
# create training and testing
X_train, X_test, Y_train, Y_test = train_test_split(df1, y,test_size=0.15)

#NaiveByes
model = GaussianNB()
model.fit(X_train,Y_train)
Y_pred = model.predict(X_test)
acc_svc = round(model.score(X_test, Y_test) * 100, 2)
print("Naive Byes accuracy with test is:", acc_svc)
plt.plot(Y_test,label="Y_test")
plt.plot(Y_pred,label="Y_pred")
plt.show()

##SVM
svc = SVC()
svc.fit(X_train, Y_train)
Y_pred = svc.predict(X_test)
#acc_svc = round(svc.score(X_train, Y_train) * 100, 2)
acc_svc1 = round(accuracy_score(Y_test, Y_pred) * 100, 2)
#print("svm accuracy with train is:", acc_svc)
print("svm accuracy with test is:", acc_svc1)
plt.plot(Y_test,label="Y_test")
plt.plot(Y_pred,label="Y_pred")
plt.legend()
plt.show()

##KNN
knn = KNeighborsClassifier(n_neighbors = 3)
knn.fit(X_train, Y_train)
Y_pred = knn.predict(X_test)
acc_knn = round(knn.score(X_train, Y_train) * 100, 2)
print("KNN accuracy is:",acc_knn)
plt.plot(X_test,label="Y_test")
plt.plot(Y_pred,label="Y_pred")
plt.legend()
plt.show()

