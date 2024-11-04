import numpy as np
from sfepy import data_dir
from sfepy.discrete import (FieldVariable, Material, Integral, Function,
                            Equation, Equations, Problem)
from sfepy.terms import Term
from sfepy.mesh.mesh_generators import gen_lines
from sfepy.mesh.meshio import UserMeshIO
from sfepy.mesh.mesh import Mesh
from sfepy.solvers.ls import ScipyDirect
from sfepy.solvers.nls import Newton
from sfepy.postprocess.viewer import Viewer

# Define mesh
mesh = Mesh.from_file(data_dir + '/meshes/1d/bar.mesh')

# Define field variable
field = FieldVariable('temperature', 'scalars', mesh, 1)

# Define material (thermal conductivity)
kappa = Material('m', val=np.array([1.0]))

# Define integral
integral = Integral('i', order=2)

# Define function (source term)
def get_source(ts, coors, mode=None, **kwargs):
    val = np.ones(coors.shape[0])  # Constant source term
    return {'val': val}

source_term = Function('source', get_source)

# Define term (diffusion term)
term = Term.new('dw_diffusion(m.k, v, u)', integral, mesh, m=kappa, v=field.test_var, u=field)

# Define equation
equation = Equation(term1=term, term2=None, term3=None, term4=None)

# Define equations
equations = Equations([equation])

# Define problem
problem = Problem('heat_conduction', equations=equations)

# Define solver
solver = {
    'name': 'ls-nls',
    'kind': 'ls.scipy_direct',
    'method': 'auto',
    'i_max': 10,
}

# Define nonlinear solver
nls_status = {
    'i_max': 1,
}

# Solve the problem
status = problem.solve(solver, nls=nls_status)

# Get the solution
temperature = problem.get_variables()['temperature']

# Plot the solution
view = Viewer(temperature)
view()

