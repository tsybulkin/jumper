%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 
% this module provides physical simulation of the jumper
%
% Ian Tsybulkin, 2016
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

-module(phy).
-export([init/0, init/2,
		next_position/3
		]).

-define(L,  0.01).
-define(M1, 0.20).
-define(M2, 0.05).
-define(Foot,0.05).
-define(Eta, math:atan(?L/?Foot)).
-define(Z0, 0.025).
-define(Z1, 0.025).
-define(Z2, 0.025).
-define(K1, 200.0).
-define(K2, 200.0).




init() -> init(1.0, 0.6).

init(Alpha, Beta) -> {Alpha, 0.0, Beta, 0.0, 0.0}.


next_position({A,A_der,B,B_der,Psi},New_Psi,Tau) ->
	% consider estimating energy injection or consumption
	case estimate(A,A_der,B,B_der,Psi,Tau) of
		{A1,B1} -> {A1,(A1-A)/Tau,B1,(B1-B)/Tau,New_Psi};
		_ -> io:format("ERROR: differential equations of motion diverged~n")
	end.


estimate(A,A_der,B,B_der,Psi,Tau) -> io:format("eta = ~p~n",[?Eta]).

