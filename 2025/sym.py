import sympy as sp

# Define the variable
r, M = sp.symbols('r M')

# Define a fractional term, e.g., (r^2 + 1)/(r - 1)
E_c = (r-2*M)**2/(r*(r-3*M))
# Differentiate
dfdr = sp.diff(E_c, r)
# print("First derivative: ",dfdr)
sol = sp.solve(dfdr, r)

dfdrdr = sp.diff(dfdr,r)
second_sol  =sp.solve(dfdrdr, r)
# Display result
print("Second derivative solutions: ", second_sol)
print()
