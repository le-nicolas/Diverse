# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Hypothetical dataset of house prices
# Features: [Square Footage, Number of Bedrooms, Number of Bathrooms]
X = np.array([[1500, 3, 2],
              [1800, 4, 3],
              [2400, 4, 2],
              [3000, 5, 4],
              [3500, 5, 3],
              [1200, 2, 1],
              [2000, 3, 3],
              [1600, 3, 2],
              [2800, 4, 3],
              [3000, 4, 3]])

# Target: Prices of the houses in dollars (in thousands)
y = np.array([300, 400, 450, 550, 600, 200, 350, 320, 500, 520])

# Split the data into training and testing sets (80% train, 20% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create the linear regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Predict prices for the test set
y_pred = model.predict(X_test)

# Evaluate the model (Mean Squared Error)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.2f}")

# Print predicted vs actual house prices
for i in range(len(y_test)):
    print(f"Predicted: {y_pred[i]:.2f}k, Actual: {y_test[i]:.2f}k")

# Visualize the results (for one feature, square footage)
plt.scatter(X_test[:, 0], y_test, color='blue', label='Actual Prices')
plt.scatter(X_test[:, 0], y_pred, color='red', label='Predicted Prices')
plt.xlabel('Square Footage')
plt.ylabel('House Price (in thousands)')
plt.title('Actual vs Predicted House Prices')
plt.legend()
plt.show()
