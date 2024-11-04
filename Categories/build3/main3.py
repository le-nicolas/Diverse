def first_law_of_thermodynamics(Q, W):
    """
    Calculate the change in internal energy using the First Law of Thermodynamics.
    ΔU = Q - W
    Where:
    ΔU = change in internal energy (Joules)
    Q = heat added to the system (Joules)
    W = work done by the system (Joules)
    """
    delta_U = Q - W
    return delta_U

# Example values:
heat_added = float(input("Enter the heat added to the system (Q) in Joules: "))  # input in Joules
work_done = float(input("Enter the work done by the system (W) in Joules: "))  # input in Joules

# Calculate change in internal energy
change_in_internal_energy = first_law_of_thermodynamics(heat_added, work_done)

print(f"The change in internal energy (ΔU) of the system is: {change_in_internal_energy:.2f} Joules")
