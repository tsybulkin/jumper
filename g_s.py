import numpy as np
from numpy import sin, cos
from params import *

def get_c3(q,q_d,psi=0):
	_,_,a,b,g = q
	_,_,a_d,b_d,g_d = q_d

	return np.array([

		  2*L1**2*m1*sin(a + b + g)**2 \
		+ L1*L2*m1*sin(b + g)*sin(a + b + g) \
		- L1*L2*m1*sin(a + b + g)*cos(b + g),

		  2*L1**2*m1*sin(a + b + g)**2 \
		+ I2 + L2**2*m1 + L2**2*eps**2*m2 \
		+ 2*L1*L2*m1*sin(b + g)*sin(a + b + g) \
		- 2*L1*L2*m1*sin(a + b + g)*cos(b + g) \
		+ L1*L3*m1*sin(a + b + g)*sin(b) \
		- L1*L3*m1*sin(a + b + g)*cos(b) \
		+ L2*L3*eps*m2*sin(b + g)*sin(b) \
		+ L2*L3*eps*m2*cos(b + g)*cos(b) \
		+ L2*L3*m1*sin(b + g)*sin(b) \
		+ L2*L3*m1*cos(b + g)*cos(b),

		  I1 + I2 + L2**2*m1 + L2**2*eps**2*m2 + L2**2*m1 \
		+ 2*L1**2*m1*sin(a + b + g)**2 \
		+ 2*L1*L2*m1*sin(b + g)*sin(a + b + g) \
		- 2*L1*L2*m1*sin(a + b + g)*cos(b + g) 
		])


def get_d3(q,q_d,psi=0):
	_,_,a,b,g = q
	_,_,a_d,b_d,g_d = q_d

	return L1**2*m1*sin(2*a + 2*b + 2*g)*a_d**2 \
		+ 2*L1**2*m1*sin(2*a + 2*b + 2*g)*a_d*b_d \
		+ 2*L1**2*m1*sin(2*a + 2*b + 2*g)*a_d*g_d \
		+ L1**2*m1*sin(2*a + 2*b + 2*g)*b_d**2 \
		+ 2*L1**2*m1*sin(2*a + 2*b + 2*g)*b_d*g_d \
		+ L1**2*m1*sin(2*a + 2*b + 2*g)*g_d**2 \
		+ L1*L2*m1*sin(b + g)*sin(a + b + g)*b_d**2 \
		+ 2*L1*L2*m1*sin(b + g)*sin(a + b + g)*b_d*g_d \
		+ L1*L2*m1*sin(b + g)*sin(a + b + g)*g_d**2 \
		+ L1*L2*m1*sin(b + g)*cos(a + b + g)*a_d**2 \
		+ 2*L1*L2*m1*sin(b + g)*cos(a + b + g)*a_d*b_d \
		+ 2*L1*L2*m1*sin(b + g)*cos(a + b + g)*a_d*g_d \
		+ L1*L2*m1*sin(b + g)*cos(a + b + g)*b_d**2 \
		+ 2*L1*L2*m1*sin(b + g)*cos(a + b + g)*b_d*g_d \
		+ L1*L2*m1*sin(b + g)*cos(a + b + g)*g_d**2 \
		+ L1*L2*m1*sin(a + b + g)*cos(b + g)*b_d**2 \
		+ 2*L1*L2*m1*sin(a + b + g)*cos(b + g)*b_d*g_d \
		+ L1*L2*m1*sin(a + b + g)*cos(b + g)*g_d**2 \
		- L1*L2*m1*cos(b + g)*cos(a + b + g)*a_d**2 \
		- 2*L1*L2*m1*cos(b + g)*cos(a + b + g)*a_d*b_d \
		- 2*L1*L2*m1*cos(b + g)*cos(a + b + g)*a_d*g_d \
		- L1*L2*m1*cos(b + g)*cos(a + b + g)*b_d**2 \
		- 2*L1*L2*m1*cos(b + g)*cos(a + b + g)*b_d*g_d \
		- L1*L2*m1*cos(b + g)*cos(a + b + g)*g_d**2 \
		+ L1*L3*m1*sin(a + b + g)*sin(b)*b_d**2 \
		+ L1*L3*m1*sin(a + b + g)*cos(b)*b_d**2 \
		- L1*Grav*m1*sin(a + b + g) \
		+ L2*L3*eps*m2*sin(b + g)*cos(b)*b_d**2 \
		- L2*L3*eps*m2*sin(b)*cos(b + g)*b_d**2 \
		+ L2*L3*m1*sin(b + g)*cos(b)*b_d**2 \
		- L2*L3*m1*sin(b)*cos(b + g)*b_d**2 \
		+ L2*eps*Grav*m2*cos(b + g) \
		+ L2*Grav*m1*cos(b + g) \
		+ da*k3*z3*sin(g) + k3*z3**2*sin(2*g)/2 \
		+ miu_g*g_d

