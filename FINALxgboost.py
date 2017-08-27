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
import xgboost as xgb
from xgboost.sklearn import XGBRegressor
from sklearn import cross_validation, metrics
from sklearn.grid_search import GridSearchCV 



df = pd.read_csv("Season_1_Finale.csv")
scaler = MinMaxScaler()
df[['BHK', 'AREA', 'YEARS', 'BATH', 'FLOOR', 'LAT', 'LONG', 'MD_AIRPORT']] = scaler.fit_transform(df[['BHK', 'AREA', 'YEARS', 'BATH', 'FLOOR', 'LAT', 'LONG', 'MD_AIRPORT']])

dfx = df[['BHK', 'AREA', 'YEARS', 'BATH', 'FLOOR', 'LAT', 'LONG', 'MD_AIRPORT']].copy()
dfy = df[['PRICE']].copy()


x_train, x_test, y_train, y_test = train_test_split(dfx,dfy,test_size = 0.3)

model = XGBRegressor(learning_rate =0.1,
	seed=0,
	subsample=0.7,
	colsample_bytree=0.8,
	objective='reg:gamma',
	max_depth=3,
	min_child_weight=3
	)
model.fit(x_train, y_train.values.ravel())
ans=model.predict(x_test)

nytest = y_test.as_matrix()

result_r2 = r2_score(nytest, ans)