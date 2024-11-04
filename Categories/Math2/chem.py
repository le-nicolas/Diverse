import matplotlib.pyplot as plt

def plot_reaction(reactants, products):
    # Convert reactants and products into dictionaries
    reactant_dict = {}
    product_dict = {}
    
    for reactant in reactants:
        coeff, name = reactant.split(" ")
        reactant_dict[name] = int(coeff)
    
    for product in products:
        coeff, name = product.split(" ")
        product_dict[name] = int(coeff)
    
    # Determine common elements
    elements = list(set(reactant_dict.keys()).union(set(product_dict.keys())))
    elements.sort()  # Ensure consistent order of elements
    
    # Initialize stoichiometric coefficients
    reactant_coefficients = [reactant_dict.get(element, 0) for element in elements]
    product_coefficients = [-product_dict.get(element, 0) for element in elements]
    
    # Plotting
    fig, ax = plt.subplots()
    
    # Reactants
    ax.barh(range(len(elements)), reactant_coefficients, color='blue', label='Reactants')
    
    # Products
    ax.barh(range(len(elements)), product_coefficients, color='green', label='Products')
    
    # Ticks and labels
    ax.set_yticks(range(len(elements)))
    ax.set_yticklabels(elements)
    ax.invert_yaxis()  # Invert y-axis to have reactants at the top
    ax.set_xlabel('Coefficients')
    ax.set_title('Balanced Chemical Reaction')
    ax.legend()

    plt.show()

# Example: Reaction between hydrogen and oxygen to form water
reactants = ["2 H2", "1 O2"]
products = ["2 H2O"]

plot_reaction(reactants, products)
