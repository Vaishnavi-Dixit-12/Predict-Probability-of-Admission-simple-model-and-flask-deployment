# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

dataset = pd.read_csv('Admission_Predict.csv')
for col in dataset.columns:
    if ' ' in col:
        dataset = dataset.rename(columns={col:col.replace(' ','_')})
dataset = dataset.drop(['Serial_No.'], axis=1)

X = dataset.drop('Chance_of_Admit_',axis='columns')
y = dataset['Chance_of_Admit_']

regressor = LinearRegression(normalize=True)
regressor.fit(X, y)

# Saving model to disk
pickle.dump(regressor, open('model.pkl','wb'))

# Loading model to compare the results
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[337, 118, 4, 4.5, 4.5, 9.65, 1]]))

