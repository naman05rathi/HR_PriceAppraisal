# Price Appraisal of property in Delhi NCR
## HR Real Value, Ghaziabad, UP
### Summer Internship Project, June-July, 2017
For any queries, please raise an issue.


## Description
This project is a price prediction system for resendential property prices in Delhi NCR.
Locations covered are Delhi, Ghaziabad, Noida, Greater Noida, Faridabad, Gurugram(Gurgaon).


## Dataset
Data is collected from the websites selling property in India, specially in Delhi. Python and Ruby scripts are use to collect data.
Price is predicted using features like BHK, Latitude, Longitude, Area, Years Old, Bathrooms, Floor, Distance from Nearest Metro Station and IGI Airport.


## File Description
1. Scripting folder contains two scripts(one in Python, one in Ruby) that are used for website scraping.
2. Airport.py: script for calculating distance of property from Indira Gandhi International Airport.
3. metro.py: script for calculating distance of property from nearest Metro distance.
4. lat_long.py: script for converting Address of property to latitude and longitude.
5. FINALregressor.py: script used for predicting prices. It contains regression models -  Ridge Regression, Bayesian Ridge Regression, kNN Regression, Decision Tree Regression, Multi Layer Perceptron Regression.
6. FINALsvr.py: Support Vector Regressor for price prediction.
7. FINALrandom.py: Random Forest Regressor for price prediction.
8. xgboost_gridsearch.py: GridSearchCV to tune parameters for XGBoost Regression model.
9. FINALxgboost.py: XGBoost Regressor for price prediction.


## Python Libraries
1. numpy
2. pandas
3. geopy
4. sklearn
5. xgboost


## Results
### Regression Models Result

Model  | Median  | Standard Deviation
------------- | ------------- | -------------
Ridge  | 0.5663  | 0.0246
Bayesian Ridge  | 0.5734  | 0.0213
kNN  | 0.7077  | 0.027
Decision Tree  | 0.63  | 0.0199
Neural Net (MLP)  | 0.6556  | 0.0321
Random Forest  | 0.7726  | 0.0246
XGBoost  | 0.7386  | 0.05217


### GridSearchCV Result

Maximum Depth  | Min Child Weight  | Mean  | Standard Deviation
------------- | ------------- | ------------- | -------------
3  | 1  | 0.7376  | 0.05975
3  | 3  | 0.73856  | 0.05217
3  | 5  | 0.73351  | 0.05993
5  | 1  | 0.73014  | 0.04219
5  | 3  | 0.73267  | 0.04214
5  | 5  | 0.73632  | 0.04516
7  | 1  | 0.72185  | 0.04562
7  | 3  | 0.71809  | 0.04393
7  | 5  | 0.71722  | 0.04400
