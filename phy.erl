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
-define(Eta0, 0.45).
-define(R0, 0.04). % distance from tip of foot to the leg's CoM

%% springs params
-define(Z0, 0.025).
-define(Z1, 0.025).
-define(Z2, 0.025).
-define(K1, 200.0).
-define(K2, 200.0).
-define(Dz, 0.03). % initial strech of the springs

-define(I1, 1.00e-3). % Inertial moment of the body arounf CoM
-define(I2, 1.25e4). % Inertial moment of the leg around tip of foot
-define(K0, 0.01). % The coefficient of friction between the body and the leg
-define(D, 0.03). % The distance between body CoM and hip
-define(G, 9.81).


init() -> init(1.4, 0.27).

init(Alpha, Beta) -> {Alpha, 0.0, Beta, 0.0, 0.0}.


next_position({A,A_der,B,B_der,Psi},New_Psi,Tau) ->
	% consider estimating energy injection or consumption
	E11 = i11(A,B), E12 = i13(A,B),
	E21 = i21(A), E22 = i23(A),

	C1 = (f1(A,B,Psi)-i12(A,B)*A_der*A_der-i14(A,B)*B_der*B_der-i15(A,B)*A_der*B_der)*Tau*Tau
		+ i11(A,B)*(A+A_der*Tau) + i13(A,B)*(B+B_der*Tau),
	C2 = (f2(A,B) - i22(A,B)*A_der*A_der - i24(A,B)*B_der*B_der - i25(A)*A_der*B_der)*Tau*Tau 
		+ i21(A)*(A+A_der*Tau) + i23(A)*(B+B_der*Tau),
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
% I11*A'' + i12*A'^2 + i13*B'' + i14*B'^2 + i15*A'*B' = f1(A,B,Psi)
%
% I21*A'' + i22*A'^2 +i23*B'' + i24*B'^2  + i25*A'B' = f2(A,B)
%
i11(_A,_B) -> ?I1 - ?K0 + ?M1*?D*?D.
i12(_A,_B) -> 0.
i13(A,_B) -> ?I1 + ?M1*?Rh*?D*math:sin(?Eta-A) + ?M1*?D*?D.
i14(A,_B) -> ?M1*?D*?Rh*math:cos(A-?Eta).
i15(_A,_B) -> 0.


i21(A) -> ?I1 + ?M1*(?Rh*?D*math:sin(?Eta-A) + ?D*?D).
i22(A,B) -> 2*?M1*?D*?D*math:sin(A+B)*math:cos(A+B)-?M1*?Rh*?D*math:cos(?Eta-A).
i23(A) -> ?I1 +?I2 + ?M1*(?Rh*?Rh + 2*?Rh*?D*math:sin(?Eta-A) + ?D*?D).
i24(A,B) -> 2*?M1*?D*?D*math:sin(A+B)*math:cos(A+B). 
i25(A) -> -2*?M1*?Rh*?D*math:cos(?Eta-A).


f1(A,B,Psi) ->  ?M1*?G*?D*math:sin(A+B)
				- ?K1*?Z1*(?Dz + ?Z0*math:sin(Psi) - ?Z1*math:cos(A) )*math:sin(A)
				+ ?K2*?Z2*(?Dz - ?Z0*math:sin(Psi) + ?Z2*math:cos(A) )*math:sin(A).

f2(A,B) ->	- ?M2*?G*?R0*math:cos(?Eta0+B)
			- ?M1*?G*(?Rh*math:cos(?Eta+B) - ?D*math:sin(A+B)).
			

get_XYa(Xt,Yt,B) -> {Xt+?Foot*math:cos(B), Yt+?Foot*math:sin(B)}.

get_XYh(Xt,Yt,B) -> {Xt+?Rh*math:cos(?Eta+B), Yt+?Rh*math:sin(?Eta+B)}.

get_XY0(Xt,Yt,A,B)->{Xt+?Rh*math:cos(?Eta+B)-?D*math:sin(A+B), 
					 Yt+?Rh*math:sin(?Eta+B)+?D*math:cos(A+B)}.

get_XY1(Xt,Yt,B) -> {Xt+?R0*math:cos(?Eta0+B), Yt+?R0*math:sin(?Eta0+B)}.
