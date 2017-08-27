import pandas as pd
from pandas import DataFrame
from sklearn.cross_validation import train_test_split
import numpy as np
from numpy import ndarray
from sklearn.metrics import r2_score
from sklearn.svm import SVR
from sklearn.preprocessing import MinMaxScaler



df = pd.read_csv("solution.csv")
scaler = MinMaxScaler()
df[['BHK', 'AREA', 'YEARS', 'BATH', 'FLOOR', 'LAT', 'LONG', 'MD_AIRPORT']] = scaler.fit_transform(df[['BHK', 'AREA', 'YEARS', 'BATH', 'FLOOR', 'LAT', 'LONG', 'MD_AIRPORT']])

dfx = df[['BHK', 'AREA', 'YEARS', 'BATH', 'FLOOR', 'LAT', 'LONG', 'MD_AIRPORT']].copy()
dfy = df[['PRICE']].copy()

x_train, x_test, y_train, y_test = train_test_split(dfx,dfy,test_size = 0.3)
model = SVR(kernel='rbf')
model.fit(x_train, y_train)
ans = model.predict(x_test)
nytest = y_test.as_matrix()
result_r2 = r2_score(nytest, ans)
print result_r2