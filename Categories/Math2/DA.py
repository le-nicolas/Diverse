import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm

# Generate synthetic data
np.random.seed(0)
n = 100
X = np.linspace(0, 10, n)
beta0 = 2
beta1 = 3
sigma = 1.0
epsilon = np.random.normal(0, sigma, n)
Y = beta0 + beta1 * X + epsilon

# Create a pandas DataFrame
data = pd.DataFrame({'X': X, 'Y': Y})

# Visualize the data
plt.scatter(data['X'], data['Y'], label='Data points')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Synthetic Data')
plt.legend()
plt.show()

# Add a constant to the predictor variable (for the intercept term)
X_with_const = sm.add_constant(data['X'])

# Fit the regression model
model = sm.OLS(data['Y'], X_with_const).fit()

# Print the summary of the regression analysis
print(model.summary())

# Generate new data for prediction
X_new = np.linspace(0, 10, 100)
X_new_with_const = sm.add_constant(X_new)

# Predict mean response and prediction intervals
mean_pred = model.predict(X_new_with_const)
pred_int = model.get_prediction(X_new_with_const).summary_frame(alpha=0.05)

# Visualize the results
plt.scatter(data['X'], data['Y'], label='Data points')
plt.plot(X_new, mean_pred, label='Mean prediction', color='red')
plt.fill_between(X_new, pred_int['obs_ci_lower'], pred_int['obs_ci_upper'], color='red', alpha=0.3, label='Prediction interval')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Regression Analysis')
plt.legend()
plt.show()
