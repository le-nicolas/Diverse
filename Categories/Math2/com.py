import cmath

# Example 1: Addition and Subtraction
z1 = complex(3, 4)  # 3 + 4i
z2 = complex(1, -2) # 1 - 2i

z_add = z1 + z2
z_sub = z1 - z2

print(f"Addition: {z1} + {z2} = {z_add}")
print(f"Subtraction: {z1} - {z2} = {z_sub}")

# Example 2: Multiplication and Division
z_mul = z1 * z2
z_div = z1 / z2

print(f"Multiplication: {z1} * {z2} = {z_mul}")
print(f"Division: {z1} / {z2} = {z_div}")

# Example 3: Roots of Complex Numbers
z = complex(3, 4)  # 3 + 4i

roots = [cmath.exp(cmath.log(z) / 2 + 2j * cmath.pi * k / 2) for k in range(2)]
print(f"Square roots of {z}: {roots}")
