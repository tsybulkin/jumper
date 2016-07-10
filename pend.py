from sympy import symbols, cos, sin, diff
from sympy.physics.mechanics import dynamicsymbols
from sympy.physics.mechanics import LagrangesMethod, Lagrangian



g = 9.81
m = 0.100
L = 0.25
miu = 0.01 

def Lagrangian():
	a = dynamicsymbols('a')
	a_d = dynamicsymbols('a',1)

	return m/2*(L*a_d)**2 + m*g*L*cos(a), a


def LEq(L,a):
	LM = LagrangesMethod(L,[a])

	return LM.form_lagranges_equations()
