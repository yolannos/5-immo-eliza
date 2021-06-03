import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.pipeline import make_pipeline
from sklearn.compose import make_column_selector, make_column_transformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder, PolynomialFeatures, Normalizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.impute import SimpleImputer
import seaborn as sns

from xgboost import XGBRegressor
import xgboost as xgb

from sklearn.ensemble import BaggingRegressor

import pickle

# Download the dataset
data = pd.read_csv("https://raw.githubusercontent.com/SamuelD005/challenge-regression/development/Data8.csv", sep=",")
data.head()

#Drop unused columns
X = data.drop(["Price","Unnamed: 0","PriceperMeter"] , axis = 1)
y = data["Price"].apply(lambda x: np.log1p(x))

#Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=41)

#Define the features cat vs num
numerical_features = ['Locality', 'Number of rooms', 'Area', 'Terrace Area', 'Garden Area', 'Surface of the land']
categorial_features = ['Type of property','Fully equipped kitchen', 'Furnished', 'Open fire',
                       'Swimming pool', 'State of the building', 'Province', 'Region','Number of facades']


#Define the transformation of both type of features
numerical_pipeline = make_pipeline(SimpleImputer(), StandardScaler())
categorial_pipeline = make_pipeline(SimpleImputer(strategy="most_frequent"), 
                                   OneHotEncoder())

#Apply the transformation on the features based on the definition above
preprocessor = make_column_transformer((numerical_pipeline, numerical_features),
                       (categorial_pipeline, categorial_features))


# #######XGBoost########
# #Preprocessing of the date and definition of the model
# model = make_pipeline(preprocessor, XGBRegressor())
# #Training of the model
# XGBoost_model = model.fit(X_train, y_train)
# #Score of the model
# XGBoost_model.score(X_test, y_test)
# #######################End XGBoost


#######Bagging XGBoost########
#Preprocessing of the date and definition of the model
BG = BaggingRegressor(base_estimator=XGBRegressor(), n_estimators= 10)
model = make_pipeline(preprocessor, BG)
#Training of the model
BG_model = model.fit(X_train, y_train)
#Score of the model
BG_model.score(X_test, y_test)

BG_model.predict(X_test)
#######################End Bagging-XGBoost


#Dumping of the models
# xg_file = "xgb_reg.pkl"
bg_file = "bg_reg.pkl"
# save
# pickle.dump(XGBoost_model, open(xg_file, "wb"))
pickle.dump(BG_model, open(bg_file, "wb"))