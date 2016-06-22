%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 
% this module provides physical simulation of the jumper
%
% Ian Tsybulkin, 2016
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

-module(sim).
-export([run/2
		]).


run(Tau,T) -> 
	io:format("Time   A  A_der  B  B_der  Psi~n"),
	run(phy:init(),Tau,T).

run(_,_,T) when T<0 -> ok;
run(Pos,Tau,T) -> 
	case phy:next_position(Pos,0,Tau) of
		Pos1={A,A_der,B,B_der,Psi} -> 
			io:format("~p~n",[Pos1]),
			run(Pos1,Tau,T-Tau);
		_ ->
			ok
	end.