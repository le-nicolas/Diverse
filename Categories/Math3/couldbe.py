import pandas as pd
import numpy as np

np.random.seed(42)
num_samples = 200

# Simulating the dataset
data = pd.DataFrame({
    'Design_Flaw': np.random.choice([0, 1], num_samples),
    'Improper_Usage': np.random.choice([0, 1], num_samples),
    'Airflow_Issue': np.random.choice([0, 1], num_samples),
    'Environmental_Factor': np.random.choice([0, 1], num_samples),
    'Construction_Material': np.random.choice([0, 1], num_samples),
    'Misinterpreting_Efficiency': np.random.choice([0, 1], num_samples),
    'Outcome': np.random.choice([0, 1], num_samples)
})

# Checking the distribution of the target variable
print("Target variable distribution:\n", data['Outcome'].value_counts())

# Displaying the first few rows of the dataset
print(data.head())


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# Separate features and target
X = data.drop('Outcome', axis=1)
y = data['Outcome']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Standardize the features
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)


from sklearn.ensemble import RandomForestClassifier

# Define the model
model = RandomForestClassifier(random_state=42)

# Train the model
model.fit(X_train_scaled, y_train)

# Make predictions
y_pred = model.predict(X_test_scaled)


from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# Compute accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

# Compute the confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)

# Plot the confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt="d", cmap="Blues", xticklabels=['Negative', 'Positive'], yticklabels=['Negative', 'Positive'])
plt.xlabel('Predicted Label')
plt.ylabel('True Label')
plt.title('Confusion Matrix')
plt.show()

# Get classification report as dictionary
class_report = classification_report(y_test, y_pred, output_dict=True)

# Extract metrics for each class
metrics_df = pd.DataFrame(class_report).transpose()

# Plot precision, recall, and F1-score for each class
metrics_df.loc[['0', '1'], ['precision', 'recall', 'f1-score']].plot(kind='bar', figsize=(12, 6))
plt.title('Precision, Recall, and F1-Score for Each Class')
plt.xlabel('Class')
plt.ylabel('Score')
plt.ylim(0, 1)
plt.legend(loc='lower right')
plt.xticks(rotation=0)
plt.show()

# Print detailed classification report
print("Classification Report:\n", classification_report(y_test, y_pred))


