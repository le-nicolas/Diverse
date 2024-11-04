# Let's define a new function using the detailed formula: HP = (Q * P) / (6356 * η)
def detailed_fan_horsepower(airflow: float, pressure: float, efficiency: float = 0.6) -> float:
    """
    Calculate the required horsepower for a fan based on airflow, pressure, and efficiency.
    - airflow: Airflow in cubic feet per minute (CFM).
    - pressure: Pressure in inches of water gauge (inH2O).
    - efficiency: Mechanical efficiency of the fan (default 0.6).
    """
    conversion_factor = 6356  # unit conversion factor
    hp = (airflow * pressure) / (conversion_factor * efficiency)
    return hp

# Example: Calculate the horsepower for a fan with 1200 CFM airflow, 1.5 inH2O pressure, and 60% efficiency
detailed_fan_horsepower(1200, 1.5)
