import numpy as np
from numpy import sin, cos
from params import *


def get_c1(q, q_d, psi=0):
	_,_,a,b,g = q
	_,_,a_d,b_d,g_d = q_d

	return np.array([ 

		I1 + 2*L1**2*m1*sin(a + b + g)**2,

		  2*L1**2*m1*sin(a + b + g)**2 \
		+ L1*L2*m1*sin(b + g)*sin(a + b + g) \
		- L1*L2*m1*sin(a + b + g)*cos(b + g) \
		+ L1*L3*m1*sin(a + b + g)*sin(b) \
		- L1*L3*m1*sin(a + b + g)*cos(b),

		  2*L1**2*m1*sin(a + b + g)**2 \
		+ L1*L2*m1*sin(b + g)*sin(a + b + g) \
		- L1*L2*m1*sin(a + b + g)*cos(b + g)
		])

def get_d1(q, q_d, psi=0):
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
		+ L1*L2*m1*sin(a + b + g)*cos(b + g)*b_d**2 \
		+ 2*L1*L2*m1*sin(a + b + g)*cos(b + g)*b_d*g_d \
		+ L1*L2*m1*sin(a + b + g)*cos(b + g)*g_d**2 \
		+ L1*L3*m1*sin(a + b + g)*sin(b)*b_d**2 \
		+ L1*L3*m1*sin(a + b + g)*cos(b)*b_d**2 \
		- L1*Grav*m1*sin(a + b + g) \
		+ dz*k1*z1*sin(a) - dz*k2*z2*sin(a) \
		+ k1*z0*z1*sin(psi)*sin(a) - k1*z1**2*sin(2*a)/2 \
		+ k2*z0*z2*sin(psi)*sin(a) - k2*z2**2*sin(2*a)/2 \
		+ miu1*a_d



