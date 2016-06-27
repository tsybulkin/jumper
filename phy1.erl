%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 
% this module provides physical simulation of pendulum with spring
%
% Ian Tsybulkin, 2016
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

-module(phy1).
-export([init/0, init/1, get_XYm/3, get_servo/4,
		next_position/3
		]).

-define(L,  0.1). % leg's length
-define(M, 0.10). % the mass of the body
-define(K0, 0.02). % friction in the shoulder

%% springs params
-define(Z0, 0.03).
-define(Z1, 0.025).
-define(Z2, 0.025).
-define(K1, 300.0).
-define(K2, 200.0).
-define(Dz, 0.03). % initial strech of the springs

-define(G, 9.81).


init() -> init(1.5).

init(Alpha) -> {Alpha, 0.0, 0.0}.


next_position({A,A_der,Psi},New_Psi,Tau) ->
	% consider estimating energy injection or consumption
	A_new = A + A_der*Tau + (f1(A,Psi) - ?K0*A_der)*Tau*Tau/?M/?L/?L,
	{A_new, (A_new-A)/Tau, New_Psi}.

%
%


f1(A,Psi) -> 	( ?M*?G*?L
				- ?K1*?Z1*(?Dz + ?Z0*math:sin(Psi) - ?Z1*math:cos(A) )
				+ ?K2*?Z2*(?Dz - ?Z0*math:sin(Psi) + ?Z2*math:cos(A) ))*math:sin(A).


get_XYm(X,Y,A) -> {X-?L*math:sin(A), Y+?L*math:cos(A)}.


get_servo(X,Y,A,Psi) -> {X+?Z0*math:cos(A+Psi), Y+?Z0*math:sin(A+Psi),
						 X-?Z0*math:cos(A+Psi), Y-?Z0*math:sin(A+Psi)}.


