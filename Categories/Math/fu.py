import numpy as np
from scipy.integrate import quad
# Number of terms to include in the series
n_terms = 10000  # Increase this number for a more accurate approximation

# Initialize the sum
pi_over_4_approx = 0

# Compute the series sum
for k in range(n_terms):
    pi_over_4_approx += (-1)**k / (2*k + 1)

# Print the result
print("Approximation of pi/4 using the series:")
print(pi_over_4_approx)

# Compare with the actual value of pi/4
actual_pi_over_4 = np.pi / 4
print("Actual value of pi/4:")
print(actual_pi_over_4)

# Calculate the error
error = abs(actual_pi_over_4 - pi_over_4_approx)
print("Error:")
print(error)

def f_t(t):
    t = t % (2 * np.pi)  # Bring t within the range [0, 2*pi)
    if 0 < t < np.pi:
        return 1
    else:
        return 0
# Compute the Fourier series coefficients
def compute_fourier_coefficients(f, L, n_terms):
    a0 = (1 / (2*L)) * quad(lambda t: f(t), -L, L)[0]
    an = []
    bn = []
    
    for n in range(1, n_terms + 1):
        an.append((1 / L) * quad(lambda t: f(t) * np.cos(n * t), -L, L)[0])
        bn.append((1 / L) * quad(lambda t: f(t) * np.sin(n * t), -L, L)[0])
    
    return a0, an, bn
# Compute the Fourier series sum at t = pi
L = np.pi
n_terms = 100  # Using more terms for better accuracy

# Compute the Fourier series coefficients
a0, an, bn = compute_fourier_coefficients(f_t, L, n_terms)

# Evaluate the Fourier series at t = pi
t = np.pi
series_sum_at_pi = a0 / 2 + sum(an[n-1] * (-1)**n for n in range(1, n_terms + 1))

print(series_sum_at_pi)
