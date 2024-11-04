import numpy as np
import matplotlib.pyplot as plt

# Base class for a thermodynamic process
class ThermodynamicProcess:
    def __init__(self, n, R):
        self.n = n  # number of moles
        self.R = R  # universal gas constant

    def process(self, V):
        raise NotImplementedError("Process method should be implemented by subclasses")

    def plot_process(self, V_range):
        P = self.process(V_range)
        plt.plot(V_range, P, label=self.__class__.__name__)
        plt.xlabel('Volume (m^3)')
        plt.ylabel('Pressure (Pa)')
        plt.title('PV Diagram for Different Processes')
        plt.legend()

# Class for Isothermal process (constant temperature)
class IsothermalProcess(ThermodynamicProcess):
    def __init__(self, n, R, T):
        super().__init__(n, R)
        self.T = T  # constant temperature

    def process(self, V):
        # Ideal gas law for isothermal process: P * V = n * R * T
        return (self.n * self.R * self.T) / V

# Class for Adiabatic process (no heat exchange, PV^gamma = constant)
class AdiabaticProcess(ThermodynamicProcess):
    def __init__(self, n, R, gamma):
        super().__init__(n, R)
        self.gamma = gamma  # adiabatic constant (specific heat ratio)

    def process(self, V):
        # Simplified adiabatic process: P * V^gamma = constant
        P_initial = 100000  # Initial pressure
        V_initial = 1       # Initial volume
        return P_initial * (V_initial / V) ** self.gamma

# Class for Isochoric process (constant volume)
class IsochoricProcess(ThermodynamicProcess):
    def __init__(self, n, R, T, V_constant):
        super().__init__(n, R)
        self.T = T  # constant temperature
        self.V_constant = V_constant  # constant volume

    def process(self, V):
        # Ideal gas law for isochoric process: P = n * R * T / V_constant
        return np.ones_like(V) * (self.n * self.R * self.T) / self.V_constant

# Now let's create objects for different processes and plot their PV diagrams
n = 1  # 1 mole of gas
R = 8.314  # universal gas constant

# Create objects for different processes
isothermal = IsothermalProcess(n, R, T=300)
adiabatic = AdiabaticProcess(n, R, gamma=1.4)
isochoric = IsochoricProcess(n, R, T=300, V_constant=2)

# Create a volume range for plotting
V_range = np.linspace(0.5, 10, 100)

# Plot all processes
plt.figure(figsize=(8, 6))
isothermal.plot_process(V_range)
adiabatic.plot_process(V_range)
isochoric.plot_process(V_range)
plt.show()
