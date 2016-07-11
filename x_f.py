import numpy as np
from numpy import sin, cos
from params import *


def get_c1(q, q_d, psi=0):
	x,y,a,b,_ = q
	x_d,y_d,a_d,b_d,_ = q_d

	return np.array([
		m1 + m2,

		0,

		-L1*m1*sin(g0 + a + a),

		- L1*m1*sin(g0 + a + a) \
		- L2*m1*sin(g0 + a) \
		- L2*eps*m2*sin(g0 + a) \
		- L3*m1*sin(a) - L3*m2*sin(a) 
		])

def get_d1(q, q_d, psi=0):
	x,y,a,b,_ = q
	x_d,y_d,a_d,b_d,_ = q_d
	return - L1*m1*cos(g0 + a + a)*a_d**2 \
		- 2*L1*m1*cos(g0 + a + a)*a_d*b_d \
		- L1*m1*cos(g0 + a + a)*b_d**2 \
		- L2*eps*m2*cos(g0 + a)*b_d**2 \
		- L2*m1*cos(g0 + a)*b_d**2 \
		- L3*m1*cos(a)*b_d**2 \
		- L3*m2*cos(a)*b_d**2 
