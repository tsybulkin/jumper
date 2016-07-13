import numpy as np
from numpy import sin, cos
from params import *


def get_c4(q, q_d, psi=0):
	x,y,a,b,g = q
	x_d,y_d,a_d,b_d,_ = q_d

	return np.array([

		- L1*m1*sin(g + a + b) \
		- L2*eps*m2*sin(g + b) \
		- L2*m1*sin(g + b) \
		- L3*m1*sin(b) \
		- L3*m2*sin(b), 

		- L1*m1*sin(g + a + b) \
		+ L2*eps*m2*cos(g + b) \
		+ L2*m1*cos(g + b) \
		+ L3*m1*cos(b) \
		+ L3*m2*cos(b),

		+ 2*L1**2*m1*sin(g + a + b)**2 \
		+ L1*L2*m1*sin(g + b)*sin(g + a + b) \
		- L1*L2*m1*sin(g + a + b)*cos(g + b) \
		+ L1*L3*m1*sin(g + a + b)*sin(b) \
		- L1*L3*m1*sin(g + a + b)*cos(b), 

		I1 + I2 + L3**2*m1 + L3**2*m2 \
		+ 2*L1**2*m1*sin(g + a + b)**2 \
		+ 2*L1*L2*m1*sin(g + b)*sin(g + a + b) \
		- 2*L1*L2*m1*sin(g + a + b)*cos(g + b) \
		+ 2*L1*L3*m1*sin(g + a + b)*sin(b) \
		+ L2**2*eps**2*m2*sin(g + b)**2 \
		+ L2**2*eps**2*m2*cos(g + b)**2 \
		+ L2**2*m1*sin(g + b)**2 \
		+ L2**2*m1*cos(g + b)**2 \
		+ 2*L2*L3*eps*m2*sin(g + b)*sin(b) \
		+ 2*L2*L3*eps*m2*cos(g + b)*cos(b) \
		+ 2*L2*L3*m1*sin(g + b)*sin(b) \
		+ 2*L2*L3*m1*cos(g + b)*cos(b) \
		- 2*L1*L3*m1*sin(g + a + b)*cos(b)
	])


def get_d4(q, q_d, psi=0):
	x,y,a,b,g = q
	x_d,y_d,a_d,b_d,_ = q_d

	return -Grav*L1*m1*sin(g + a + b) + Grav*L2*eps*m2*cos(g + b) \
		+ Grav*L2*m1*cos(g + b) + Grav*L3*m1*cos(b) + Grav*L3*m2*cos(b) \
		+ L1**2*m1*sin(2*g + 2*a + 2*b)*a_d**2 \
		+ 2*L1**2*m1*sin(2*g + 2*a + 2*b)*a_d*b_d \
		+ L1**2*m1*sin(2*g + 2*a + 2*b)*b_d**2 \
		+ L1*L2*m1*sin(g + b)*sin(g + a + b)*b_d**2 \
		+ L1*L2*m1*sin(g + b)*cos(g + a + b)*a_d**2 \
		+ 2*L1*L2*m1*sin(g + b)*cos(g + a + b)*a_d*b_d \
		+ L1*L2*m1*sin(g + b)*cos(g + a + b)*b_d**2 \
		+ L1*L2*m1*sin(g + a + b)*cos(g + b)*b_d**2 \
		- L1*L2*m1*cos(g + b)*cos(g + a + b)*a_d**2 \
		- 2*L1*L2*m1*cos(g + b)*cos(g + a + b)*a_d*b_d \
		- L1*L2*m1*cos(g + b)*cos(g + a + b)*b_d**2 \
		+ L1*L3*m1*sin(g + a + b)*sin(b)*b_d**2 \
		+ L1*L3*m1*sin(g + a + b)*cos(b)*b_d**2 \
		+ L1*L3*m1*sin(b)*cos(g + a + b)*a_d**2 \
		+ 2*L1*L3*m1*sin(b)*cos(g + a + b)*a_d*b_d \
		+ L1*L3*m1*sin(b)*cos(g + a + b)*b_d**2 \
		- L1*L3*m1*cos(g + a + b)*cos(b)*a_d**2 \
		- 2*L1*L3*m1*cos(g + a + b)*cos(b)*a_d*b_d \
		- L1*L3*m1*cos(g + a + b)*cos(b)*b_d**2 
