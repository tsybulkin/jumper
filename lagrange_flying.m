%
%
%g = 9.81;
%m1 = 0.20;
%m2 = 0.05;
%L1 = 0.05;
%L2 = 0.15;
%L3 = 0.10;
%I1 = 0.1e-3;
%gama = 0.1;

syms a(t) b(t) gama(t) x y psi eps g m1 m2 L1 L2 L3 I1 I2 z0 z1 z2 z3 k1 k2 k3 dz da;

x1 = x + L3*cos(b) + L2*cos(b+gama) + L1*cos(a+b+gama);
y1 = y + L3*sin(b) + L2*sin(b+gama) + L1*cos(a+b+gama);

x2 = x + L3*cos(b) + L2*eps*cos(b+gama);
y2 = y + L3*sin(b) + L2*eps*sin(b+gama);

u1 = dz + z0*sin(psi) - z1*cos(a);
u2 = dz - z0*sin(psi) + z2*cos(a);
u3 = da + z3*cos(gama);


T = m1/2*(diff(x1,t)^2 + diff(y1,t)^2) + I1/2*(diff(a,t)^2 + diff(b,t)^2 + diff(gama,t)^2) + ...
	m2/2*(diff(x2,t)^2 + diff(y2,t)^2) + I2/2*(diff(b,t) + diff(gama,t))^2;

V = m1*g*y1 + k1/2*u1^2 + k2/2*u2^2 + m2*g*y2 + k3/2*u3^2;

L = T-V