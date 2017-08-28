import pandas as pd
from pandas import DataFrame
from sklearn.cross_validation import train_test_split
import numpy as np
from numpy import ndarray
from sklearn.metrics import r2_score
from sklearn.preprocessing import MinMaxScaler
import xgboost as xgb
from sklearn.grid_search import GridSearchCV



df = pd.read_csv("Season_1_Finale.csv")
scaler = MinMaxScaler()
df[['BHK', 'AREA', 'YEARS', 'BATH', 'FLOOR', 'LAT', 'LONG', 'MD_AIRPORT']] = scaler.fit_transform(df[['BHK', 'AREA', 'YEARS', 'BATH', 'FLOOR', 'LAT', 'LONG', 'MD_AIRPORT']])

dfx = df[['BHK', 'AREA', 'YEARS', 'BATH', 'FLOOR', 'LAT', 'LONG', 'MD_AIRPORT']].copy()
dfy = df[['PRICE']].copy()
x_train, x_test, y_train, y_test = train_test_split(dfx,dfy,test_size = 0.2)

cv_params = {'max_depth': [3,5,7], 'min_child_weight': [1,3,5]}
ind_params = {'learning_rate': 0.1, 'n_estimators': 1000, 'seed':0, 'subsample': 0.8, 'colsample_bytree': 0.8, 'objective': 'reg:gamma'}
optimized_GBM = GridSearchCV(xgb.XGBRegressor(**ind_params), cv_params, scoring = 'accuracy', cv = 5, n_jobs = -1)
optimized_GBM.fit(x_train, y_train)

GridSearchCV(cv=5, error_score='raise',
       estimator=XGBRegressor(base_score=0.5, colsample_bylevel=1, colsample_bytree=0.8,
       gamma=0, learning_rate=0.1, max_delta_step=0, max_depth=3,
       min_child_weight=1, missing=None, n_estimators=1000, nthread=-1,
       objective='reg:gamma', reg_alpha=0, reg_lambda=1,
       scale_pos_weight=1, seed=0, silent=True, subsample=0.8),
       fit_params={}, iid=True, n_jobs=-1,
       param_grid={'min_child_weight': [1, 3, 5], 'max_depth': [3, 5, 7]},
       pre_dispatch='2*n_jobs', refit=True, scoring='accuracy', verbose=0)

print optimized_GBM.grid_scores_