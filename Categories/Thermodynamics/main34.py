import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score

# Hypothetical data: Temperature, Pressure, and Phase
data = {'Temperature': [0, 100, 150, 200, 374],
        'Pressure': [0.61, 101.3, 476, 1554, 22064],
        'Phase': ['Liquid', 'Vapor', 'Vapor', 'Vapor', 'Supercritical']}

# Create a DataFrame
df = pd.DataFrame(data)

# Encode the Phase as a numerical value
label_encoder = LabelEncoder()
df['Phase_Encoded'] = label_encoder.fit_transform(df['Phase'])

# Features (Temperature, Pressure) and target (Phase_Encoded)
X = df[['Temperature', 'Pressure']]
y = df['Phase_Encoded']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict using the test data
y_pred = model.predict(X_test)

# Evaluate the model accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy*100:.2f}%")

# Predict phase for a new point (example: Temp = 250°C, Pressure = 3000 kPa)
new_point = np.array([[250, 3000]])
predicted_phase = model.predict(new_point)

# Get the phase label
predicted_phase_label = label_encoder.inverse_transform(predicted_phase)
print(f"Predicted Phase: {predicted_phase_label[0]}")
