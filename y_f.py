import numpy as np
from numpy import sin, cos
from params import *


def get_c2(q, q_d, psi=0):
	x,y,a,b,_ = q
	x_d,y_d,a_d,b_d,_ = q_d

	return np.array([
		0,

		m1 + m2

		- L1*m1*sin(g0 + a + b), 

		- L1*m1*sin(g0 + a + b) \ 
		+ L2*eps*m2*cos(g0 + b) \
		+ L2*m1*cos(g0 + b) \ 
		+ L3*m1*cos(b) \
		+ L3*m2*cos(b)
		])


def get_d2(q, q_d, psi=0):
	x,y,a,b,_ = q
	x_d,y_d,a_d,b_d,_ = q_d

	return Grav*m1 + Grav*m2 \
		- L1*m1*cos(g0 + a + b)*a_d**2 \
		- 2*L1*m1*cos(g0 + a + b)*a_d*b_d \
		- L1*m1*cos(g0 + a + b)*b_d**2 \
		- L2*eps*m2*sin(g0 + b)*b_d**2 \
		- L2*m1*sin(g0 + b)*b_d**2 \
		- L3*m1*sin(b)*b_d**2 \
		- L3*m2*sin(b)*b_d**2 
