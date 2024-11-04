from sklearn.linear_model import LinearRegression

# Hypothetical data: Temperature and Pressure
data = {'Temperature': [100, 150, 200, 250, 300],
        'Pressure': [101.3, 150, 200, 250, 300]}
df = pd.DataFrame(data)

# Features and target
X = df[['Temperature']]
y = df['Pressure']

# Train a linear regression model
lin_reg = LinearRegression()
lin_reg.fit(X, y)

# Predict Pressure at 275°C
predicted_pressure = lin_reg.predict([[275]])
print(f"Predicted Pressure: {predicted_pressure[0]} kPa")
