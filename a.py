Derivative(a, t, t) 
I1 + 2*L1**2*m1*sin(a + b + gama)**2

Derivative(b, t, t) 
+ 2*L1**2*m1*sin(a + b + gama)**2
+ L1*L2*m1*sin(b + gama)*sin(a + b + gama) 
- L1*L2*m1*sin(a + b + gama)*cos(b + gama) 
+ L1*L3*m1*sin(a + b + gama)*sin(b) 
- L1*L3*m1*sin(a + b + gama)*cos(b) 

Derivative(gama, t, t)
+ 2*L1**2*m1*sin(a + b + gama)**2
+ L1*L2*m1*sin(b + gama)*sin(a + b + gama) 
- L1*L2*m1*sin(a + b + gama)*cos(b + gama)


+ L1**2*m1*sin(2*a + 2*b + 2*gama)*Derivative(a, t)**2 
+ 2*L1**2*m1*sin(2*a + 2*b + 2*gama)*Derivative(a, t)*Derivative(b, t) 
+ 2*L1**2*m1*sin(2*a + 2*b + 2*gama)*Derivative(a, t)*Derivative(gama, t) 
+ L1**2*m1*sin(2*a + 2*b + 2*gama)*Derivative(b, t)**2 
+ 2*L1**2*m1*sin(2*a + 2*b + 2*gama)*Derivative(b, t)*Derivative(gama, t) 
+ L1**2*m1*sin(2*a + 2*b + 2*gama)*Derivative(gama, t)**2 
+ L1*L2*m1*sin(b + gama)*sin(a + b + gama)*Derivative(b, t)**2 
+ 2*L1*L2*m1*sin(b + gama)*sin(a + b + gama)*Derivative(b, t)*Derivative(gama, t) 
+ L1*L2*m1*sin(b + gama)*sin(a + b + gama)*Derivative(gama, t)**2 
+ L1*L2*m1*sin(a + b + gama)*cos(b + gama)*Derivative(b, t)**2 
+ 2*L1*L2*m1*sin(a + b + gama)*cos(b + gama)*Derivative(b, t)*Derivative(gama, t) 
+ L1*L2*m1*sin(a + b + gama)*cos(b + gama)*Derivative(gama, t)**2 
+ L1*L3*m1*sin(a + b + gama)*sin(b)*Derivative(b, t)**2 
+ L1*L3*m1*sin(a + b + gama)*cos(b)*Derivative(b, t)**2 
- L1*g*m1*sin(a + b + gama) + dz*k1*z1*sin(a) - dz*k2*z2*sin(a) 
+ k1*z0*z1*sin(psi)*sin(a) - k1*z1**2*sin(2*a)/2 + k2*z0*z2*sin(psi)*sin(a) 
- k2*z2**2*sin(2*a)/2


