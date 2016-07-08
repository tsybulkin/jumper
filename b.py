Derivative(a, t, t) 
+ 2*L1**2*m1*sin(a + b + gama)**2 
+ L1*L2*m1*sin(b + gama)*sin(a + b + gama)
- L1*L2*m1*sin(a + b + gama)*cos(b + gama)
+ L1*L3*m1*sin(a + b + gama)*sin(b)
- L1*L3*m1*sin(a + b + gama)*cos(b)


Derivative(b, t, t) 
+ I1 + I2 + L2**2*eps**2*m2 + L2**2*m1 + L3**2*m1 + L3**2*m2 
+ 2*L1**2*m1*sin(a + b + gama)**2 
- 2*L1*L2*m1*sin(a + b + gama)*cos(b + gama)
+ 2*L1*L2*m1*sin(b + gama)*sin(a + b + gama) 
+ 2*L1*L3*m1*sin(a + b + gama)*sin(b)
- 2*L1*L3*m1*sin(a + b + gama)*cos(b)
+ 2*L2*L3*eps*m2*sin(b + gama)*sin(b)
+ 2*L2*L3*eps*m2*cos(b + gama)*cos(b)
+ 2*L2*L3*m1*sin(b + gama)*sin(b)
+ 2*L2*L3*m1*cos(b + gama)*cos(b)


Derivative(gama, t, t) 
+ I2 + L2**2*eps**2*m2 + L2**2*m1 
+ 2*L1**2*m1*sin(a + b + gama)**2 
- 2*L1*L2*m1*sin(a + b + gama)*cos(b + gama)
+ 2*L1*L2*m1*sin(b + gama)*sin(a + b + gama)
+ L1*L3*m1*sin(a + b + gama)*sin(b)
- L1*L3*m1*sin(a + b + gama)*cos(b)
+ L2*L3*eps*m2*sin(b + gama)*sin(b)
+ L2*L3*eps*m2*cos(b + gama)*cos(b)
+ L2*L3*m1*sin(b + gama)*sin(b)
+ L2*L3*m1*cos(b + gama)*cos(b)



+ L1**2*m1*sin(2*a + 2*b + 2*gama)*Derivative(a, t)**2 
+ 2*L1**2*m1*sin(2*a + 2*b + 2*gama)*Derivative(a, t)*Derivative(b, t) 
+ 2*L1**2*m1*sin(2*a + 2*b + 2*gama)*Derivative(a, t)*Derivative(gama, t) 
+ L1**2*m1*sin(2*a + 2*b + 2*gama)*Derivative(b, t)**2 
+ 2*L1**2*m1*sin(2*a + 2*b + 2*gama)*Derivative(b, t)*Derivative(gama, t) 
+ L1**2*m1*sin(2*a + 2*b + 2*gama)*Derivative(gama, t)**2 
+ L1*L2*m1*sin(b + gama)*sin(a + b + gama)*Derivative(b, t)**2 
+ 2*L1*L2*m1*sin(b + gama)*sin(a + b + gama)*Derivative(b, t)*Derivative(gama,t) 
+ L1*L2*m1*sin(b + gama)*sin(a + b + gama)*Derivative(gama, t)**2 
+ L1*L2*m1*sin(b + gama)*cos(a + b + gama)*Derivative(a, t)**2 
+ 2*L1*L2*m1*sin(b + gama)*cos(a + b + gama)*Derivative(a, t)*Derivative(b, t) 
+ 2*L1*L2*m1*sin(b + gama)*cos(a + b + gama)*Derivative(a, t)*Derivative(gama, t) 
+ L1*L2*m1*sin(b + gama)*cos(a + b+ gama)*Derivative(b, t)**2 
+ 2*L1*L2*m1*sin(b + gama)*cos(a + b + gama)*Derivative(b, t)*Derivative(gama, t) 
+ L1*L2*m1*sin(b + gama)*cos(a + b + gama)*Derivative(gama, t)**2 
+ L1*L2*m1*sin(a + b + gama)*cos(b + gama)*Derivative(b, t)**2 
+ 2*L1*L2*m1*sin(a + b + gama)*cos(b + gama)*Derivative(b, t)*Derivative(gama, t) 
+ L1*L2*m1*sin(a + b + gama)*cos(b + gama)*Derivative(gama, t)**2 
- L1*L2*m1*cos(b + gama)*cos(a + b + gama)*Derivative(a, t)**2 
- 2*L1*L2*m1*cos(b + gama)*cos(a + b + gama)*Derivative(a, t)*Derivative(b, t) 
- 2*L1*L2*m1*cos(b + gama)*cos(a + b + gama)*Derivative(a, t)*Derivative(gama, t) 
- L1*L2*m1*cos(b + gama)*cos(a + b+ gama)*Derivative(b, t)**2 
- 2*L1*L2*m1*cos(b + gama)*cos(a + b + gama)*Derivative(b, t)*Derivative(gama, t) 
- L1*L2*m1*cos(b + gama)*cos(a + b + gama)*Derivative(gama, t)**2 
+ L1*L3*m1*sin(a + b + gama)*sin(b)*Derivative(b, t)**2 
+ L1*L3*m1*sin(a + b + gama)*cos(b)*Derivative(b, t)**2 
+ L1*L3*m1*sin(b)*cos(a + b + gama)*Derivative(a, t)**2 
+ 2*L1*L3*m1*sin(b)*cos(a + b + gama)*Derivative(a, t)*Derivative(b, t) 
+ 2*L1*L3*m1*sin(b)*cos(a + b + gama)*Derivative(a, t)*Derivative(gama, t) 
+ L1*L3*m1*sin(b)*cos(a + b + gama)*Derivative(b, t)**2 
+ 2*L1*L3*m1*sin(b)*cos(a + b + gama)*Derivative(b, t)*Derivative(gama, t) 
+ L1*L3*m1*sin(b)*cos(a + b + gama)*Derivative(gama, t)**2 
- L1*L3*m1*cos(a + b + gama)*cos(b)*Derivative(a, t)**2 
- 2*L1*L3*m1*cos(a + b + gama)*cos(b)*Derivative(a, t)*Derivative(b, t) 
- 2*L1*L3*m1*cos(a + b + gama)*cos(b)*Derivative(a, t)*Derivative(gama, t) 
- L1*L3*m1*cos(a + b + gama)*cos(b)*Derivative(b, t)**2 
- 2*L1*L3*m1*cos(a + b + gama)*cos(b)*Derivative(b, t)*Derivative(gama, t) 
- L1*L3*m1*cos(a + b + gama)*cos(b)*Derivative(gama, t)**2 
- L1*g*m1*sin(a + b + gama) 
- 2*L2*L3*eps*m2*sin(b + gama)*cos(b)*Derivative(b, t)*Derivative(gama, t) 
- L2*L3*eps*m2*sin(b + gama)*cos(b)*Derivative(gama, t)**2 
+ 2*L2*L3*eps*m2*sin(b)*cos(b + gama)*Derivative(b, t)*Derivative(gama, t) 
+ L2*L3*eps*m2*sin(b)*cos(b + gama)*Derivative(gama, t)**2 
- 2*L2*L3*m1*sin(b + gama)*cos(b)*Derivative(b, t)*Derivative(gama, t) 
- L2*L3*m1*sin(b + gama)*cos(b)*Derivative(gama, t)**2 
+ 2*L2*L3*m1*sin(b)*cos(b + gama)*Derivative(b, t)*Derivative(gama, t) 
+ L2*L3*m1*sin(b)*cos(b + gama)*Derivative(gama, t)**2 
+ L3*g*m1*cos(b) + L3*g*m2*cos(b)
+ L2*eps*g*m2*cos(b + gama) + L2*g*m1*cos(b + gama) 

