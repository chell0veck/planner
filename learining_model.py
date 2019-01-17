from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import statsmodels.formula.api as sm
from statsmodels.api import add_constant
import pandas as pd

import itertools


dataset = pd.read_excel('learn_dataset.xlsx', index_col=0, header=0)
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1:].values
X = add_constant(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

lin_reg = LinearRegression()
lin_reg.fit(X_train, y_train)
ols_reg = sm.OLS(y, X).fit()

lin_pred = lin_reg.predict(X_test)
# ols_pred = ols_reg.predict(X_test)

ols_pred = ols_reg.predict([[1, 1, 18, 5]])

print(round(*ols_pred, 2))

"""
[[ 1. 15. 18.  1.]
 [ 1.  1. 18.  5.]
 [ 1. 14. 18.  3.]
 [ 1.  6.  6.  2.]
 [ 1.  5. 13.  2.]
 [ 1.  4.  4.  5.]
 [ 1.  0.  9.  1.]
 [ 1. 20. 20.  3.]
 [ 1.  0. 10.  3.]
 [ 1.  0.  4.  4.]
 [ 1.  1. 17.  2.]
 [ 1. 12. 16.  3.]
 [ 1. 20. 20.  3.]
 [ 1. 10. 12.  0.]
 [ 1.  9. 14.  4.]
 [ 1. 12. 18.  3.]
 [ 1.  5.  5.  1.]
 [ 1.  2. 13.  1.]
 [ 1.  5. 10.  4.]
 [ 1. 18. 19.  5.]]

[[3]
 [5]
 [5]
 [1]
 [3]
 [2]
 [3]
 [1]
 [4]
 [2]
 [5]
 [4]
 [1]
 [2]
 [4]
 [4]
 [1]
 [4]
 [4]
 [4]]

[2.92002315 5.46995245 3.41985054 1.9034847  3.41200282 2.32372667
 3.08444385 3.03880716 3.65212864 2.65516592 4.71694875 3.28413575
 3.03880716 2.19837031 3.46292942 3.67822963 1.65030838 3.61425252
 3.19149984 3.47077715]
"""