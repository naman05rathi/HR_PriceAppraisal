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
from sklearn.svm import SVR
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.neural_network import MLPRegressor
from sklearn import linear_model



df = pd.read_csv("solution.csv")
scaler = MinMaxScaler()
df[['BHK', 'AREA', 'YEARS', 'BATH', 'FLOOR', 'LAT', 'LONG', 'MD_AIRPORT']] = scaler.fit_transform(df[['BHK', 'AREA', 'YEARS', 'BATH', 'FLOOR', 'LAT', 'LONG', 'MD_AIRPORT']])

dfx = df[['BHK', 'AREA', 'YEARS', 'BATH', 'FLOOR', 'LAT', 'LONG', 'MD_AIRPORT']].copy()
dfy = df[['PRICE']].copy()

models = [linear_model.Ridge (alpha = 0.1),
			linear_model.BayesianRidge(),
			linear_model.LogisticRegression(),
			KNeighborsRegressor(n_neighbors=6),
			DecisionTreeRegressor(max_depth=3,min_samples_split=3),
			MLPRegressor(hidden_layer_sizes=(100,), activation='relu')
			]

for model in models:
	x_train, x_test, y_train, y_test = train_test_split(dfx,dfy,test_size = 0.3)
	model.fit(x_train, y_train.values.ravel())
	ans=model.predict(x_test)

	nytest = y_test.as_matrix()

	result_r2 = r2_score(nytest, ans)