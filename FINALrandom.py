import pandas as pd
from pandas import DataFrame
from sklearn.cross_validation import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler
import numpy as np
from numpy import ndarray
import csv
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
from sklearn import cross_validation, metrics



df = pd.read_csv("solution.csv")
scaler = MinMaxScaler()
df[['BHK', 'AREA', 'YEARS', 'BATH', 'FLOOR', 'LAT', 'LONG', 'MD_AIRPORT']] = scaler.fit_transform(df[['BHK', 'AREA', 'YEARS', 'BATH', 'FLOOR', 'LAT', 'LONG', 'MD_AIRPORT']])

dfx = df[['BHK', 'AREA', 'YEARS', 'BATH', 'FLOOR', 'LAT', 'LONG', 'MD_AIRPORT']].copy()
dfy = df[['PRICE']].copy()

x_train, x_test, y_train, y_test = train_test_split(dfx,dfy,test_size = 0.3)

model = RandomForestRegressor(n_estimators = 100, max_features = 'sqrt')
model.fit(x_train, y_train.values.ravel())
ans=model.predict(x_test)

nytest = y_test.as_matrix()

result_r2 = r2_score(nytest, ans)