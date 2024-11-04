import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.formula.api import ols
import seaborn as sns
import matplotlib.pyplot as plt

# Define the design matrix for a 2x2 factorial design
design_matrix = pd.DataFrame({
    'A': [-1, 0, -1, 0],
    'B': [-1, 0, 0, 1]
})

# Display the design matrix
print("Design Matrix:")
print(design_matrix)

# Simulate the response variable Y
np.random.seed()
beta0 = 10
betaA = 3
betaB = 2
betaAB = 1.5
sigma = 1.0

design_matrix['Y'] = (beta0 + 
                      betaA * design_matrix['A'] + 
                      betaB * design_matrix['B'] + 
                      betaAB * design_matrix['A'] * design_matrix['B'] + 
                      np.random.normal(0, sigma, design_matrix.shape[0]))

# Display the design matrix with response variable
print("\nDesign Matrix with Response:")
print(design_matrix)

# Check for NaN or inf values in the data
print("\nInitial Check for NaN or inf values:")
print("Is NaN present?:\n", design_matrix.isna().sum())  # Check for NaN values
print("Is finite:\n", np.isfinite(design_matrix).all())  # Check for inf values

# Handling NaN or inf values
# Replace inf with NaN and drop rows with NaN values
design_matrix.replace([np.inf, -np.inf], np.nan, inplace=True)
design_matrix.dropna(inplace=True)

# Verbose display of cleaned data
print("\nCleaned Data:")
print(design_matrix)

# Check again to ensure no NaNs or infs are present
print("\nAfter handling, checking for NaN or inf values again:")
print("Is NaN present?:\n", design_matrix.isna().sum())  # Check for NaN values
print("Is finite:\n", np.isfinite(design_matrix).all())  # Check for inf values

# Ensure no zero variance in the independent variables
print("\nVariance of Independent Variables:")
print(design_matrix[['A', 'B']].var())

if design_matrix[['A', 'B']].var().min() == 0:
    raise ValueError("Independent variables must have non-zero variance")

# Fit the factorial model
print("\nFitting the model...")
model = ols('Y ~ A * B', data=design_matrix).fit()

# Perform ANOVA
print("\nPerforming ANOVA...")
anova_table = sm.stats.anova_lm(model, typ=2)
print("\nANOVA Table:")
print(anova_table)

# Display the regression summary
print("\nRegression Summary:")
print(model.summary())

# Create interaction plot
sns.interaction_plot(x=design_matrix['A'], 
                     trace='B', 
                     response=design_matrix['Y'], 
                     colors=['red', 'blue'])

plt.xlabel('Factor A')
plt.ylabel('Response Y')
plt.title('Interaction Plot')

# Create main effect plots
sns.catplot(x='A', y='Y', kind='point', data=design_matrix)
plt.xlabel('Factor A')
plt.ylabel('Response Y')
plt.title('Main Effect Plot for Factor A')

sns.catplot(x='B', y='Y', kind='point', data=design_matrix)
plt.xlabel('Factor B')
plt.ylabel('Response Y')
plt.title('Main Effect Plot for Factor B')

plt.show()
