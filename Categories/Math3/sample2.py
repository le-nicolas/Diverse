import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Simulate a larger dataset
np.random.seed(42)
num_samples = 100

data = pd.DataFrame({
    'Temperature': np.random.normal(300, 20, num_samples),
    'Airflow': np.random.normal(1.5, 0.3, num_samples),
    'Fuel Moisture': np.random.normal(15, 3, num_samples),
    'Fuel Type': np.random.choice(['wood', 'charcoal'], num_samples),
    'Combustion Chamber Insulation': np.random.choice(['high', 'medium', 'low'], num_samples),
    'Environmental Temperature': np.random.normal(20, 5, num_samples),
    'Wind Speed': np.random.normal(3, 1, num_samples),
    'Operator Experience': np.random.choice(['novice', 'experienced'], num_samples),
    'Outcome': np.random.choice([0, 1], num_samples)
})

# Separate features and target
X = data.drop('Outcome', axis=1)
y = data['Outcome']

# Identify categorical and numerical columns
categorical_cols = ['Fuel Type', 'Combustion Chamber Insulation', 'Operator Experience']
numerical_cols = ['Temperature', 'Airflow', 'Fuel Moisture', 'Environmental Temperature', 'Wind Speed']

# Preprocessing for numerical data
numerical_transformer = StandardScaler()

# Preprocessing for categorical data
categorical_transformer = OneHotEncoder(handle_unknown='ignore')

# Bundle preprocessing for numerical and categorical data
preprocessor = ColumnTransformer(
    transformers=[
        ('num', numerical_transformer, numerical_cols),
        ('cat', categorical_transformer, categorical_cols)
    ])

# Define the model
model = RandomForestClassifier(random_state=42)

# Create and evaluate the pipeline
clf = Pipeline(steps=[('preprocessor', preprocessor),
                      ('classifier', model)])

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Train the model
clf.fit(X_train, y_train)

# Make predictions
y_pred = clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred)

print("Accuracy:", accuracy)
print("Confusion Matrix:\n", conf_matrix)
print("Classification Report:\n", class_report)
