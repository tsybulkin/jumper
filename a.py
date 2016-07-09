import numpy as np
from numpy import sin, cos
from params import *


def get_c1(q, q_d, psi=0):
	a,b,gama = q
	a_d,b_d,gama_d = q_d

	return np.array([ I1 + 2*L1**2*m1*sin(a + b + gama)**2,

					  2*L1**2*m1*sin(a + b + gama)**2 \
					+ L1*L2*m1*sin(b + gama)*sin(a + b + gama) \
					- L1*L2*m1*sin(a + b + gama)*cos(b + gama) \
					+ L1*L3*m1*sin(a + b + gama)*sin(b) \
					- L1*L3*m1*sin(a + b + gama)*cos(b),

					  2*L1**2*m1*sin(a + b + gama)**2 \
					+ L1*L2*m1*sin(b + gama)*sin(a + b + gama) \
					- L1*L2*m1*sin(a + b + gama)*cos(b + gama)
		])

def get_d1(q, q_d, psi=0):
	a,b,gama = q
	a_d,b_d,gama_d = q_d
	
	return L1**2*m1*sin(2*a + 2*b + 2*gama)*a_d**2 \
		+ 2*L1**2*m1*sin(2*a + 2*b + 2*gama)*a_d*b_d \
		+ 2*L1**2*m1*sin(2*a + 2*b + 2*gama)*a_d*gama_d \
		+ L1**2*m1*sin(2*a + 2*b + 2*gama)*b_d**2 \
		+ 2*L1**2*m1*sin(2*a + 2*b + 2*gama)*b_d*gama_d \
		+ L1**2*m1*sin(2*a + 2*b + 2*gama)*gama_d**2 \
		+ L1*L2*m1*sin(b + gama)*sin(a + b + gama)*b_d**2 \
		+ 2*L1*L2*m1*sin(b + gama)*sin(a + b + gama)*b_d*gama_d \
		+ L1*L2*m1*sin(b + gama)*sin(a + b + gama)*gama_d**2 \
		+ L1*L2*m1*sin(a + b + gama)*cos(b + gama)*b_d**2 \
		+ 2*L1*L2*m1*sin(a + b + gama)*cos(b + gama)*b_d*gama_d \
		+ L1*L2*m1*sin(a + b + gama)*cos(b + gama)*gama_d**2 \
		+ L1*L3*m1*sin(a + b + gama)*sin(b)*b_d**2 \
		+ L1*L3*m1*sin(a + b + gama)*cos(b)*b_d**2 \
		- L1*g*m1*sin(a + b + gama) + dz*k1*z1*sin(a) - dz*k2*z2*sin(a) \
		+ k1*z0*z1*sin(psi)*sin(a) - k1*z1**2*sin(2*a)/2 + k2*z0*z2*sin(psi)*sin(a) \
		- k2*z2**2*sin(2*a)/2 \
		+ miu1*a_d


