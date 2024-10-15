import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

def marks_prediction(hrs):
    # Load the datasets correctly
    X = pd.read_csv('Linear_X_Train.csv')
    y = pd.read_csv('Linear_Y_Train.csv')

    # Convert data to numpy arrays
    X = X.values
    y = y.values

    # Train the linear regression model
    model = LinearRegression()
    model.fit(X, y)

    # Convert the input to a numpy array and reshape it
    X_test = np.array([[hrs]])

    # Return the predicted marks
    return model.predict(X_test)[0]
