import pandas as pd
import matplotlib.pyplot as plt
from sklearn.svm import SVC, LinearSVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df = pd.read_csv('./glass.csv')
y = df["Type"]
df1 = df.drop("Type",axis=1).copy()
# create training and testing
X_train, X_test, Y_train, Y_test = train_test_split(df1, y,test_size=0.15)
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

