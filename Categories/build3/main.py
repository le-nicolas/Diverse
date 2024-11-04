# Let's define the function based on the relationship between fan size, speed, and horsepower.
# The formula will include speed (RPM) and size (diameter), considering their respective powers.
# For simplicity, we'll assume a baseline power requirement for a standard fan.

def fan_horsepower(diameter: float, speed: float, base_hp: float = 0.05) -> float:
    """
    Calculate the required horsepower for a fan based on its diameter and speed.
    - diameter: Fan blade diameter in inches.
    - speed: Fan speed in RPM.
    - base_hp: Baseline horsepower (for a small fan at a default speed).
    """
    # The power scales with the cube of the speed and the fifth power of the diameter
    hp = base_hp * (speed / 600) ** 3 * (diameter / 12) ** 5
    return hp

# Example: Calculate the horsepower for a fan with 24 inches diameter and 1200 RPM
fan_horsepower(24, 1200)
