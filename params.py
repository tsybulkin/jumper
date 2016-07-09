# This is robots parameters
#

g = 9.81
m1 = 0.20
m2 = 0.05
L1 = 0.06
L2 = 0.2
L3 = 0.10
I1 = 0.1e-3
I2 = 0.1e-4

gama0 = 0.1 # minimal angle between foot and leg when robot flies
eps = 0.5 # eps*L2 is the distance from the anckle to the center of mass of the leg
x,y = 10,0 # coords of the toe tip

z0 = 0.02 # leverage of the leg's servo
z1 = 0.03 
z2 = 0.03
z3 = 0.03 
k1 = 200 # spring's coeffs
k2 = 200
k3 = 5000
dz = 0.05 # initial stretch of the springs
da = 0.1

miu1 = 0.02
miu2 = 0.02
