import numpy as np
from numpy import sin, cos
from params import *

def get_c2(q, q_d,psi=0):
	a,b,gama = q
	a_d,b_d,gama_d = q_d

	return np.array([

		  2*L1**2*m1*sin(a + b + gama)**2 \
		+ L1*L2*m1*sin(b + gama)*sin(a + b + gama) \
		- L1*L2*m1*sin(a + b + gama)*cos(b + gama) \
		+ L1*L3*m1*sin(a + b + gama)*sin(b) \
		- L1*L3*m1*sin(a + b + gama)*cos(b),

		I1 + I2 + L2**2*eps**2*m2 + L2**2*m1 + L3**2*m1 + L3**2*m2 \
		+ 2*L1**2*m1*sin(a + b + gama)**2 \
		+ 2*L1*L2*m1*sin(b + gama)*sin(a + b + gama) \
		- 2*L1*L2*m1*sin(a + b + gama)*cos(b + gama) \
		+ 2*L1*L3*m1*sin(a + b + gama)*sin(b) \
		- 2*L1*L3*m1*sin(a + b + gama)*cos(b) \
		+ 2*L2*L3*eps*m2*sin(b + gama)*sin(b) \
		+ 2*L2*L3*eps*m2*cos(b + gama)*cos(b) \
		+ 2*L2*L3*m1*sin(b + gama)*sin(b) \
		+ 2*L2*L3*m1*cos(b + gama)*cos(b), 

		I2 + L2**2*eps**2*m2 + L2**2*m1 \
		+ 2*L1**2*m1*sin(a + b + gama)**2 \
		+ 2*L1*L2*m1*sin(b + gama)*sin(a + b + gama) \
		- 2*L1*L2*m1*sin(a + b + gama)*cos(b + gama) \
		+ L1*L3*m1*sin(a + b + gama)*sin(b) \
		- L1*L3*m1*sin(a + b + gama)*cos(b) \
		+ L2*L3*eps*m2*sin(b + gama)*sin(b) \
		+ L2*L3*eps*m2*cos(b + gama)*cos(b) \
		+ L2*L3*m1*sin(b + gama)*sin(b) \
		+ L2*L3*m1*cos(b + gama)*cos(b) 
	])


def get_d2(q, q_d, psi=0):
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
		+ L1*L2*m1*sin(b + gama)*cos(a + b + gama)*a_d**2 \
		+ 2*L1*L2*m1*sin(b + gama)*cos(a + b + gama)*a_d*b_d \
		+ 2*L1*L2*m1*sin(b + gama)*cos(a + b + gama)*a_d*gama_d \
		+ L1*L2*m1*sin(b + gama)*cos(a + b + gama)*b_d**2 \
		+ 2*L1*L2*m1*sin(b + gama)*cos(a + b + gama)*b_d*gama_d \
		+ L1*L2*m1*sin(b + gama)*cos(a + b + gama)*gama_d**2 \
		+ L1*L2*m1*sin(a + b + gama)*cos(b + gama)*b_d**2 \
		+ 2*L1*L2*m1*sin(a + b + gama)*cos(b + gama)*b_d*gama_d \
		+ L1*L2*m1*sin(a + b + gama)*cos(b + gama)*gama_d**2 \
		- L1*L2*m1*cos(b + gama)*cos(a + b + gama)*a_d**2 \
		- 2*L1*L2*m1*cos(b + gama)*cos(a + b + gama)*a_d*b_d \
		- 2*L1*L2*m1*cos(b + gama)*cos(a + b + gama)*a_d*gama_d \
		- L1*L2*m1*cos(b + gama)*cos(a + b + gama)*b_d**2 \
		- 2*L1*L2*m1*cos(b + gama)*cos(a + b + gama)*b_d*gama_d \
		- L1*L2*m1*cos(b + gama)*cos(a + b + gama)*gama_d**2 \
		+ L1*L3*m1*sin(a + b + gama)*sin(b)*b_d**2 \
		+ L1*L3*m1*sin(a + b + gama)*cos(b)*b_d**2 \
		+ L1*L3*m1*sin(b)*cos(a + b + gama)*a_d**2 \
		+ 2*L1*L3*m1*sin(b)*cos(a + b + gama)*a_d*b_d \
		+ 2*L1*L3*m1*sin(b)*cos(a + b + gama)*a_d*gama_d \
		+ L1*L3*m1*sin(b)*cos(a + b + gama)*b_d**2 \
		+ 2*L1*L3*m1*sin(b)*cos(a + b + gama)*b_d*gama_d \
		+ L1*L3*m1*sin(b)*cos(a + b + gama)*gama_d**2 \
		- L1*L3*m1*cos(a + b + gama)*cos(b)*a_d**2 \
		- 2*L1*L3*m1*cos(a + b + gama)*cos(b)*a_d*b_d \
		- 2*L1*L3*m1*cos(a + b + gama)*cos(b)*a_d*gama_d \
		- L1*L3*m1*cos(a + b + gama)*cos(b)*b_d**2 \
		- 2*L1*L3*m1*cos(a + b + gama)*cos(b)*b_d*gama_d \
		- L1*L3*m1*cos(a + b + gama)*cos(b)*gama_d**2 \
		- L1*g*m1*sin(a + b + gama) \
		- 2*L2*L3*eps*m2*sin(b + gama)*cos(b)*b_d*gama_d \
		- L2*L3*eps*m2*sin(b + gama)*cos(b)*gama_d**2 \
		+ 2*L2*L3*eps*m2*sin(b)*cos(b + gama)*b_d*gama_d \
		+ L2*L3*eps*m2*sin(b)*cos(b + gama)*gama_d**2 \
		- 2*L2*L3*m1*sin(b + gama)*cos(b)*b_d*gama_d \
		- L2*L3*m1*sin(b + gama)*cos(b)*gama_d**2 \
		+ 2*L2*L3*m1*sin(b)*cos(b + gama)*b_d*gama_d \
		+ L2*L3*m1*sin(b)*cos(b + gama)*gama_d**2 \
		+ L2*eps*g*m2*cos(b + gama) + L2*g*m1*cos(b + gama) \
		+ L3*g*m1*cos(b) + L3*g*m2*cos(b)
