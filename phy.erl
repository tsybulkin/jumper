%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 
% this module provides physical simulation of the jumper
%
% Ian Tsybulkin, 2016
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

-module(phy).
-export([init/0, init/2,
		next_position/3,
		get_XYa/3, get_XYh/3, get_XY0/4, get_XY1/3
		]).

-define(L,  0.1). % leg's length
-define(M1, 0.20). % the mass of the body
-define(M2, 0.05). % the mass of the leg
-define(Foot,0.05).
-define(Eta, math:atan(?L/?Foot)).
-define(Rh, math:sqrt(?L*?L + ?Foot*?Foot)).
-define(Eta0, 0.6).
-define(R0, 0.04). % distance from tip of foot to the leg's CoM

%% springs params
-define(Z0, 0.025).
-define(Z1, 0.025).
-define(Z2, 0.025).
-define(K1, 200.0).
-define(K2, 200.0).
-define(Dz, 0.02). % initial strech of the springs

-define(I1, 1.00e-3). % Inertial moment of the body arounf CoM
-define(I2, 1.25e-4). % Inertial moment of the leg around tip of foot
-define(K0, 0.01). % The coefficient of friction between the body and the leg
-define(D, 0.03). % The distance between body CoM and hip
-define(G, 9.81).


init() -> init(1.6, 0.1).

init(Alpha, Beta) -> {Alpha, 0.0, Beta, 0.0, 0.0}.


next_position({A,A_der,B,B_der,Psi},New_Psi,Tau) ->
	% consider estimating energy injection or consumption
	E11 = ?I1, E12 = i11(A),
	E21 = i21(A), E22 = i22(A),

	C1 = (f1(A,B,Psi) - i12(A)*B_der*B_der)*Tau*Tau +
		?I1*(A+A_der*Tau) + E12*(B+B_der*Tau),
	C2 = (f2(A,B) - i23(A)*A_der*A_der - i24(A)*A_der*B_der)*Tau*Tau + 
		E21*(A+A_der*Tau) + E22*(B+B_der*Tau),
	%io:format("I1=~p~n",[?I1]),
	%io:format("I11=~p~n",[E12]),
	%io:format("I21=~p~n",[E21]),
	%io:format("I12=~p~n",[i12(A)]),
	%io:format("I22=~p~n",[E22]),
	%io:format("I23=~p~n",[i23(A)]),
	%io:format("I24=~p~n",[i24(A)]),
	%io:format("f1=~p~n",[f1(A,B,Psi)]),
	%io:format("f2=~p~n",[f2(A,B)]),
	
	Det = E11*E22 - E12*E21,
	A1 = (C1*E22 - C2*E12)/Det,
	B1 = (C2*E11 - C1*E21)/Det,
	{A1, (A1-A)/Tau, B1, (B1-B)/Tau, New_Psi}.

%
% I1*A'' + i11*B'' + i12*B'^2 = f1(A,B,Psi)
%
% I21*A'' + i22*B'' + i23*A'^2 + i24*A'*B' = f2(A,B,Psi)
%
i11(A) -> ?I1 - ?M1*?Rh*?D*math:sin(A).
i12(A) -> ?M1*?Rh*?D*math:cos(A).

i21(A) -> ?I1 + ?M1*?D*?D + ?M1*?Rh*?D*math:sin(A).
i22(A) -> ?I1 + ?I2 + ?M1*(?Rh*?Rh+?D*?D) + 2*?M1*?Rh*?D*math:sin(A).
i23(A) -> ?M1*?Rh*?D*math:cos(A).
i24(A) -> 2*?M1*?Rh*?D*math:cos(A). 


f1(A,B,Psi) ->  (?K1*?Z1*?Z1 + ?K2*?Z2*?Z2)*math:sin(A)*math:cos(A) +
				(?K2*psi2(Psi)*?Z2 - ?K1*psi1(Psi)*?Z1)*math:sin(A) +
				?M1*?G*?D*math:sin(?Eta+A+B).

f2(A,B) ->	?M1*?G*?Rh*math:cos(?Eta+B) +
			?M1*?G*?D*math:sin(?Eta+A+B) -
			?M2*?G*?R0*math:cos(?Eta0+B).


psi1(Psi) -> ?Dz + ?Z0*math:sin(Psi).

psi2(Psi) -> ?Dz - ?Z0*math:sin(Psi).


get_XYa(Xt,Yt,B) -> {Xt+?Foot*math:cos(B), Yt+?Foot*math:sin(B)}.

get_XYh(Xt,Yt,B) -> {Xt+?Rh*math:cos(?Eta+B), Yt+?Rh*math:sin(?Eta+B)}.

get_XY0(Xt,Yt,A,B)->{Xt+?Rh*math:cos(?Eta+B)-?D*math:sin(A+B), 
					 Yt+?Rh*math:sin(?Eta+B)+?D*math:cos(A+B)}.

get_XY1(Xt,Yt,B) -> {Xt+?R0*math:cos(?Eta0+B), Yt+?R0*math:sin(?Eta0+B)}.
