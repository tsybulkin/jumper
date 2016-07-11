import numpy as np
from numpy import sin, cos
from params import *


def get_c3(q, q_d, psi=0):
	x,y,a,b,_ = q
	x_d,y_d,a_d,b_d,_ = q_d

	return np.array([

		- L1*m1*sin(g0 + a + b), # x

		- L1*m1*sin(g0 + a + b), # y

		I1 + 2*L1**2*m1*sin(g0 + a + b)**2, # a

		2*L1**2*m1*sin(g0 + a + b)**2 \ 
		+ L1*L2*m1*sin(g0 + b)*sin(g0 + a + b) \ 
		- L1*L2*m1*sin(g0 + a + b)*cos(g0 + b) \ 
		+ L1*L3*m1*sin(g0 + a + b)*sin(b) \ 
		- L1*L3*m1*sin(g0 + a + b)*cos(b) 
		])


def get_d3(q, q_d, psi=0):
	x,y,a,b,_ = q
	x_d,y_d,a_d,b_d,_ = q_d
	return -Grav*L1*m1*sin(g0 + a + b) \
		+ L1**2*m1*sin(2*g0 + 2*a + 2*b)*a_d**2 \
		+ 2*L1**2*m1*sin(2*g0 + 2*a + 2*b)*a_d*b_d \
		+ L1**2*m1*sin(2*g0 + 2*a + 2*b)*b_d**2 \
		+ L1*L2*m1*sin(g0 + b)*sin(g0 + a + b)*b_d**2 \
		+ L1*L2*m1*sin(g0 + a + b)*cos(g0 + b)*b_d**2 \
		+ L1*L3*m1*sin(g0 + a + b)*sin(b)*b_d**2 \
		+ L1*L3*m1*sin(g0 + a + b)*cos(b)*b_d**2 \
		+ dz*k1*z1*sin(a) - dz*k2*z2*sin(a) \
		+ k1*z0*z1*sin(psi)*sin(a) - k1*z1**2*sin(2*a)/2 \
		+ k2*z0*z2*sin(psi)*sin(a) - k2*z2**2*sin(2*a)/2
