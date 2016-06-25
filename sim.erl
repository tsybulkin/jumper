%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% 
% this module provides physical simulation of the jumper
%
% Ian Tsybulkin, 2016
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

-module(sim).
-export([run/2, run1/2
		]).


run(Tau,T) -> 
	io:format("Time   A  A_der  B  B_der  Psi~n"),
	run(phy:init(),Tau,T,[]).

run(_,_,T,Log) when T<0 -> show:make_demo(lists:reverse(Log));
run(Pos,Tau,T,Log) -> 
	Pos1 = phy:next_position(Pos,0,Tau),
	io:format("~p~n",[Pos1]),
	run(Pos1,Tau,T-Tau,[Pos1|Log]).


run1(Tau,T) -> 
	run1(phy1:init(),Tau,T,[]).

run1(_,Tau,T,Log) when T<0 -> show1:make_demo(lists:reverse(Log),Tau);
run1(Pos,Tau,T,Log) -> 
	Pos1 = phy1:next_position(Pos,0,Tau),
	io:format("~p~n",[Pos1]),
	run1(Pos1,Tau,T-Tau,[Pos1|Log]).
