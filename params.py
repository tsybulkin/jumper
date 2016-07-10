# This is robots parameters
#

g = 9.81
m1 = 0.20
m2 = 0.05
L1 = 0.06
L2 = 0.15
L3 = 0.09
I1 = m1/2 * L1**2
I2 = m2/8 * L2**2 

gama0 = 0.4 # minimal angle between foot and leg when robot flies
eps = 0.5 # eps*L2 is the distance from the anckle to the center of mass of the leg
x,y = 0.3, 0 # coords of the toe tip

z0 = 0.02 # leverage of the leg's servo
z1 = 0.02 
z2 = 0.02
z3 = 0.02 
k1 = 200 # spring's coeffs
k2 = 200
k3 = 50
dz = 0.05 # initial stretch of the springs
da = 0.07

miu1 = 0.02
miu2 = 0.02
