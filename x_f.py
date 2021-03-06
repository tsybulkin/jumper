import numpy as np
from numpy import sin, cos
from params import *


def get_c1(q, q_d, psi=0):
	x,y,a,b,g = q
	x_d,y_d,a_d,b_d,_ = q_d

	return np.array([
		m1 + m2,

		0,

		- L1*m1*sin(g + a + b),

		- L1*m1*sin(g + a + b) \
		- L2*m1*sin(g + b) \
		- L2*eps*m2*sin(g + b) \
		- L3*m1*sin(b) - L3*m2*sin(b) 
		])

def get_d1(q, q_d, psi=0):
	x,y,a,b,g = q
	x_d,y_d,a_d,b_d,_ = q_d
	return - L1*m1*cos(g + a + b)*a_d**2 \
		- 2*L1*m1*cos(g + a + b)*a_d*b_d \
		- L1*m1*cos(g + a + b)*b_d**2 \
		- L2*eps*m2*cos(g + b)*b_d**2 \
		- L2*m1*cos(g + b)*b_d**2 \
		- L3*m1*cos(b)*b_d**2 \
		- L3*m2*cos(b)*b_d**2 

