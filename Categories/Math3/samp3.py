import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Simulate loading the data
data = pd.DataFrame({
    'Temperature': [300, 250, 320, 270, 280],
    'Airflow': [1.5, 1.2, 1.7, 1.3, 1.4],
    'Fuel Moisture': [12, 20, 15, 18, 14],
    'Fuel Type': ['wood', 'charcoal', 'wood', 'wood', 'charcoal'],
    'Combustion Chamber Insulation': ['high', 'low', 'medium', 'high', 'medium'],
    'Environmental Temperature': [20, 15, 22, 18, 19],
    'Wind Speed': [3, 5, 2, 4, 3],
    'Operator Experience': ['experienced', 'novice', 'experienced', 'novice', 'experienced'],
    'Outcome': [0, 1, 0, 1, 0]
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
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

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
