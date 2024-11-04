import pandas as pd
import numpy as np
import statsmodels.api as sm
from statsmodels.formula.api import ols
import seaborn as sns
import matplotlib.pyplot as plt


# Define the design matrix for a 2x2 factorial design
design_matrix = pd.DataFrame({
    'A': [-1, 1, -1, 1],
    'B': [-1, -1, 1, 1]
})

# Display the design matrix
print("Design Matrix:")
print(design_matrix)

# Simulate the response variable Y
np.random.seed(0)
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
print("\nChecking for NaN or inf values:")
print(design_matrix.isnull().sum())  # Check for NaN values
print(np.isfinite(design_matrix).all())  # Check for inf values

# Fit the factorial model
model = ols('Y ~ A * B', data=design_matrix).fit()

# Perform ANOVA
anova_table = sm.stats.anova_lm(model, typ=2)
print("\nANOVA Table:")
print(anova_table)

# Display the regression summary
print("\nRegression Summary:")
print(model.summary())

# Create interaction plot
sns.interaction_plot(x=design_matrix['A'], 
                     trace=design_matrix['B'], 
                     response=design_matrix['Y'], 
                     colors=['red', 'blue'])

plt.xlabel('Factor A')
plt.ylabel('Response Y')
plt.title('Interaction Plot')
plt.show()

# Create main effect plots
sns.catplot(x='A', y='Y', kind='point', data=design_matrix)
plt.xlabel('Factor A')
plt.ylabel('Response Y')
plt.title('Main Effect Plot for Factor A')
plt.show()

sns.catplot(x='B', y='Y', kind='point', data=design_matrix)
plt.xlabel('Factor B')
plt.ylabel('Response Y')
plt.title('Main Effect Plot for Factor B')
plt.show()
